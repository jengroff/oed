import os

from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from fastapi import FastAPI
import uvicorn

from utils.oed import full_lookup, OED

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

app = FastAPI()


@app.get("/sms", response_model=OED, status_code=201)
def sms_reply(word):
    resp = MessagingResponse()
    resp.message(full_lookup(word))
    return str(resp)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=5050, reload=True)
