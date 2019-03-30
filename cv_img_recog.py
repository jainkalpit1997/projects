import cv2
camera=cv2.VideoCapture(0)
ret,img=camera.read()
print(ret)
loc="/home/kalpitjain/abc.jpg"
cv2.imwrite(loc,img)
del(camera)
facecascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("/home/kalpitjain/abc.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=facecascade.detectMultiScale(gray,1.3,9,minSize=(80,80))
for (x,y,w,h) in face:
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.namedWindow("my_image",cv2.WINDOW_NORMAL)
cv2.resizeWindow("my_image",640,480)
cv2.imshow("my_image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()      


