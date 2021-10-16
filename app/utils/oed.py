import os
import requests
import json

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

app_id = os.getenv("OED_APP_ID")
app_key = os.getenv("OED_APP_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


class OED(BaseModel):
    word: str


def full_lookup(word: str, use: str = None):
    word_id = word.lower()
    language = "en-us"
    url = f"https://od-api.oxforddictionaries.com/api/v2/entries/{language}/{word_id}?strictMatch=false"
    response = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    json_response = json.loads(response.text)

    # etymology = json_response["results"][0]["lexicalEntries"][0]["entries"][0]["etymologies"][0]
    definition = json_response["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
    # example = json_response["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["examples"][0]["text"]

    # print(f"\nDefinition: \t{definition}")
    # print(f"Etymology: \t{etymology}")
    # print(f"Example: \t'{example}'\n")

    return f'"{word_id}":  {definition}'




