from pyrogram import Client, filters, errors
from time import sleep
import re

app = Client("my_account")


def dynamic_data_filter(data):
    return filters.create(
        lambda flt, _, query: flt.data == query.data,
        data=data  # "data" kwarg is accessed with "flt.data" above
    )


@app.on_message(filters.command("type", prefixes='.') & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ''
    chat_id, message_id = msg['chat']['id'], msg['message_id']
    typing_symbol = '▒'
    while(tbp != orig_text):
        try:
            app.edit_message_text(chat_id, message_id, f'<b>{tbp + typing_symbol}</b>', parse_mode='html')
            sleep(0.15)

            tbp = tbp + str(text)[0]
            text = text[1:]

            app.edit_message_text(chat_id, message_id, f'<b>{tbp}</b>', parse_mode='html')
            sleep(0.15)
        except errors.FloodWait as e:
            sleep(e.x)


@app.on_message(filters.command("b", prefixes='.') & filters.me)
def bold(_, msg):
    orig_text = re.split(".B |.b ", msg.text, maxsplit=1)[1]
    chat_id, message_id = msg['chat']['id'], msg['message_id']
    app.edit_message_text(chat_id, message_id, f'<b>{orig_text}</b>', parse_mode='html')


@app.on_message(filters.command("i", prefixes='.') & filters.me)
def italic(_, msg):
    orig_text = re.split(".I |.i ", msg.text, maxsplit=1)[1]
    chat_id, message_id = msg['chat']['id'], msg['message_id']
    app.edit_message_text(chat_id, message_id, f'<i>{orig_text}</i>', parse_mode='html')


@app.on_message(filters.command("bi", prefixes='.') & filters.me)
def bold_and_italic(_, msg):
    orig_text = re.split(".Bi |.bi ", msg.text, maxsplit=1)[1]
    chat_id, message_id = msg['chat']['id'], msg['message_id']
    app.edit_message_text(chat_id, message_id, f'<b><i>{orig_text}</i></b>', parse_mode='html')


@app.on_message(filters.command("wave", prefixes='.') & filters.me)
def wave(_, msg):
    orig_text = msg.text.split(".wave", maxsplit=1)[1]
    text = orig_text.lower()
    tbp = text
    for j in range(5):
        for i in range(0, len(text)):
            try:
                msg.edit(tbp[:i] + tbp[i].upper() + tbp[i + 1:])
                sleep(0.1)
            except errors.FloodWait as e:
                sleep(e.x)
        if tbp != tbp.lower():
            msg.edit(tbp.lower())


@app.on_message(filters.command("Я гуль", prefixes='') & filters.me)
def zxc(_, msg):
    a = 1000
    contacts = app.get_contacts()
#    print(contacts)
    while a > 0:
        try:
            app.send_message(msg["chat"]["id"], f"<b>{a} - 7 = {a - 7}</b>", parse_mode="html")
            a -= 7
        except errors.FloodWait as e:
            sleep(e.x)
    app.send_message(msg["chat"]["id"], "<b><i>let me die</i></b>", parse_mode="html")


app.run()
