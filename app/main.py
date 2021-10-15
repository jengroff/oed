import requests
import json
import argparse


parser = argparse.ArgumentParser(description='required arguments: the word (str) you want to look up')
parser.add_argument('word', type=str, help='the specific word you want to look up')
args = parser.parse_args()

word = args.word


def oed_full(word: str):
    app_id = "f2bb346a"
    app_key = "3255d6901f3b2760b1d4c510f9444e99"
    language = 'en-us'
    word_id = word.lower()

    url = f"https://od-api.oxforddictionaries.com/api/v2/entries/{language}/{word_id}?strictMatch=false"

    response = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    json_response = json.loads(response.text)

    etymology = json_response["results"][0]["lexicalEntries"][0]["entries"][0]["etymologies"][0]
    definition = json_response["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
    example = json_response["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["examples"][0]["text"]

    print(f"\nDefinition: \t{definition}")
    print(f"Etymology: \t{etymology}")
    print(f"Example: \t'{example}'\n")


if __name__ == "__main__":
    oed_full(word)
