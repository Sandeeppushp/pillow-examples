from PIL import Image, ImageDraw, ImageFont,ImageEnhance, ImageFilter,ImageOps
import PIL

img = PIL.Image.open('image.jpg')

image_file = img.convert('1') 
image_file.save('blacknWhite.png')

converter = PIL.ImageEnhance.Brightness(img).enhance(4.5)
converter.save('brightness.jpg')

converter = PIL.ImageEnhance.Color(img).enhance(4.5)
converter.save('color.jpg')

blur = img.filter(ImageFilter.GaussianBlur(radius = 10)) 
blur.save('blur.jpg') 


converter = PIL.ImageEnhance.Contrast(img).enhance(4.5)
converter.save('Contrast.jpg')


im = ImageOps.posterize(img, 3)  
im.save('posterize.jpg')


inverted_image = PIL.ImageOps.invert(img)
inverted_image.save('invert.png')


crop = img.crop((0, 0, 2500, 2500))
crop.save('crop.jpg')


rotate = img.rotate(180)
rotate.save('rotate.jpg')


im_mirror = ImageOps.mirror(img)
im_mirror.save('mirror.jpg')


height,width = img.size
image_data = img.load()
for loop1 in range(height):
    for loop2 in range(width):
        r,g,b = image_data[loop1,loop2]
        image_data[loop1,loop2] = 0,g,0
img.save('changecolor.jpeg')


draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((50, 50), 'hello world',fill = 'rgb(0, 0, 0)', font=font)


img.save("compress.jpg",optimize=True,quality=10)
