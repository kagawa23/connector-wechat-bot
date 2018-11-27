# -*- encoding: utf-8 -*-

import threading
import time
import re
import unicodedata
from wxpy import *

bot = Bot(cache_path=True, console_qr=True)
bot.enable_puid()


def send_online_notification(name):
    my_friend = ensure_one(bot.search(name))
    while True:
        my_friend.send('I\'m Still Alive!! ' +
                       time.strftime('%y/%m/%d-%H:%M:%S', time.localtime()))
        time.sleep(3600)


positiveSendingThread = threading.Thread(
    target=send_online_notification, args=(u'xxxx',))
positiveSendingThread.setDaemon(True)
positiveSendingThread.start()

# embed()
bot.join()
