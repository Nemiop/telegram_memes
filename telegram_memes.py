import telebot
import vk_parser as vp

bot = telebot.TeleBot("870053741:AAEjGB6ozZDZKT8Rs9yj1X9ZX-Ls0tETnkg")
path_csv = "vk_mhk.csv"

@bot.message_handler(content_types=['text'])
def send_test_result(message):
    img_url, max_index = vp.lol_image(path_csv)
    message_back = "Memes left: " + str(max_index)

    bot.send_photo(message.chat.id, img_url)
    bot.send_message(message.chat.id, message_back)


bot.polling( none_stop = True)
