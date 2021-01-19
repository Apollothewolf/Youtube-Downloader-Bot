from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("©ⱮͲ_OᖴᖴIᑕIᗩᒪ™", url="https://t.me/TheRealApollo")],
       
    ])
    welcomed = f"Heya <b>{message.from_user.first_name}</b>\nWelcome to @malluurlbot,\nThe Most Advanced utube Video and Audio Downloader in Telegram!\nplease send any YouTube url or hit /help for more info\nPlease send any utube video link or search using @vid inline mode.\n "


    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
