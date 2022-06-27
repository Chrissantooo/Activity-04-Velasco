import cv2
import os

while True:
    file = input(" \nFile name: ")
    fileName = str(file + '.jpg')

    flag = int(input("[1] Colored [2] Grayscale \nEnter Flag Values: "))

    if flag == 1:
        if os.path.exists(fileName):
            image = cv2.imread(fileName,1)
            if file == 'disgust':
                name = 'disgust meme'
                cv2.imshow(name, image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            
            if file == 'mushroom':
                name = 'mushroom meme'
                cv2.imshow(name, image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break

        else:
            print("File not found...")

    elif flag == 2:
        if os.path.exists(fileName):
            image = cv2.imread(fileName,0)
            if file == 'disgust':
                name = 'disgust meme'
                cv2.imshow(name, image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break

            if file == 'mushroom':
                name = 'mushroom meme'
                cv2.imshow(name, image)
                cv2.waitKey(0)  
                cv2.destroyAllWindows()
                break

        else:
            print("File not found...")

    else:
        print("Error Flag...")
