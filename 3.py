from PIL import Image, ImageDraw, ImageFont
import random

seed = "qwertyuiopasdfghjklzxcvbnm"

#to remove the skin from emotes with skin color
def remove_skin(text):
    return text.replace("🏻", "").replace("🏼", "").replace("🏽", "").replace("🏾", "").replace("🏿", "")

with open("output.txt", "r", encoding="utf-8") as f:
    text1 = f.read().split('\n')

for text in text1:
    i = random.choice(seed)
    j = random.choice(seed)
    k = random.choice(seed)
    if not text:
        continue

    img = Image.open('bg.jpg')
    W, H = img.size
    dr = ImageDraw.Draw(img)
    font_size = 35
    ft = ImageFont.truetype('seguiemj.ttf', font_size) #seguiemj only font which supports emotes😭

    text_without_skin = remove_skin(text)

    words = text_without_skin.split()
    wrapped_lines = []
    current_line = words[0]
    
    for word in words[1:]:
        test_line = current_line + ' ' + word
        if len(test_line) <= 50:
            current_line = test_line
        else:
            wrapped_lines.append(current_line)
            current_line = word
    
    wrapped_lines.append(current_line)

    y = (H - len(wrapped_lines) * font_size) / 2

    for line in wrapped_lines:
        x = (W - dr.textbbox((0, 0), line, font=ft)[2]) / 2

        # Border
        outline_color = (0, 0, 0) #(134, 74, 245)
        outline_width = 1.5  # Width
        dr.text((x - outline_width, y), line, font=ft, fill=outline_color)
        dr.text((x + outline_width, y), line, font=ft, fill=outline_color)
        dr.text((x, y - outline_width), line, font=ft, fill=outline_color)
        dr.text((x, y + outline_width), line, font=ft, fill=outline_color)

        # Main text
        dr.text((x, y), line, font=ft, fill=(255, 255, 255))
        y += dr.textbbox((0, 0), line, font=ft)[3] - dr.textbbox((0, 0), line, font=ft)[1]

    img.save('Confessions\\conf ' + i + j + k + '.jpg')
