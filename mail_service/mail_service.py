from email.encoders import encode_base64
from email.mime.base import MIMEBase
from flask import Flask, request
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import urllib
import json

app = Flask(__name__)


def send_mail(user_email, user_name, category, subject, message_body, attachment):
    reply_to = f"{user_email}"
    sender_email = os.environ["SENDER_EMAIL"]
    receiver_email = os.environ["RECEIVER_EMAIL"]
    message = MIMEMultipart("alternative")
    message["Subject"] = f"[{category}][{user_name}] {subject}"
    message["From"] = sender_email
    message["To"] = receiver_email
    message.add_header("reply-to", reply_to)
    smtp_server = os.environ["SMTP_SERVER"]
    port = os.environ["SMTP_PORT"]

    # Create the plain-text and HTML version of your message
    message.attach(MIMEText(message_body, "plain"))

    if attachment is not None:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment)
        encode_base64(part)

        part.add_header("Content-Disposition", 'attachment; filename="text.txt"')

        message.attach(part)

    server = smtplib.SMTP(smtp_server, port)
    server.connect(smtp_server, port)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()


def validate_recaptcha(recaptcha_token: str, remote_ip: str):
    URIReCaptcha = "https://www.google.com/recaptcha/api/siteverify"
    private_recaptcha = os.environ["SECRET_RECAPTCHA"]
    http_proxy = os.environ["HTTP_PROXY"]
    https_proxy = os.environ["HTTPS_PROXY"]
    remote_ip = request.remote_addr
    params = urllib.urlencode(
        {
            "secret": private_recaptcha,
            "response": recaptcha_token,
            "remote_ip": remote_ip,
        }
    )
    proxy_support = urllib.request.ProxyHandler(
        {"http": http_proxy, "https": https_proxy}
    )
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    with urllib.request.urlopen(URIReCaptcha, params.encode("utf-8")) as response:
        data = response.read()
        result = json.loads(data)
        success = result.get("success", None)
    return success


@app.route("/api/create-ticket/", methods=["POST"])
def hello_world():
    json_body = request.get_json()
    if validate_recaptcha(json_body["recaptchaToken"], request.remote_addr):
        send_mail(
            json_body["email"],
            json_body["name"],
            "Feedback form",
            "Website feedback",
            json_body["feedback"],
            None,
        )
        return request.get_json()
    return {"error": "invalid-recaptcha"}
