# coding=utf8
from PIL import Image
import telebot
from telebot import types
import os
from flask import Flask, request
import math
import ast
import json



server = Flask(__name__)
members_dict = {}
text_queue = {}
bot = telebot.TeleBot('5514371847:AAHyXwFZWL4Ak_EEXFa6CigjYGQFqquaCqI')
a = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я', 'ы', 'і', 'ї', 'є']
b = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'й', 'ґ']
s_drop = Image.open('звезда.png')
s_drop = s_drop.resize((62, 97))
b_drop = Image.open('звезда.png')
b_drop = b_drop.resize((126, 195))
boat_1 = Image.open('самолет1.png')
boat_2 = Image.open('самолет2.png')
boat_3 = Image.open('самолет3.png')
boat_4 = Image.open('самолет4.png')

start_menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
b1 = types.KeyboardButton(text='Ввести текст')
b2 = types.KeyboardButton(text="Выбрать вид слов")
b3 = types.KeyboardButton(text="Выбрать другую дугу")
start_menu.add(b1, b2, b3)


def word(word, id):
    global boat_1
    global boat_2
    global boat_3
    global boat_4
    width_total = (len(word) - 1) * 40 + 80
    widths = []
    chars = []
    new_line = False
    
    try:
        with open("preferences.txt", "r") as f:
            s = ast.literal_eval(f.read())[id]['plane']
        if s == '1':
            boat = boat_1
        elif s == '2':
            boat = boat_2
        elif s == '3':
            boat = boat_3
        elif s == '4':
            boat = boat_4
    except:
        boat = boat_1
    
    for char in word:
        try:
            if char == '?':
                img = Image.open('Буквы/q.png')
            elif char == ':':
                img = Image.open('Буквы/colon.png')
            elif char in '“«„"':
                img = Image.open('Буквы/opencommas.png')
            elif char in '”’»“"':
                img = Image.open('Буквы/closecommas.png')
            elif char == '-' or char == '–' or char == '—':
                img = Image.open('Буквы/-.png')
            elif char == 'і' or char == 'i':
                img = Image.open('Буквы/іі.png')
            else:
                img = Image.open('Буквы/' + char.upper() + '.png')
            width, height = img.size
        except:
            pass
        
        if char == char.upper():
            if char == 'Ё':
                img = img.resize((320 * width // height, 320), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Щ' or char == 'Ц':
                img = img.resize((260 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Й':
                img = img.resize((320 * width // height, 320), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == '.':
                img = img.resize((60 * width // height, 60), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == ',':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char in '“«„"”’»“"':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '!':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '?':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '-':
                img = img.resize((150 * width // height, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '–':
                img = img.resize((150 * width // height + 150, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '—':
                img = img.resize((150 * width // height + 200, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ':':
                img = img.resize((220 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ';':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == 'Ґ':
                img = img.resize((295 * width // height, 295), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Ї':
                img = img.resize((330 * width // height, 330), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == '*':
                new_line = True
            elif char == '_':
                width_total += 200
                widths.append(200)
                chars.append(Image.new('RGB', (200, 250), 'white'))
            else:
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
        else:
            if char == 'ё':
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'щ' or char == 'ц':
                img = img.resize((200 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'ї':
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'й':
                img = img.resize((250 * width // height, 250), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'ґ':
                img = img.resize((230 * width // height, 230), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'і' or char == 'i':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            else:
                img = img.resize((200 * width // height, 200), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue

    bg = Image.new('RGB', (width_total, 600), 'white')
    x = 40
    index = 0
    for img in chars:
        if word[index] == 'Ё':
            bg.paste(img, (x, 20))
        elif word[index] == 'ё':
            bg.paste(img, (x, 80))
        elif word[index] == 'Й':
            bg.paste(img, (x, 20))
        elif word[index] == 'й':
            bg.paste(img, (x, 90))
        elif word[index] == '.':
            bg.paste(img, (x, 290))
        elif word[index] == ',':
            bg.paste(img, (x, 310))
        elif word[index] == ',':
            bg.paste(img, (x, 50))
        elif word[index] == '!':
            bg.paste(img, (x, 50))
        elif word[index] == '?':
            bg.paste(img, (x, 50))
        elif word[index] == ':':
            bg.paste(img, (x, 140))
        elif word[index] == ';':
            bg.paste(img, (x, 140))
        elif word[index] == 'Ґ':
            bg.paste(img, (x, 45))
        elif word[index] == 'ґ':
            bg.paste(img, (x, 110))
        elif word[index] == 'Ї':
            bg.paste(img, (x, 10))
        elif word[index] == 'ї':
            bg.paste(img, (x, 80))
        elif word[index] == 'і' or word[index] == 'i':
            bg.paste(img, (x, 60))
        elif word[index] == '-' or word[index] == '–' or word[index] == '—':
            bg.paste(img, (x, 190))
        elif word[index] == word[index].upper():
            bg.paste(img, (x, 80))
        elif word[index] == word[index].lower():
            bg.paste(img, (x, 140))
        x += widths[index] + 40
        index += 1
    drop_y = 380
    boat_y = 340
    
    
    index = 0
    while index < len(word):
        if word[index].lower() in a:
            b_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 63
            bg.paste(b_drop, (b_drop_x, drop_y))
            index += 1
        elif word[index].lower() in b:
            try:
                if word[index + 1].lower() in b:
                    s_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 31
                    bg.paste(s_drop, (s_drop_x, drop_y))
                    index += 1
                elif word[index + 1].lower() in a:
                    boat_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40
                    b_weight, b_height = boat.size
                    boat_place = boat.resize((40 + widths[index] + widths[index+1],
                                          math.ceil(50 * b_height / 100)))
                    bg.paste(boat_place, (boat_x, boat_y), boat_place)
                    index += 2
                else:
                    s_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 31
                    bg.paste(s_drop, (s_drop_x, drop_y))
                    index += 1
            except IndexError:
                s_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 31
                bg.paste(s_drop, (s_drop_x, drop_y))
                index += 1
        else:
            index += 1
    return bg, new_line

def word_only(word, id):
    global boat_1
    global boat_2
    global boat_3
    global boat_4
    width_total = (len(word) - 1) * 40 + 80
    widths = []
    chars = []
    new_line = False
    
    
    for char in word:
        try:
            if char == '?':
                img = Image.open('Буквы/q.png')
            elif char == ':':
                img = Image.open('Буквы/colon.png')
            elif char == '"':
                img = Image.open('Буквы/comas.png')
            elif char == '-' or char == '–' or char == '—':
                img = Image.open('Буквы/-.png')
            elif char == 'і' or char == 'i':
                img = Image.open('Буквы/іі.png')
            else:
                img = Image.open('Буквы/' + char.upper() + '.png')
            width, height = img.size
        except:
            pass
        
        if char == char.upper():
            if char == 'Ё':
                img = img.resize((320 * width // height, 320), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Щ' or char == 'Ц':
                img = img.resize((260 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Й':
                img = img.resize((320 * width // height, 320), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == '.':
                img = img.resize((60 * width // height, 60), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == ',':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '"':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '!':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '?':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '-':
                img = img.resize((150 * width // height, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '–':
                img = img.resize((150 * width // height + 150, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '—':
                img = img.resize((150 * width // height + 200, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ':':
                img = img.resize((220 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ';':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == 'Ґ':
                img = img.resize((295 * width // height, 295), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Ї':
                img = img.resize((330 * width // height, 330), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == '*':
                new_line = True
            elif char == '_':
                width_total += 200
                widths.append(200)
                chars.append(Image.new('RGB', (200, 250), 'white'))
            else:
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
        else:
            if char == 'ё':
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'щ' or char == 'ц':
                img = img.resize((200 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'ї':
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'й':
                img = img.resize((250 * width // height, 250), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'ґ':
                img = img.resize((230 * width // height, 230), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'і' or char == 'i':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            else:
                img = img.resize((200 * width // height, 200), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue

    bg = Image.new('RGB', (width_total, 600), 'white')
    x = 40
    index = 0
    for img in chars:
        if word[index] == 'Ё':
            bg.paste(img, (x, 20))
        elif word[index] == 'ё':
            bg.paste(img, (x, 80))
        elif word[index] == 'Й':
            bg.paste(img, (x, 20))
        elif word[index] == 'й':
            bg.paste(img, (x, 90))
        elif word[index] == '.':
            bg.paste(img, (x, 290))
        elif word[index] == ',':
            bg.paste(img, (x, 310))
        elif word[index] == ',':
            bg.paste(img, (x, 50))
        elif word[index] == '!':
            bg.paste(img, (x, 50))
        elif word[index] == '?':
            bg.paste(img, (x, 50))
        elif word[index] == ':':
            bg.paste(img, (x, 140))
        elif word[index] == ';':
            bg.paste(img, (x, 140))
        elif word[index] == 'Ґ':
            bg.paste(img, (x, 45))
        elif word[index] == 'ґ':
            bg.paste(img, (x, 110))
        elif word[index] == 'Ї':
            bg.paste(img, (x, 10))
        elif word[index] == 'ї':
            bg.paste(img, (x, 80))
        elif word[index] == 'і' or word[index] == 'i':
            bg.paste(img, (x, 60))
        elif word[index] == '-' or word[index] == '–' or word[index] == '—':
            bg.paste(img, (x, 190))
        elif word[index] == word[index].upper():
            bg.paste(img, (x, 80))
        elif word[index] == word[index].lower():
            bg.paste(img, (x, 140))
        x += widths[index] + 40
        index += 1
    drop_y = 380
    boat_y = 340
    return bg, new_line

def word_with_drops(word, id):
    global boat_1
    global boat_2
    global boat_3
    global boat_4
    width_total = (len(word) - 1) * 40 + 80
    widths = []
    chars = []
    new_line = False
    
    
    for char in word:
        try:
            if char == '?':
                img = Image.open('Буквы/q.png')
            elif char == ':':
                img = Image.open('Буквы/colon.png')
            elif char == '"':
                img = Image.open('Буквы/comas.png')
            elif char == '-' or char == '–' or char == '—':
                img = Image.open('Буквы/-.png')
            elif char == 'і' or char == 'i':
                img = Image.open('Буквы/іі.png')
            else:
                img = Image.open('Буквы/' + char.upper() + '.png')
            width, height = img.size
        except:
            pass
        
        if char == char.upper():
            if char == 'Ё':
                img = img.resize((320 * width // height, 320), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Щ' or char == 'Ц':
                img = img.resize((260 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Й':
                img = img.resize((320 * width // height, 320), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == '.':
                img = img.resize((60 * width // height, 60), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == ',':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '"':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '!':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '?':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '-':
                img = img.resize((150 * width // height, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '–':
                img = img.resize((150 * width // height + 150, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '—':
                img = img.resize((150 * width // height + 200, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ':':
                img = img.resize((220 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ';':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == 'Ґ':
                img = img.resize((295 * width // height, 295), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Ї':
                img = img.resize((330 * width // height, 330), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == '*':
                new_line = True
            elif char == '_':
                width_total += 200
                widths.append(200)
                chars.append(Image.new('RGB', (200, 250), 'white'))
            else:
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
        else:
            if char == 'ё':
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'щ' or char == 'ц':
                img = img.resize((200 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'ї':
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'й':
                img = img.resize((250 * width // height, 250), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'ґ':
                img = img.resize((230 * width // height, 230), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'і' or char == 'i':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            else:
                img = img.resize((200 * width // height, 200), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue

    bg = Image.new('RGB', (width_total, 600), 'white')
    x = 40
    index = 0
    for img in chars:
        if word[index] == 'Ё':
            bg.paste(img, (x, 20))
        elif word[index] == 'ё':
            bg.paste(img, (x, 80))
        elif word[index] == 'Й':
            bg.paste(img, (x, 20))
        elif word[index] == 'й':
            bg.paste(img, (x, 90))
        elif word[index] == '.':
            bg.paste(img, (x, 290))
        elif word[index] == ',':
            bg.paste(img, (x, 310))
        elif word[index] == ',':
            bg.paste(img, (x, 50))
        elif word[index] == '!':
            bg.paste(img, (x, 50))
        elif word[index] == '?':
            bg.paste(img, (x, 50))
        elif word[index] == ':':
            bg.paste(img, (x, 140))
        elif word[index] == ';':
            bg.paste(img, (x, 140))
        elif word[index] == 'Ґ':
            bg.paste(img, (x, 45))
        elif word[index] == 'ґ':
            bg.paste(img, (x, 110))
        elif word[index] == 'Ї':
            bg.paste(img, (x, 10))
        elif word[index] == 'ї':
            bg.paste(img, (x, 80))
        elif word[index] == 'і' or word[index] == 'i':
            bg.paste(img, (x, 60))
        elif word[index] == '-' or word[index] == '–' or word[index] == '—':
            bg.paste(img, (x, 190))
        elif word[index] == word[index].upper():
            bg.paste(img, (x, 80))
        elif word[index] == word[index].lower():
            bg.paste(img, (x, 140))
        x += widths[index] + 40
        index += 1
    drop_y = 380
    boat_y = 340
    
    
    index = 0
    while index < len(word):
        if word[index].lower() in a:
            b_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 63
            bg.paste(b_drop, (b_drop_x, drop_y))
            index += 1
        elif word[index].lower() in b:
            try:
                if word[index + 1].lower() in b:
                    s_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 31
                    bg.paste(s_drop, (s_drop_x, drop_y))
                    index += 1
                elif word[index + 1].lower() in a:
                    index += 2
                else:
                    s_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 31
                    bg.paste(s_drop, (s_drop_x, drop_y))
                    index += 1
            except IndexError:
                s_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 31
                bg.paste(s_drop, (s_drop_x, drop_y))
                index += 1
        else:
            index += 1
    return bg, new_line

def word_with_boats(word, id):
    global boat_1
    global boat_2
    global boat_3
    global boat_4
    width_total = (len(word) - 1) * 40 + 80
    widths = []
    chars = []
    new_line = False
    
    with open("preferences.txt", "r") as f:
        data = ast.literal_eval(f.read())
    try:
        s = data[id]['plane']
        if s == '1':
            boat = boat_1
        elif s == '2':
            boat = boat_2
        elif s == '3':
            boat = boat_3
        elif s == '4':
            boat = boat_4
    except:
        boat = boat_1
    
    for char in word:
        try:
            if char == '?':
                img = Image.open('Буквы/q.png')
            elif char == ':':
                img = Image.open('Буквы/colon.png')
            elif char == '"':
                img = Image.open('Буквы/comas.png')
            elif char == '-' or char == '–' or char == '—':
                img = Image.open('Буквы/-.png')
            elif char == 'і' or char == 'i':
                img = Image.open('Буквы/іі.png')
            else:
                img = Image.open('Буквы/' + char.upper() + '.png')
            width, height = img.size
        except:
            pass
        
        if char == char.upper():
            if char == 'Ё':
                img = img.resize((320 * width // height, 320), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Щ' or char == 'Ц':
                img = img.resize((260 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Й':
                img = img.resize((320 * width // height, 320), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == '.':
                img = img.resize((60 * width // height, 60), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == ',':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '"':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '!':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '?':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '-':
                img = img.resize((150 * width // height, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '–':
                img = img.resize((150 * width // height + 150, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '—':
                img = img.resize((150 * width // height + 200, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ':':
                img = img.resize((220 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ';':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == 'Ґ':
                img = img.resize((295 * width // height, 295), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Ї':
                img = img.resize((330 * width // height, 330), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == '*':
                new_line = True
            elif char == '_':
                width_total += 200
                widths.append(200)
                chars.append(Image.new('RGB', (200, 250), 'white'))
            else:
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
        else:
            if char == 'ё':
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'щ' or char == 'ц':
                img = img.resize((200 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'ї':
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'й':
                img = img.resize((250 * width // height, 250), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'ґ':
                img = img.resize((230 * width // height, 230), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'і' or char == 'i':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            else:
                img = img.resize((200 * width // height, 200), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue

    bg = Image.new('RGB', (width_total, 600), 'white')
    x = 40
    index = 0
    for img in chars:
        if word[index] == 'Ё':
            bg.paste(img, (x, 20))
        elif word[index] == 'ё':
            bg.paste(img, (x, 80))
        elif word[index] == 'Й':
            bg.paste(img, (x, 20))
        elif word[index] == 'й':
            bg.paste(img, (x, 90))
        elif word[index] == '.':
            bg.paste(img, (x, 290))
        elif word[index] == ',':
            bg.paste(img, (x, 310))
        elif word[index] == ',':
            bg.paste(img, (x, 50))
        elif word[index] == '!':
            bg.paste(img, (x, 50))
        elif word[index] == '?':
            bg.paste(img, (x, 50))
        elif word[index] == ':':
            bg.paste(img, (x, 140))
        elif word[index] == ';':
            bg.paste(img, (x, 140))
        elif word[index] == 'Ґ':
            bg.paste(img, (x, 45))
        elif word[index] == 'ґ':
            bg.paste(img, (x, 110))
        elif word[index] == 'Ї':
            bg.paste(img, (x, 10))
        elif word[index] == 'ї':
            bg.paste(img, (x, 80))
        elif word[index] == 'і' or word[index] == 'i':
            bg.paste(img, (x, 60))
        elif word[index] == '-' or word[index] == '–' or word[index] == '—':
            bg.paste(img, (x, 190))
        elif word[index] == word[index].upper():
            bg.paste(img, (x, 80))
        elif word[index] == word[index].lower():
            bg.paste(img, (x, 140))
        x += widths[index] + 40
        index += 1
    drop_y = 380
    boat_y = 340
    
    
    index = 0
    while index < len(word):
        if word[index].lower() in a:
            index += 1
        elif word[index].lower() in b:
            try:
                if word[index + 1].lower() in b:
                    index += 1
                elif word[index + 1].lower() in a:
                    boat_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40
                    b_weight, b_height = boat.size
                    boat_place = boat.resize((40 + widths[index] + widths[index+1],
                                          math.ceil(50 * b_height / 100)))
                    bg.paste(boat_place, (boat_x, boat_y), boat_place)
                    index += 2
                else:
                    index += 1
            except IndexError:
                index += 1
        else:
            index += 1
    return bg, new_line


def g_text(text1, size, orientation, id):
    if orientation == 'альбомная':
        width, height = 3508, 2480
    elif orientation == 'книжная':
        width, height = 2480, 3508

    bg = Image.new('RGB', (width, height), 'white')

    x, y = 100, 100
    text_list = list(text1.replace('\n', '* ').split())
    img_height = 0
    x_max = 0
    while y + img_height + 0.1 * size <= height:
        try:
            w = text_list[0]
        except:
            break
        
        try:
            with open('preferences.txt', 'r') as f:
                w_type = ast.literal_eval(f.read())[str(id)]['word']
            
            if w_type == '1':
                img, new_line = word(w, str(id))
            elif w_type == '2':
                img, new_line = word_with_boats(w, str(id))
            elif w_type == '3':
                img, new_line = word_with_drops(w, str(id))
            elif w_type == '4':
                img, new_line = word_only(w, str(id))
        except:
            img, new_line = word(w, id)
        
        img_width, img_height = img.size
        img = img.resize((math.ceil(80 * img_width // img_height * (size / 10)), math.ceil(80 * (size / 10))), Image.ANTIALIAS)
        img_width, img_height = img.size
        if x + img_width + 100 <= width:
            bg.paste(img, (math.ceil(x), math.ceil(y)))
            if x + img_width + 100 > x_max:
                x_max = x + img_width
            x += img_width + 2 * size

        else:
            if x > x_max:
                x_max = x
            y += img_height + 0.1 * size
            x = 100
            bg.paste(img, (math.ceil(x), math.ceil(y)))
            x += img_width + 2 * size
        
        if new_line:
            if x > x_max:
                x_max = x
            y += img_height + 0.1 * size
            x = 100
        
        try:
            del text_list[0]
        except:
            break
    if x_max > width:
        x_max = width
    if y + 50 + img_height > height:
        y = height
    else:
        y = y + 50 + img_height
    bg = bg.crop((0, 0, x_max + 100, y))
    if len(text_list) != 0:
        text1 = ' '.join(text_list)
        return bg, text1
    return bg, ''

@bot.message_handler(commands=['start'])
def answer(message):
    global start_menu
    bot.send_message(chat_id=message.chat.id, text='Отправьте слово или несколько слов через пробел.\nВоспользуйтесь кнопками ниже, для ввода текста или изменения вида дуг', reply_markup=start_menu)


@bot.message_handler(commands=['text'])
def is_available(message):
    ask_text(message)
    
def ask_text(message):
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
        photo.save(text[:6] + '.png')
        photo = open(text[:6] + '.png', 'rb')
        bot.send_document(chat_id=message.chat.id, data=photo, caption=text[:10] + '...')
        while text2 != '':
            photo, text2 = g_text(text2, size, orientation, mode)
            print(text2)
            photo.save(text[:6] + '.png')
            photo = open(text[:6] + '.png', 'rb')
            bot.send_document(chat_id=message.chat.id, data=photo, caption='Продолжение')
        bot.edit_message_text(text='Готово!', chat_id=message.chat.id, message_id=msg.id)
        bot.send_message(text='Возврат в меню...', chat_id=message.chat.id, reply_markup=start_menu)
    except:
        bot.delete_message(chat_id=message.chat.id, message_id=msg.id)
        bot.send_message(chat_id=message.chat.id, text='Произошла ошибка, попробуйте еще раз. В тексте допускаются знаки:\n!\n,\n?\n""\n_\n-\n.\n;\n:\n Заглавные и строчные буквы русского алфавита')
        bot.send_message(text='Возврат в меню...', chat_id=message.chat.id, reply_markup=start_menu)
    #bot.send_message(chat_id=599040955, text=str(text_queue))
    photo.close()
    os.remove(text[:6] + '.png')
    del text_queue[str(message.chat.id)]

@bot.message_handler(func=lambda m: m.text == 'Ввести текст')
def generate_text(message):
    is_available(message)

@bot.message_handler(func=lambda m: m.text == 'Выбрать другую дугу')
def answer(message):
    bot.send_message(chat_id=message.chat.id, text="Выберите один из вариантов:")
    
    markup1 = types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton(text='✅', callback_data='1'))
    img = Image.open("самолет1.png")
    bg = Image.new("RGBA", img.size, "white")
    bg.paste(img, img)
    bot.send_photo(chat_id=message.chat.id, photo=bg, reply_markup=markup1)
    
    markup2 = types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton(text='✅', callback_data='2'))
    img = Image.open("самолет2.png")
    bg = Image.new("RGBA", img.size, "white")
    bg.paste(img, img)
    bot.send_photo(chat_id=message.chat.id, photo=bg, reply_markup=markup2)
    
    markup3 = types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton(text='✅', callback_data='3'))
    img = Image.open("самолет3.png")
    bg = Image.new("RGBA", img.size, "white")
    bg.paste(img, img)
    bot.send_photo(chat_id=message.chat.id, photo=bg, reply_markup=markup3)
    
    markup4 = types.InlineKeyboardMarkup(row_width=1).add(types.InlineKeyboardButton(text='✅', callback_data='4'))
    img = Image.open("самолет4.png")
    bg = Image.new("RGBA", img.size, "white")
    bg.paste(img, img)
    bot.send_photo(chat_id=message.chat.id, photo=bg, reply_markup=markup4)
    
@bot.message_handler(func=lambda m: m.text == 'Выбрать вид слов')
def ans(message):
    k = types.InlineKeyboardMarkup(row_width=1)
    k.add(types.InlineKeyboardButton(text='Дуги и точки', callback_data='w1'))
    k.add(types.InlineKeyboardButton(text='Только дуги', callback_data='w2'))
    k.add(types.InlineKeyboardButton(text='Только точки', callback_data='w3'))
    k.add(types.InlineKeyboardButton(text='Только текст', callback_data='w4'))
    bot.send_message(chat_id=message.chat.id, text='Выбирайте', reply_markup=k)

@bot.message_handler(func=lambda m: True, content_types=['text'])
def create_word(message):
    try:
        with open('preferences.txt', 'r') as f:
            w_type = ast.literal_eval(f.read())[str(message.chat.id)]['word']
        for i in message.text.split():
            if w_type == '1':
                photo, new_line = word(i, str(message.chat.id))
            elif w_type == '2':
                photo, new_line = word_with_boats(i, str(message.chat.id))
            elif w_type == '3':
                photo, new_line = word_with_drops(i, str(message.chat.id))
            elif w_type == '4':
                photo, new_line = word_only(i, str(message.chat.id))
            else:
                photo, new_line = word(i, str(message.chat.id))
            if not '?' in i:
                pass
            else:
                i = 'pic'
            photo.save(i + '.png')
            photo = open(i + '.png', 'rb')
            bot.send_document(chat_id=message.chat.id, data=photo, caption=i)
            photo.close()
            os.remove(i + '.png')
            #bot.send_message(chat_id=599040955, text=i)
    except:
        try:
            for i in message.text.split():
                photo, newline = word(i, str(message.chat.id))
                if not '?' in i:
                    pass
                else:
                    i = 'poop'
                photo.save(i + '.png')
                photo = open(i + '.png', 'rb')
                bot.send_document(chat_id=message.chat.id, data=photo, caption=i)
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


@bot.callback_query_handler(lambda query: query.data == '1')
def f(query):
    global start_menu
    with open("preferences.txt", "r") as f:
        data = ast.literal_eval(f.read())
    try:
        data[str(query.message.chat.id)]['plane'] = '1'
    except:
        try:
            w = data[str(query.message.chat.id)]['word']
            data[str(query.message.chat.id)] = {'word': w, 'plane': '1'}
        except:
            data[str(query.message.chat.id)] = {'word': '1', 'plane': '1'}
    with open("preferences.txt", "w") as f:
        f.write(str(data))
    bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)
    

@bot.callback_query_handler(lambda query: query.data == '2')
def f(query):
    global start_menu
    with open("preferences.txt", "r") as f:
        data = ast.literal_eval(f.read())
    try:
        data[str(query.message.chat.id)]['plane'] = '2'
    except:
        try:
            w = data[str(query.message.chat.id)]['word']
            data[str(query.message.chat.id)] = {'word': w, 'plane': '2'}
        except:
            data[str(query.message.chat.id)] = {'word': '1', 'plane': '2'}
    with open("preferences.txt", "w") as f:
        f.write(str(data))
    bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)

@bot.callback_query_handler(lambda query: query.data == '3')
def f(query):
    global start_menu
    with open("preferences.txt", "r") as f:
        data = ast.literal_eval(f.read())
    try:
        data[str(query.message.chat.id)]['plane'] = '3'
    except:
        try:
            w = data[str(query.message.chat.id)]['word']
            data[str(query.message.chat.id)] = {'word': w, 'plane': '3'}
        except:
            data[str(query.message.chat.id)] = {'word': '1', 'plane': '3'}
    with open("preferences.txt", "w") as f:
        f.write(str(data))
    bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)

@bot.callback_query_handler(lambda query: query.data == '4')
def f(query):
    global start_menu
    with open("preferences.txt", "r") as f:
        data = ast.literal_eval(f.read())
    try:
        data[str(query.message.chat.id)]['plane'] = '4'
    except:
        try:
            w = data[str(query.message.chat.id)]['word']
            data[str(query.message.chat.id)] = {'word': w, 'plane': '4'}
        except:
            data[str(query.message.chat.id)] = {'word': '1', 'plane': '4'}
    with open("preferences.txt", "w") as f:
        f.write(str(data))
    bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)

@bot.callback_query_handler(lambda query: query.data == 'w1')
def f(query):
    global start_menu
    with open("preferences.txt", "r") as f:
        data = ast.literal_eval(f.read())
    try:
        data[str(query.message.chat.id)]['word'] = '1'
    except:
        try:
            p = data[str(query.message.chat.id)]['plane']
            data[str(query.message.chat.id)] = {'word': '1', 'plane': p}
        except:
            data[str(query.message.chat.id)] = {'word': '1', 'plane': '1'}
    with open("preferences.txt", "w") as f:
        f.write(str(data))
    bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)

@bot.callback_query_handler(lambda query: query.data == 'w2')
def f(query):
    global start_menu
    with open("preferences.txt", "r") as f:
        data = ast.literal_eval(f.read())
    try:
        data[str(query.message.chat.id)]['word'] = '2'
    except:
        try:
            p = data[str(query.message.chat.id)]['plane']
            data[str(query.message.chat.id)] = {'word': '2', 'plane': p}
        except:
            data[str(query.message.chat.id)] = {'word': '2', 'plane': '1'}
    with open("preferences.txt", "w") as f:
        f.write(str(data))
    bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)

@bot.callback_query_handler(lambda query: query.data == 'w3')
def f(query):
    global start_menu
    with open("preferences.txt", "r") as f:
        data = ast.literal_eval(f.read())
    try:
        data[str(query.message.chat.id)]['word'] = '3'
    except:
        try:
            p = data[str(query.message.chat.id)]['plane']
            data[str(query.message.chat.id)] = {'word': '3', 'plane': p}
        except:
            data[str(query.message.chat.id)] = {'word': '3', 'plane': '1'}
    with open("preferences.txt", "w") as f:
        f.write(str(data))
    bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)

@bot.callback_query_handler(lambda query: query.data == 'w4')
def f(query):
    global start_menu
    with open("preferences.txt", "r") as f:
        data = ast.literal_eval(f.read())
    try:
        data[str(query.message.chat.id)]['word'] = '4'
    except:
        try:
            p = data[str(query.message.chat.id)]['plane']
            data[str(query.message.chat.id)] = {'word': '4', 'plane': p}
        except:
            data[str(query.message.chat.id)] = {'word': '4', 'plane': '1'}
    with open("preferences.txt", "w") as f:
        f.write(str(data))
    bot.send_message(chat_id=query.message.chat.id, text="Готово!", reply_markup=start_menu)


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
