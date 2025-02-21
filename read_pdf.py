import os

def filter(list_files, extension):
    filtered_list = []
    for file in list_files:
        if file[-3:] == extension:
            filtered_list.append(file)
    return filtered_list    

path = './healthy_menus'
list_files = os.listdir(path)

filtered_list = filter(list_files, 'pdf')

test_file = os.path.join(path, filtered_list[0])
if os.path.exists(test_file):
    pass
else:
    print('file does not exist')

## Using Tabula - https://datascientyst.com/extract-table-from-pdf-with-python-pandas/
# from tabula import read_pdf
# if os.path.exists(test_file):
#     tables = read_pdf(test_file, pages = 'all')
#     tables
# else:
#     print('file does not exist')


from pdf2image import convert_from_path
images = convert_from_path(test_file)
for i in range(len(images)):
    images[i].save('./images/page'+ str(i) +'.jpg', 'JPEG')


# https://analyticsindiamag.com/deep-tech/how-to-use-opencv-to-extract-information-from-table-images/
import cv2 as cv
import matplotlib.pyplot as plt
plt.figure(figsize=(20, 10))
path_img = './images/page1.jpg'
img = cv.imread(path_img, 0)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

(thresh, im_bw) = cv.threshold(img, 20, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

plt.imshow(im_bw)
plt.show()