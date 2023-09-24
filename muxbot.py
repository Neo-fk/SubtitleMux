
# (c) mohdsabahat

import logging
logging.basicConfig(level = logging.DEBUG,
                     format="%(asctime)s - %(name)s - %(message)s - %(levelname)s")

logger = logging.getLogger(__name__)

import os

if os.path.exists('testconfig.py'):
    from testconfig import Config
else:
    from config import Config

from helper_func.dbhelper import Database as Db
db = Db().setup()

import pyrogram
logging.getLogger('pyrogram').setLevel(logging.WARNING)


if __name__ == '__main__':

    if not os.path.isdir(Config.DOWNLOAD_DIR):
        os.mkdir(Config.DOWNLOAD_DIR)

    
app = pyrogram (
        name="merge-bot",
        api_hash=Config.API_HASH,
        api_id=int(Config.TELEGRAM_API),
        bot_token=Config.BOT_TOKEN,
        workers=300,
        plugins=dict(root="plugins"),
        app_version="5.0+yash-mergebot",


    )
    app.run()
