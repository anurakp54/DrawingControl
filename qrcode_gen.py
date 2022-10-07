import qrcode
from PIL import Image, ImageDraw, ImageFont

dwg_num = '122123'
STORAGE = "/Users/mbpro/PycharmProjects/flask/Static/"
URL = 'http://127.0.0.1:5000'
data = URL + '/goodforconstruction/' + dwg_num
img = qrcode.make(data)
img.save(STORAGE + 'qcode.png')
img = Image.open(STORAGE + 'qcode.png')
editable = ImageDraw.Draw(img)
editable.text((10, img.size[1] - 20), dwg_num,size = 7.5, fill='black')
img.save(STORAGE + 'temp_QR.png')


