from email.encoders import encode_base64
from email.mime.base import MIMEBase
from flask import Flask, request
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

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
    server = os.environ["SMTP_SERVER"]
    port = os.environ["SMTP_PORT"]
    print(
        f"sender_email: {user_email} | receiver_email: {receiver_email} | server: {server} | port: {port}",
        flush=True,
    )

    # Create the plain-text and HTML version of your message
    message.attach(MIMEText(message_body, "plain"))

    if attachment is not None:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment)
        encode_base64(part)

        part.add_header("Content-Disposition", 'attachment; filename="text.txt"')

        message.attach(part)

    server = smtplib.SMTP(os.environ["SMTP_SERVER"], os.environ["SMTP_PORT"])
    server.connect(os.environ["SMTP_SERVER"], os.environ["SMTP_PORT"])
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()


@app.route("/api/create-ticket/", methods=["POST"])
def hello_world():
    json_body = request.get_json()
    send_mail(
        json_body["user_email"],
        json_body["user_name"],
        json_body["category"],
        json_body["subject"],
        json_body["message_body"],
        None,
    )
    return request.get_json()
