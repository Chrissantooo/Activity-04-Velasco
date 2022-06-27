import cv2

print("Printing disguted yet horny meme...")

filePath = 'disgust.jpg'
img = cv2.imread(filePath, 1)
cv2.imshow("disgust", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
