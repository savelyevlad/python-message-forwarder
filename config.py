
# questionary.text('Please provide your Telegram App api_id:', validate=IntegerValidator).unsafe_ask()
CHAT_ID = 21859429

# questionary.password(
#     'Please provide your secret Telegram App api_hash:', validate=TelegramApiHashValidator
# ).unsafe_ask()
API_HASH = '30dc40fca92e05169ce91a81777d6ad8'

# questionary.text(
#     'Please provide the source channel(s) or chat(s) username(s) or ID(s)'
#     + ' (you can provide multiple values separated with a comma, links accepted except for private groups):',
#     validate=TelegramUimage.pngsernameOrLinkValidator,
# ).unsafe_ask()
CHANNELS = '1756457498, kek_kotek'

# questionary.text(
#     'Please provide the destination chat ID or username (links accepted except for private groups):',
#     validate=TelegramUsernameOrLinkValidator,
# ).unsafe_ask()
DESTINATION = '1779394685'
