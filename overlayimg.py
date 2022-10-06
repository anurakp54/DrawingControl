from PIL import Image

img1 = Image.open(r"/Users/mbpro/PycharmProjects/flask/data/1.png")
img2 = Image.open(r"/Users/mbpro/PycharmProjects/flask/Static/temp_qr.png")
print(img1.size)
print(img2.size)
H = img1.size[0] - img2.size[0] - 140
img3 = img1
img3.paste(img2, (H,140))
img3.save(r"/Users/mbpro/PycharmProjects/flask/data/dwg.png")