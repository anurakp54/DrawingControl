import cv2
from pdf2image import convert_from_path
import os


def read_qr_code(filename):
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        values, points, straight_qrcode = detect.detectAndDecode(img)
        return values
    except:
        return


# CONVERT PDF FILE TO 'PNG'

# WORKING DIRECTORY

PATH: str = "/Users/mbpro/PycharmProjects/flask/data/"


def qrcode_reader(path):
    files = os.listdir(path)
    file_list = filter(lambda c: c[-3:] == 'pdf', files)  # filter the list where not equal to None
    file_list = (list(file_list))
    filenum = 0

    for file in file_list:
        pages = convert_from_path(path + file, 300)
        for page in pages:
            page.save(path + str(filenum) + '.png', 'PNG')
            filenum += 1

    # Get the list of all files and directories

    dir_list = os.listdir(path)

    qr = []
    for file in dir_list:
        filename = str(PATH + file)
        if filename[-3:] == 'png':
            values = read_qr_code(filename)
            qr.append(values)
            os.remove(filename)

    filelist = zip(dir_list, qr)
    result = list(filelist)
    dwg_list = []
    dwg_with_qr = filter(lambda c: c[1] != '' and c[1] != None, result)  # filter the list where not equal to None

    for dwg in dwg_with_qr:
        dwgnumber = str(dwg[1])
        if dwgnumber != '':
            dwgnumber = dwgnumber[-8:]
            dwg_list.append(dwgnumber)
        else:
            pass

    return dwg_list

if __name__ == "__main__":
    dwglist = qrcode_reader(PATH)
    print(dwglist)