from wand.image import Image as wi
import os
import io
import pytesseract
from PIL import Image
from pytesseract import image_to_string

filenames = ['May_2019_ADP_meeting.pdf']

pdf = wi(filename=filenames[0],resolution=800)

image = pdf.convert('jpeg')
i= 1
image_blobs =[]
for img in image.sequence:
    directory = './'+filenames[0][:-4]+'/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    page = wi(image=img)
    # image_blobs.append(page.make_blob('jpeg'))
    # page.save(filename=directory+filenames[0][:-4]+str(i)+".jpg")

    im = Image.open(io.BytesIO(page.make_blob('jpeg')))
    text = pytesseract.image_to_string(im, lang='ben')
    f = open(directory + filenames[0][:-4]+str(i) + ".txt", "w+")
    f.write(text)
    i += 1

f.close()