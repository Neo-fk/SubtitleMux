import os

class Config:

    BOT_TOKEN = os.environ.get('5800802984:AAG0EUk9edno0k83LcHcnfwT1FtPtdjdQRk', None)
    APP_ID = os.environ.get('22404062', None)
    API_HASH = os.environ.get('162d4eb8c9cbfe558121c6cf41f8df43', None)

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1165215979').split(',')]

    DOWNLOAD_DIR = 'downloads'
