#first, we input all libraries that we need:
import PIL
from PIL import Image
from PIL import ImageEnhance
from IPython.display import display

#read image:
image = Image.open(r'E:\GitHub\Pillow_Tesseract_OpenCV_coursera-1\images\msi_recruitment.gif').convert('RGB')
#make a black image from main image:
blank = ImageEnhance.Brightness(image)
blank = blank.enhance(0)
# make the combined image:
contact_sheet = Image.new(blank.mode, (blank.width*3, blank.height*3))

#x,y are pos of where the next image must be start from:
x = 0
y = 0

# we append all created image to a images list:
images = []
#split channels(R,G,B)
r, g, b = image.split()

#ints are intensity values that we put them in a list:
ints = [0.1, 0.5, 0.9]

#in below loops, we make images:
for i in ints:
    r = r.point(lambda p: p*i)
    result = Image.merge('RGB', (r,g,b))
    r, g, b = image.split()
    images.append(result)
    
for i in ints:
    g = g.point(lambda p: p*i)
    result = Image.merge('RGB', (r,g,b))
    r, g, b = image.split()
    images.append(result)
    
for i in ints:
    b = b.point(lambda p: p*i)
    result = Image.merge('RGB', (r,g,b))
    r, g, b = image.split()
    images.append(result)
    
for img in images:
    contact_sheet.paste(img, (x,y))
    x += blank.width
    if x == 3*blank.width:
        y += blank.height
        x = 0
resized = contact_sheet.resize((int(blank.width*3/2), int(blank.height*3/2)))
display(resized)
resized.show('channel changed')
resized.save('OutPut.png')