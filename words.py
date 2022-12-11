from PIL import Image
import math
from admin import get_info


a = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я', 'ы', 'і', 'ї', 'є']
b = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'й', 'ґ']
s_drop = Image.open('звезда.png')
s_drop = s_drop.resize((62, 62))
b_drop = Image.open('звезда.png')
b_drop = b_drop.resize((126, 126))
boat_1 = Image.open('самолет1.png').convert("RGBA")

def word(word, id):
    global boat_1
    boat = boat_1
    width_total = (len(word) - 1) * 40 + 80
    widths = []
    chars = []
    new_line = False
    info = get_info(id)
    excluded = info[2]
    red = info[3]
    if info[4]:
        word = word.upper()
        boat_y = 580
        drop_y = 580
        accent_y = 160
        boat_height = 220
        blank = 250
    else:
        boat_y = 610
        drop_y = 620
        accent_y = 230
        boat_height = 200
        blank = 200
        
    
    for char in word:
        try:
            if char.lower() in excluded:
                img = Image.open('Буквы/blank.png')
                width, height = img.size
                img = img.resize((blank, 120), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == '?':
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
            elif char == '*':
                img = Image.open("Буквы/'.png")
            else:
                if char == char.upper():
                    img = Image.open('Буквы/' + char + '.png')
                else:
                    img = Image.open('Буквы/' + char * 2 + '.png')
            width, height = img.size
        except:
            pass
        
        if not red and char.lower() in a:
            img = img.convert('1', dither=Image.NONE)
            s = Image.new('RGB', (img.size), 'white')
            s.paste(img, (0, 0))
            img = s
        
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
            elif char == "*":
                img = img.resize((80 * width // height, 80), Image.ANTIALIAS)
                width, height = img.size
                chars.append(img)
                widths.append(0)
            elif char in '“«„"”»“"':
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
            elif char == '/':
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
                img = img.resize((270 * width // height, 270), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'щ' or char == 'ц':
                img = img.resize((235 * width // height, 235), Image.ANTIALIAS)
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
            elif char == 'д':
                img = img.resize((230 * width // height, 230), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'б':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'й':
                img = img.resize((285 * width // height, 285), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'р':
                img = img.resize((270 * width // height, 270), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'у':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'ф':
                img = img.resize((330 * width // height, 330), Image.ANTIALIAS)
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
    
    bg = Image.new('RGB', (width_total, 800), 'white')
    x = 40
    index = 0
    for img in chars:
        if word[index] in excluded or word[index].lower() in excluded:
            bg.paste(img, (x, 490))
        elif word[index] == 'Ё':
            bg.paste(img, (x, 220))
        elif word[index] == 'ё':
            bg.paste(img, (x, 265))
        elif word[index] == 'б':
            bg.paste(img, (x, 265))
        elif word[index] == 'Й':
            bg.paste(img, (x, 220))
        elif word[index] == 'й':
            bg.paste(img, (x, 255))
        elif word[index] == 'ф':
            bg.paste(img, (x, 275))
        elif word[index] == '.':
            bg.paste(img, (x, 490))
        elif word[index] == "*":
            bg.paste(img, (x - widths[index-1] // 2 - 74, accent_y))
        elif word[index] == ',':
            bg.paste(img, (x, 510))
        elif word[index] == ',':
            bg.paste(img, (x, 250))
        elif word[index] == '!':
            bg.paste(img, (x, 250))
        elif word[index] == '?':
            bg.paste(img, (x, 250))
        elif word[index] == ':':
            bg.paste(img, (x, 340))
        elif word[index] == ';':
            bg.paste(img, (x, 340))
        elif word[index] == 'Ґ':
            bg.paste(img, (x, 245))
        elif word[index] == 'ґ':
            bg.paste(img, (x, 310))
        elif word[index] == 'Ї':
            bg.paste(img, (x, 210))
        elif word[index] == 'ї':
            bg.paste(img, (x, 280))
        elif word[index] == 'і' or word[index] == 'i':
            bg.paste(img, (x, 260))
        elif word[index] == '-' or word[index] == '–' or word[index] == '—':
            bg.paste(img, (x, 390))
        elif word[index] == word[index].upper():
            bg.paste(img, (x, 280))
        elif word[index] == word[index].lower():
            bg.paste(img, (x, 340))
        x += widths[index] + 40
        accent_y = 440 - img.size[1]
        index += 1
    

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
                    boat_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + 20
                    b_width, b_height = boat.size
                    boat_place = boat.resize((40 + widths[index] + widths[index+1] - 40, boat_height))
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


def g_text(text1, size, orientation, id):
    if orientation == 'альбомная':
        width, height = 3508, 2480
    elif orientation == 'книжная':
        width, height = 2480, 3508

    bg = Image.new('RGB', (width, height), 'white')

    x, y = 100, 100
    text_list = list(text1.replace('\n', '/ ').split())
    img_height = 0
    x_max = 0
    while y + img_height + 0.1 * size <= height:
        try:
            w = text_list[0]
        except:
            break
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
