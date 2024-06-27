import cv2
import numpy as np
import re
import warnings

print(".-------------------------------------------------.")
print("|--------- Welcome Ops Tool v3.0 by Altaf --------|")
print("| MAKE SURE THIS PROGRAM IS IN THE SAME FOLDER AS |")
print("|        THE IMAGE YOU WISH TO MAKE WORK ON       |")
print("'-------------------------------------------------'")


name = input("Enter name with extension of image: ")
image = cv2.imread(name)
height, width, _ = image.shape
z = input("Enter the CSV points as x.y,q.r: ")
xz = int(input("Enter the points thickness: "))

z1 = re.sub("[.,]", " ", z)
warnings.filterwarnings("ignore")
pts = np.array([list(map(int, point.split(","))) for point in z1.split()], np.int32)
pts = pts.reshape((-1, 1, 2))
isClosed = True
color = (0, 0, 255)
thickness = xz
cv2.polylines(image, [pts], isClosed, color, thickness)
filename = 'ouput_line_' + name
cv2.imshow("Image", image)
cv2.imwrite(filename, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
