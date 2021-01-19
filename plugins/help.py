from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Heya!  It's a YouTube link To video/mp3 converter.\ncurrently bot supports single (no playlist).\nCheck <a href='https://telegra.ph/How-to-use-MT-UtubeBot-01-19'>Here</a>"
await message.disable_web_page_preview(True)
    await message.reply_text(helptxt)
