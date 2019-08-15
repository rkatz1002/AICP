import barcode
from docx import Document
from barcode.writer import ImageWriter
from docx.shared import Inches

document = Document()

def barcodef(num):
    l = len(num)
    num = num.zfill(13)

    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(num, writer=ImageWriter())
    # Now we look if the checksum was added
    ean.save(num)


    document.add_picture(num + '.png', width=Inches(1.0))
    document.save('file' + '.docx')

num = input()
barcodef(num)