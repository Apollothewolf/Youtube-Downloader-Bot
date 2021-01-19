from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Heya!  It's a YouTube link To video/mp3 converter.currently bot supports single (no playlist). Check <a href='https://telegra.ph/How-to-use-MT-UtubeBot-01-19'>Here</a>"
    await message.reply_text(helptxt)
