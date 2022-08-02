from admin import *
from words import word, g_text
import telebot
from telebot import types
import os
from flask import Flask, request
import math
import ast



server = Flask(__name__)
members_dict = {}
text_queue = {}
admins = ["599040955", "818958117"]
bot = telebot.TeleBot('5514371847:AAHyXwFZWL4Ak_EEXFa6CigjYGQFqquaCqI')
start_menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
b1 = types.KeyboardButton(text='Ввести текст')
b2 = types.KeyboardButton(text="Пропуски вместо гласных")
b3 = types.KeyboardButton(text="Цвет гласных")
b4 = types.KeyboardButton(text="Регистр букв")
start_menu.add(b1, b2, b3, b4)
oops = 'Упс, кажется у вас нет доступа, свяжитесь с @dina_Dj'


@bot.message_handler(commands=['start'])
def answer(message):
    global start_menu
    if message.chat.id in get_ids():
        bot.send_message(chat_id=message.chat.id, text='Отправьте слово или несколько слов через пробел.\nВоспользуйтесь кнопками ниже, для ввода текста, замены определенных гласных на пробелы, выбора цвета гласных и изменения регистра букв. Для того, чтобы поставить ударение, напишите символ * после ударной гласной. Например: словома*стер', reply_markup=start_menu)
    else:
        bot.send_message(chat_id=message.chat.id, text=oops)

@bot.message_handler(commands=['admin'])
def menu(message):
    if message.chat.id not in admins:
        bot.send_message(chat_id=message.chat.id, text="Эта команда только для админов")
        return
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton(text='Добавить пользователя', callback_data='add_user')
    b2 = types.InlineKeyboardButton(text='Удалить кого-нибудь', callback_data='delete_user')
    markup.add(b1, b2)
    bot.send_message(chat_id=message.chat.id, text='Главное меню администратора', reply_markup=markup)

@bot.callback_query_handler(lambda query: query.data == 'add_user')
def ask_for_message(query):
    bot.send_message(chat_id=query.message.chat.id, text='Отлично, теперь перешлите мне любое сообщение от пользователя, которого хотите добавить. Только так я смогу узнать его айди')
    message = query.message
    bot.register_next_step_handler(message, ask_name)

def ask_name(message):
    try:
        id = message.forward_from.id
    except: 
         bot.send_message(chat_id=message.chat.id, text='Не похоже на пересланное сообщение...\nПопробуйте снова')
         menu(message)
         return
    bot.send_message(chat_id=message.chat.id, text='Как вы хотите назвать пользователя?')
    bot.register_next_step_handler(message, add, id=id)

def add(message, id):
    try:
        add_user(id, message.text, 'normal', 'false', 'false')
        bot.send_message(chat_id=message.chat.id, text=f'Успех! {message.text} теперь имеет доступ к боту')
        bot.send_message(chat_id=id, text='Привет, я Словомастер, спешу сообщить, что Вам открыт доступ ко всем моим функциям. Приятного использования!', reply_markup=start_menu)
        bot.send_message(chat_id=message.chat.id, text='Отправьте слово или несколько слов через пробел.\nВоспользуйтесь кнопками ниже, для ввода текста, замены определенных гласных на пробелы, выбора цвета гласных и изменения регистра букв. Для того, чтобы поставить ударение, напишите символ * после ударной гласной. Например: словома*стер', reply_markup=start_menu)
    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text=f'Что-то не так, попробуйте еще раз. Ошибка {e}')
        menu(message)

@bot.callback_query_handler(lambda query: query.data == 'delete_user')
def users_list(query):
    users = get_users_list()
    markup = types.InlineKeyboardMarkup(row_width=1)
    for user in users:
        markup.add(types.InlineKeyboardButton(text=user, callback_data=f'delete_{user}'))
    bot.send_message(chat_id=query.message.chat.id, text='Нажмите на пользователя, которого хотите удалить', reply_markup=markup)

