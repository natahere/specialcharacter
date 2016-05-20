import os.path
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

count_lines = 0 #for loop to read font file
W, H = (300,200) #set the h,w of image file


with open('font.txt') as f1: #read the font.txt and get all fonts list 
	fonts = f1.read().splitlines()
for line in fonts: #for each font
			print(line)
			font = ImageFont.truetype(line,150) #set the size of font
			char_count = 0
			current_h, pad = 150, 10 #current height and padding

			with open('char.txt') as f: #read all the chars
				content = f.read().splitlines()
			for p in content:
				img = Image.new("RGBA",(W,H),(255,255,255)) #
				draw = ImageDraw.Draw(img)
				w, h = draw.textsize(p, font=font)
				draw.text(((W-w)/2,(H-h)/2), p, (0,0,0),font=font)
				draw = ImageDraw.Draw(img)
				img.save("C:/Users/Natarajan/spimages/" + "spl" + str(ord(p)) + "-"+ str(char_count) + line + ".png")
				char_count += 1
				
			count_lines += 1
