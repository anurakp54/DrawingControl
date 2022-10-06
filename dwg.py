from pdf2image import convert_from_path
import os

path = "/Users/mbpro/PycharmProjects/flask/data/"
files = os.listdir(path)
file_list = filter(lambda c: c[-3:] == 'pdf', files)  # filter the list where not equal to None
file_list = (list(file_list))
filenum = 0

for file in file_list:
    pages = convert_from_path(path+file, 300)
    for page in pages:
        page.save(path+str(filenum)+'.png','PNG')
        filenum += 1
