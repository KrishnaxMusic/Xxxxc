import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7300349510:AAH9djPuiZCyuj9DqNV-K7U7YadQ_qIC9Hg")
    API_ID = int(os.environ.get("API_ID", "23303247"))
    API_HASH = os.environ.get("API_HASH", "23623f737dc15708708c65a7297e1510")
    VIP_USER = os.environ.get('VIP_USERS', '6335525003').split(',')
    VIP_USERS = [int(user_id) for user_id in VIP_USER]
