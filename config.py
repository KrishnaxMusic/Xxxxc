import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6760555565:AAGIhQG-s4nQ-cLBs73dUptgio2yDW5UTxs")
    API_ID = int(os.environ.get("API_ID", "23303247"))
    API_HASH = os.environ.get("API_HASH", "23623f737dc15708708c65a7297e1510")
    VIP_USER = os.environ.get('VIP_USERS', '6780082379').split(',')
    VIP_USERS = [int(user_id) for user_id in VIP_USER]
