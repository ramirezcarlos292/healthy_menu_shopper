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

test_file = os.path.join(path, filtered_list[1])
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



import cv2 as cv
import matplotlib.pyplot as plt
plt.figure(figsize=(40, 30))
path_img = './images/page1.jpg'
img = cv.imread(path_img)
gray = cv.cvtColor(img, cv.COLOR_BGR

plt.imshow(gray)
plt.show()