@bot.callback_query_handler(lambda query: query.data[:6] == 'delete')
def delete(query):
    if delete_user(query.data[7:]):
        bot.send_message(query.message.chat.id, text=f'Пользователь {query.data[7:]} успешно удален')
    else:
        bot.send_message(chat_id=query.message.chat.id, text='Что-то не так, попробуйте еще раз')
        menu(query.message)

    
@bot.message_handler(commands=['text'])
def ask_text(message):
    if message.chat.id not in get_ids():
        bot.send_message(chat_id=message.chat.id, text=oops)
        return
    global exit
    global text_queue
    exit = False
    text_queue[str(message.chat.id)] = []
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton(text='Выход', callback_data='Выход')
    markup.add(item)
    bot.send_message(chat_id=message.chat.id, text='⭕Для переноса строки на телефоне нажмите enter, на компьютере - shift+enter.\n⭕Используйте один или два символа "_" для выделение нового обзаца\n⭕Вы можете использовать разные регистры букв, точки, запятые, вопросительные и восклицательные знаки.\n⭕Чтобы в дальнейшем использовать генерацию текста просто отправьте боту команду /text.\n⭕Нажмите "Выход", если хотите выйти', reply_markup=markup)
    bot.send_message(chat_id=message.chat.id, text='📝Отправьте текст👇')
    bot.register_next_step_handler(message, ask_size)

def ask_size(message):
    if exit:
        return
    text1 = message.text
    text_queue[str(message.chat.id)].append(text1)
    #bot.send_message(chat_id=599040955, text=text1)
    bot.send_message(chat_id=message.chat.id, text='Вы можете выбрать размер текста. Средний - 25. Отправьте просто число')
    bot.register_next_step_handler(message, ask_orientation)

def ask_orientation(message):
    if exit:
        del text_queue[str(message.chat.id)]
        return
    try:
        size = int(message.text)
    except:
        bot.send_message(chat_id=message.chat.id, text='Введите число')
        bot.register_next_step_handler(message, ask_orientation)
        return
    text_queue[str(message.chat.id)].append(size)
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
    item1 = types.KeyboardButton('Альбомная')
    item2 = types.KeyboardButton('Книжная')
    markup.add(item1, item2)
    bot.send_message(chat_id=message.chat.id, text='Выберите ориентацию', reply_markup=markup)
    bot.register_next_step_handler(message, create_text)

def create_text(message):
    global start_menu
    if exit:
        del text_queue[str(message.chat.id)]
        return
    orientation = message.text.lower()
    if orientation == 'альбомная' or orientation == 'книжная':
        pass
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
        item1 = types.KeyboardButton('Альбомная')
        item2 = types.KeyboardButton('Книжная')
        markup.add(item1, item2)
        bot.send_message(chat_id=message.chat.id, text='Выберите ориентацию, нажимая на кнопки внизу', reply_markup=markup)
        bot.register_next_step_handler(message, ask_orientation)
        return
    text_queue[str(message.chat.id)].append(orientation)
    mode = 'Обычный'
    try:
        msg = bot.send_message(chat_id=message.chat.id, text='Ожидайте, процесс может занять какое-то время🕒')
        text, size, orientation = text_queue[str(message.chat.id)]
        photo, text2 = g_text(text, size, orientation, message.chat.id)
        photo.save('текст.png')
        photo = open('текст.png', 'rb')
        bot.send_document(chat_id=message.chat.id, document=photo, caption='ваш текст')
        while text2 != '':
            photo, text2 = g_text(text2, size, orientation, message.chat.id)
            print(text2)
            photo.save('текст.png')
            photo = open('текст.png', 'rb')
            bot.send_document(chat_id=message.chat.id, document=photo, caption='Продолжение')
        bot.edit_message_text(text='Готово!', chat_id=message.chat.id, message_id=msg.id)
        bot.send_message(text='Возврат в меню...', chat_id=message.chat.id, reply_markup=start_menu)
    except Exception as e:
        bot.delete_message(chat_id=message.chat.id, message_id=msg.id)
        bot.send_message(chat_id=message.chat.id, text=f'Произошла ошибка {e}, попробуйте еще раз. В тексте допускаются знаки:\n!\n,\n?\n""\n_\n-\n.\n;\n:\n Заглавные и строчные буквы русского алфавита')
        bot.send_message(text='Возврат в меню...', chat_id=message.chat.id, reply_markup=start_menu)
    #bot.send_message(chat_id=599040955, text=str(text_queue))
    photo.close()
    os.remove('текст.png')
    del text_queue[str(message.chat.id)]

