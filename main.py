import cv2

filePath = 'kler.jpg'

image = cv2.imread(filePath,1)

cv2.imshow("GANDA KO BHIE!!",image)

cv2.waitKey(0)

cv2.destroyAllWindows()
