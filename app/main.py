import os

from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from utils.oed import full_lookup

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


def create_app():
    # instantiate the app
    app = Flask(__name__)
    app.run(port=5050, debug=True)

    return app


app = create_app()


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    word = request.form['Body']

    resp = MessagingResponse()
    resp.message(full_lookup(word))
    return str(resp)

#
# if __name__ == "__main__":
#     create_app()