@bot.message_handler(func=lambda m: m.text == 'Ввести текст')
def generate_text(message):
    ask_text(message)
    
@bot.message_handler(func=lambda m: m.text == 'Пропуски вместо гласных')
def ans(message):
    k = types.InlineKeyboardMarkup(row_width=1)
    k.add(types.InlineKeyboardButton(text='Без пропусков', callback_data='normal'))
    k.add(types.InlineKeyboardButton(text='Без А-Я', callback_data='w1'))
    k.add(types.InlineKeyboardButton(text='Без У-Ю', callback_data='w2'))
    k.add(types.InlineKeyboardButton(text='Без Ы-И', callback_data='w3'))
    k.add(types.InlineKeyboardButton(text='Без Э-Е', callback_data='w4'))
    k.add(types.InlineKeyboardButton(text='Без О-Ё', callback_data='w5'))
    bot.send_message(chat_id=message.chat.id, text='Выбирайте', reply_markup=k)

@bot.message_handler(func=lambda m: m.text == 'Регистр букв')
def pick_1(message):
    k = types.InlineKeyboardMarkup(row_width=1)
    if get_info(message.chat.id)[4]:
        k.add(types.InlineKeyboardButton(text='Пусть строчные тоже появятся', callback_data='not_e'))
        bot.send_message(chat_id=message.chat.id, text='Сейчас все буквы одинакового регистра', reply_markup=k)
    else:
        k.add(types.InlineKeyboardButton(text='Пусть все будут одинаковые', callback_data='e'))
        bot.send_message(chat_id=message.chat.id, text='Сейчас регистр букв выбирается вами', reply_markup=k)

@bot.callback_query_handler(lambda query: query.data == 'not_e')
def not_even(query):
    if change_evenLetters(query.message.chat.id, "false"):
        bot.edit_message_text(text='Готово!', chat_id=query.message.chat.id, message_id=query.message.message_id)
    else:
        bot.edit_message_text(text='Произошла ошибка, попробуйте еще раз', chat_id=query.message.chat.id, message_id=query.message.message_id)

@bot.callback_query_handler(lambda query: query.data == 'e')
def even(query):
    if change_evenLetters(query.message.chat.id, "true"):
        bot.edit_message_text(text='Готово!', chat_id=query.message.chat.id, message_id=query.message.message_id)
    else:
        bot.edit_message_text(text='Произошла ошибка, попробуйте еще раз', chat_id=query.message.chat.id, message_id=query.message.message_id)

@bot.message_handler(func=lambda m: m.text == 'Цвет гласных')
def pick(message):
    markup = types.InlineKeyboardMarkup()
    if get_info(message.chat.id)[3]:
        markup.add(types.InlineKeyboardButton(text='Пусть будут черными', callback_data='b'))
        bot.send_message(chat_id=message.chat.id, text='Сейчас гласные красного цвета', reply_markup=markup)
    else:
        markup.add(types.InlineKeyboardButton(text='Пусть будут красными', callback_data='r'))
        bot.send_message(chat_id=message.chat.id, text='Сейчас гласные черного цвета', reply_markup=markup)

@bot.callback_query_handler(lambda query: query.data == 'b')
def black(query):
    if change_redLetters(query.message.chat.id, False):
        bot.edit_message_text(text='Готово!', chat_id=query.message.chat.id, message_id=query.message.message_id)
    else:
        bot.edit_message_text(text='Что-то не так', chat_id=query.message.chat.id, message_id=query.message.message_id)

@bot.callback_query_handler(lambda query: query.data == 'r')
def red(query):
    if change_redLetters(query.message.chat.id, True):
        bot.edit_message_text(text='Готово!', chat_id=query.message.chat.id, message_id=query.message.message_id)
    else:
        bot.edit_message_text(text='Что-то не так', chat_id=query.message.chat.id, message_id=query.message.message_id)



