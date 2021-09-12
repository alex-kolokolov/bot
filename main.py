from pyrogram import Client, filters, errors
from time import sleep


app = Client("my_account")


def dynamic_data_filter(data):
    return filters.create(
        lambda flt, _, query: flt.data == query.data,
        data=data  # "data" kwarg is accessed with "flt.data" above
    )


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
