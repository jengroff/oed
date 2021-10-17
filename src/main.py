import os

from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from src.utils.oed import full_lookup

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    word = request.form['Body']

    resp = MessagingResponse()
    resp.message(full_lookup(word))
    return str(resp)
