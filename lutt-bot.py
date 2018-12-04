import telepot
from telepot.loop import MessageLoop
from config import TOKEN
from time import sleep


db = {}
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    from_id = msg['from']['id']

    if chat_type == u'private':
        if content_type == 'text':
            if msg['text'] == '/start':
                bot.sendMessage(chat_id, '*WELCOME* 🙂', 'Markdown')

            else:
                if 'forward_from' in msg: # target forwarded message
                    target_id = msg['forward_from']['id']
                    bot.sendMessage(chat_id, target_id)
                    db[from_id] = target_id

                elif msg['text'].isdigit(): # target id
                    db[from_id] = int(msg['text'])

                else:
                    try:
                        bot.sendMessage(chat_id, '[%s](tg://user?id=%d)' % (msg['text'], db[from_id]), 'Markdown')

                    except KeyError:
                        bot.sendMessage(chat_id, 'Target id not found!')


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
while 1:
    sleep(10)
