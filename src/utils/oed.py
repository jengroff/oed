import os
import requests
import json

from dotenv import load_dotenv

load_dotenv()

app_id = os.getenv("OED_APP_ID")
app_key = os.getenv("OED_APP_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


def full_lookup(word: str):
    word_id = word.lower()
    language = "en-us"
    url = f"https://od-api.oxforddictionaries.com/api/v2/entries/{language}/{word_id}?strictMatch=false"
    response = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    json_response = json.loads(response.text)

    if response.status_code == 200:
        definition = json_response["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
    else:
        definition = "Sorry, the OED has no entry for that word."

    return f'"{word_id}":  {definition}'




