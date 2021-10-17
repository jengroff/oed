from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from werkzeug.middleware.proxy_fix import ProxyFix

from src.utils.oed import full_lookup


def create_app():

    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

    return app


app = create_app()


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    word = request.form['Body']

    resp = MessagingResponse()
    resp.message(full_lookup(word))
    return str(resp)
