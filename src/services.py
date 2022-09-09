from dataclasses import replace


from typing import Dict, List
import random as _random
import json as _json


def _get_quotes() -> List:
    with open("quotes.json") as quotes_file:
        quotes = _json.load(quotes_file)

        return quotes


def _sub_for_dog_sounds(quote):
    dog_sounds = ["bark", "woof", "howl"]
    word_sub_list = ["think", "say", "set", "need", "knowledge", "come", "know.", "feel", "learn", "get", "teach",
                     "know", "claim", "grasp", "understand", "have", "live", "claim"]
    for word in word_sub_list:
        if word in quote:
            return quote.replace(word, _random.choice(dog_sounds))
            # return f"found it - {quote}"

    return quote


def _get_random_quote() -> Dict:
    quotes = _get_quotes()
    quote = _random.choice(quotes)

    return quote


def _form_tweet(quote: Dict[str, str]) -> str:
    not_sure = ["maybe", "or something like that",
                "but im paraphrasing", " *tilts head", "but i could be wrong"]
    author = quote["author"].strip(",")
    dog_tweet = _sub_for_dog_sounds(f"{quote['quote'].lower()}")
    # dog_tweet = _sub_for_dog_sounds(
    #     "you don’t need scores of suitors. you need only one… if he’s the right one.")
    tweet = f"{dog_tweet} - {author}...{_random.choice(not_sure)}"

    return tweet


def _is_valid_characters(tweet: str) -> bool:
    return len(tweet) <= 280


def get_tweet():
    while True:
        quote = _get_random_quote()
        tweet = _form_tweet(quote)
        if _is_valid_characters(tweet):
            return tweet
        return tweet

