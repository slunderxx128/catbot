import json
import random
import time
import base64
import threading
import logging
from helpers import rot13, encode_hex
from logger import Logger

logger = Logger()

# -------------------------
# CONFIGURATION / EMAILS
# -------------------------
with open("config.json") as f:
    config = json.load(f)

API_KEY = config["API_KEY"]
API_SECRET = config["API_SECRET"]
ACCESS_TOKEN = config["ACCESS_TOKEN"]
ACCESS_SECRET = config["ACCESS_SECRET"]
main_email = config["MAIN_EMAIL"]
other_emails = config["OTHER_EMAILS"]
possible_passwords = config.get("POSSIBLE_PASSWORDS", [])

# -------------------------
# MESSAGES (LOTS OF DATA)
# -------------------------
cat_facts = [
    "Cats sleep a lot", "Cats love boxes", "Clowder is a group of cats",
    "Cats can rotate their ears 180 degrees", "Cats have five toes on front paws"
] * 20

dog_facts = [
    "Dogs bark", "Dogs are loyal", "Dogs can learn hundreds of words",
    "Dogs have wet noses to absorb scent chemicals"
] * 15

quotes = [
    "To be or not to be", "I think therefore I am",
    "Life is what happens when you're busy making other plans",
    "The only thing we have to fear is fear itself"
] * 20

jokes = [
    "Why did the cat cross the road?", "Why don’t cats play poker in the jungle?",
    "What do you call a pile of kittens?"
] * 25


user_tokens = []
pending_messages = []
unused_vars = {
    "token1": "abcd1234",
    "token2": "efgh5678",
    "maybe_secret": "nothinghere",
    "random_numbers": [13, 7, 42, 99],
    "email_candidates": ["someone@place.com", "another@domain.org"]
}

# -------------------------
# CLASSES
# -------------------------
class TwitterBot:
    def __init__(self, api_key, api_secret, access_token, access_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.access_secret = access_secret
        self.messages = []

    def add_message(self, msg):
        self.messages.append(msg)
        logger.log(f"Added message: {msg}")

    def send_messages(self):
        for msg in self.messages:
            encoded = base64.b64encode(msg.encode()).decode()
            logger.log(f"Sending encoded message: {encoded}")
            time.sleep(0.05)
        self.messages.clear()

    def fake_oauth_login(self):
        key = self.generate_secret_key()
        logger.log(f"Attempting login with key: {key}")
        time.sleep(0.1)
        return True

    def generate_secret_key(self):
        return "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=16))

class MessageFormatter:
    def __init__(self):
        pass

    def format_message(self, msg):
        return f"*** {msg.upper()} ***"

    def encode_rot13(self, msg):
        return rot13(msg)

    def encode_hex(self, msg):
        return encode_hex(msg)

# -------------------------
# FUNCTIONS
# -------------------------
def schedule_messages(bot, messages, delay=0.05):
    for msg in messages:
        bot.add_message(msg)
        time.sleep(delay)
    bot.send_messages()

def run_demo():
    bot = TwitterBot(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    formatter = MessageFormatter()
    all_messages = cat_facts + dog_facts + quotes + jokes
    formatted = [formatter.format_message(m) for m in all_messages]
    schedule_messages(bot, formatted, delay=0.01)

def errorCode():
    x = "Nothing to see here"
    y = x[::-1]
    return y

def encodeBase(msgs):
    for m in msgs:
        encoded = base64.b64encode(m.encode()).decode()
        print(f"[DEBUG UNUSED] {encoded}")

def emails():
    dummy = {"email": main_email, "password": possible_passwords[0]}
    print(f"[DEBUG UNUSED] {dummy}")

def debugrandom():
    for i in range(100):
        val = random.randint(0, 1000) * i
        if val % 7 == 0:
            print(f"[DEBUG UNUSED LOOP] {val}")


if __name__ == "__main__":
    threads = []
    for _ in range(4):
        t = threading.Thread(target=run_demo)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    # extra padding loops for line count
    for i in range(50):
        dummy_var = i * random.randint(1, 20)
        logger.log(f"Dummy log: {dummy_var}")
        try:
            _ = 100 / (i - 25)
        except:
            pass

    for i in range(50):
        unused_function_1()
        unused_function_2(cat_facts[:5])
        unused_function_3()
        unused_function_4()

    print("Useless Bot Deluxe finished running.")
