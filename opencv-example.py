import cv2

img= cv2.imread("C:\\Users\\YourName\\FileName.jpg") #please change it to your file's path

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade=cv2.CascadeClassifier("C:\\Users\\classifiers\\haarcascade_frontalface_default.xml") #change it to your classifier's path

faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,minNeighbors=20) #you may need to change the neighbors to get a more accurate reading)

print(type(faces))
print(faces)

for x,y,w,h in faces:
	img= cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0,3))

resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("G", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