@bot.message_handler(func=lambda m: True, content_types=['text'])
def create_word(message):
    if message.chat.id not in get_ids():
        bot.send_message(chat_id=message.chat.id, text=oops)
        return
    try:
        try:
            for i in message.text.split():
                photo, new_line = word(i, str(message.chat.id))
                i = i.replace('?', '').replace('*', '')
                photo.save(i + '.png')
                photo = open(i + '.png', 'rb')
                bot.send_document(chat_id=message.chat.id, document=photo, caption=i)
                photo.close()
                os.remove(i + '.png')
        except:
            for i in message.text.split():
                photo, new_line = word(i, str(message.chat.id))
                i.replace('?', '').replace('*', '')
                photo.save(i + '.png')
                photo = open(i + '.png', 'rb')
                bot.send_document(chat_id=message.chat.id, document=photo, caption=i)
                photo.close()
                os.remove(i + '.png')
        #bot.send_message(chat_id=599040955, text=i)
    except Exception as e:
        print(e)
        try:
            for i in message.text.split():
                photo, newline = word(i, str(message.chat.id))
                i.replace('?', '').replace('*', '')
                photo.save(i + '.png')
                photo = open(i + '.png', 'rb')
                bot.send_document(chat_id=message.chat.id, document=photo, caption=i)
                photo.close()
                os.remove(i + '.png')
                #bot.send_message(chat_id=599040955, text=i)
        except:
            bot.send_message(chat_id=message.chat.id, text='Произошла ошибка, проверьте отсутствие недопустимых знаков')
            return

@bot.callback_query_handler(lambda query: query.data == 'Выход')
def exit_func(query):
    global start_menu
    bot.send_message(text='Возвращение в меню...', chat_id=query.message.chat.id, reply_markup=start_menu)
    global exit
    exit = True
    return

@bot.callback_query_handler(lambda query: query.data == 'normal')
def f(query):
    global start_menu
    #try:
    change_wordType(query.message.chat.id, 'normal')
    bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)
    #except:
    #bot.send_message(chat_id=query.message.chat.id, text="Что-то не так с базой данных!", reply_markup=start_menu)

@bot.callback_query_handler(lambda query: query.data == 'w1')
def f(query):
    global start_menu
    try:
        change_wordType(query.message.chat.id, 'ая')
        bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)
    except:
        bot.send_message(chat_id=query.message.chat.id, text="Что-то не так с базой данных!", reply_markup=start_menu)

@bot.callback_query_handler(lambda query: query.data == 'w2')
def f(query):
    global start_menu
    try:
        change_wordType(query.message.chat.id, 'ую')
        bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)
    except:
        bot.send_message(chat_id=query.message.chat.id, text="Что-то не так с базой данных!", reply_markup=start_menu)

@bot.callback_query_handler(lambda query: query.data == 'w3')
def f(query):
    global start_menu
    try:
        change_wordType(query.message.chat.id, 'ыи')
        bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)
    except:
        bot.send_message(chat_id=query.message.chat.id, text="Что-то не так с базой данных!", reply_markup=start_menu)

@bot.callback_query_handler(lambda query: query.data == 'w4')
def f(query):
    global start_menu
    try:
        change_wordType(query.message.chat.id, 'эе')
        bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)
    except:
        bot.send_message(chat_id=query.message.chat.id, text="Что-то не так с базой данных!", reply_markup=start_menu)

@bot.callback_query_handler(lambda query: query.data == 'w5')
def f(query):
    global start_menu
    try:
        change_wordType(query.message.chat.id, 'оё')
        bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)
    except:
        bot.send_message(chat_id=query.message.chat.id, text="Что-то не так с базой данных!", reply_markup=start_menu)


@server.route('/' + '5514371847:AAHyXwFZWL4Ak_EEXFa6CigjYGQFqquaCqI', methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://brackets-tg-bot.herokuapp.com/' + '5514371847:AAHyXwFZWL4Ak_EEXFa6CigjYGQFqquaCqI')
    return "!", 200

if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
