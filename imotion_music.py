from tkinter import*
import random
import os
import pygame
import vlc
import speech_recognition as sr 
import requests
#from mutagen.id3 import ID3
#from tkMessageBox import *
from tkinter.ttk import Progressbar
import requests
import cv2,sys,time
from keras.models import load_model
import numpy as np

from utils.datasets import get_labels
from utils.inference import detect_faces
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.inference import load_image
from utils.preprocessor import preprocess_input


camera_port = 0 
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)
 
def get_image():
 retval, im = camera.read()
 if retval==True:
    print('Image captured successfully')
 else:
    print('No Image captured')
 return im

print("Taking image...")
camera_capture = get_image()
file = "test_image.png"
cv2.imwrite(file, camera_capture)
del(camera)

image_path = 'test_image.png'
detection_model_path = 'haarcascade_frontalface_default.xml'
emotion_model_path = 'fer2013_mini_XCEPTION.110-0.65.hdf5'
gender_model_path = '/home/ankit/Python37/files/music_player123/simple_CNN.81-0.96.hdf5'
emotion_labels = get_labels('fer2013')
gender_labels = get_labels('imdb')
font = cv2.FONT_HERSHEY_SIMPLEX

# hyper-parameters for bounding boxes shape
gender_offsets = (30, 60)
gender_offsets = (10, 10)
emotion_offsets = (20, 40)
emotion_offsets = (0, 0)

# loading models
face_detection = load_detection_model(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)
gender_classifier = load_model(gender_model_path, compile=False)
print(emotion_classifier)
# getting input model shapes for inference
emotion_target_size = emotion_classifier.input_shape[1:3]
gender_target_size = gender_classifier.input_shape[1:3]
print(emotion_target_size,gender_target_size)

# loading images
rgb_image = load_image(image_path, grayscale=False)
gray_image = load_image(image_path, grayscale=True)
gray_image = np.squeeze(gray_image)
gray_image = gray_image.astype('uint8')

faces = detect_faces(face_detection, gray_image)
for face_coordinates in faces:
    x1, x2, y1, y2 = apply_offsets(face_coordinates, gender_offsets)
    rgb_face = rgb_image[y1:y2, x1:x2]

    x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
    gray_face = gray_image[y1:y2, x1:x2]

    try:
        rgb_face = cv2.resize(rgb_face, (gender_target_size))
        gray_face = cv2.resize(gray_face, (emotion_target_size))
    except:
        continue

    rgb_face = preprocess_input(rgb_face, False)
    rgb_face = np.expand_dims(rgb_face, 0)
    gender_prediction = gender_classifier.predict(rgb_face)
    gender_label_arg = np.argmax(gender_prediction)
    gender_text = gender_labels[gender_label_arg]

    gray_face = preprocess_input(gray_face, True)
    gray_face = np.expand_dims(gray_face, 0)
    gray_face = np.expand_dims(gray_face, -1)
    emotion_label_arg = np.argmax(emotion_classifier.predict(gray_face))
    emotion_text = emotion_labels[emotion_label_arg]

    if gender_text == gender_labels[0]:
        color = (0, 0, 255)
    else:
        color = (255, 0, 0)

    draw_bounding_box(face_coordinates, rgb_image, color)
    draw_text(face_coordinates, rgb_image, gender_text, color, 0, -20, 1, 2)
    draw_text(face_coordinates, rgb_image, emotion_text, color, 0, -50, 1, 2)

bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
cv2.imwrite('ankit.png', bgr_image)
print (emotion_text)
l=emotion_text


root = Tk()
root.geometry("1600x800+0+0")
root.title("Music Player")

text_Input = StringVar()
operator = ""

instance = vlc.Instance()
player = instance.media_player_new()



Tops = Frame(root, width = 1600, height = 50, bg = "Pink" ,relief = SUNKEN)
Tops.pack(side=TOP)
f1= Frame(root,width = 800, height = 700, bg = "Pink",relief = SUNKEN)
f1.pack(side=LEFT)
f2= Frame(root,width = 200,height = 700, bg = "Pink",relief = SUNKEN)
f2.pack(side=RIGHT)

#localtime = time.asctime(time.localtime(time.time()))
lbifo = Label(Tops,font=('arial',50,"bold"),text="MUSIC PLAYER",fg="Red",bd =10,anchor ="w")
lbifo.grid(row=0,column=0)	

#lbifo1 = Label(Tops,font=('arial',20,"bold"),text=s,fg="Red",bd =10,anchor ="w")
#lbifo1.grid(row=1,column=0)
def timedisplay():
	localtime = time.asctime(time.localtime(time.time()))
	lbifo1 = Label(Tops,font=('arial',20,"bold"),text=localtime,fg="Red",bd =10,anchor ="w")
	lbifo1.grid(row=1,column=0)
def displaytime():
	timedisplay()
	Tops.after(1000,displaytime)
displaytime()

e=[]
d = []
index = 0
for dirname, dirnames, filenames in os.walk('.'):
	print (filenames)
     #print path to all subdirectories first.
	for subdirname in dirnames:
     		x = (os.path.join(dirname, subdirname))
	for filename in filenames:
		if filename.endswith(".mp3"):
			p=(os.path.join(dirname, filename))
			d.append(p)
			e.append(filename)
listbox = Listbox(f2,width = 50,height = 20)
listbox.grid(row =0,column=2)	

for items in e:
	listbox.insert(0,items)


	

def startsong():
	lsl=len(d)
	t=random.randint(0,lsl-1)
	#u = StringVar(f1,value =e[t])
	#q = player.audio_get_time(e[t])
	#print(q)
	songtex = Label(f1,font=('arial',16,"bold"),text=e[t] ,bd = 10,bg = "powder blue",justify ='right').grid(row=1,column=1)
	pb_hD = Progressbar(f1, orient='horizontal', mode='determinate')
	pb_hD.grid(row=2,column=1)
	#if(player.is_playing == 1):
	pb_hD.start(1000)
	media = instance.media_new(d[t])
	player.set_media(media)
	player.play()	
def next():
	player.stop()
	startsong()

def previous():
	player.stop()
	startsong()

def stop():
	player.stop()
def pp():
	if(player.is_playing()==0):
		player.play()
	else:
		player.pause()
def volumeup():
	s = player.audio_get_volume()
	s = s+1
	player.audio_set_volume(s)
def volumedown():
	s = player.audio_get_volume()
	s = s-1
	player.audio_set_volume(s)
def mm():
	s=player.audio_get_volume()
	if(s!=0):
		player.audio_set_volume(0)
	else:
		player.audio_set_volume(50)


#StartButton =Button(f2,padx=16,pady=16,bd=8,fg = "black",font=('arial',20,'bold'),text="Start Song",bg ="Pink",command =startsong).grid(row =4,column=3)
NextButton =Button(f2,padx=16,pady=16,bd=8,fg = "black",font=('arial',20,'bold'),text="Next Song",bg ="Pink",command =next).grid(row=3,column=0)
PreviousButton =Button(f2,padx=16,pady=16,bd=8,fg = "black",font=('arial',20,'bold'),text="Previous Song",bg ="Pink",command=previous).grid(row =3,column=1)
#StopButton =Button(f2,padx=16,pady=16,bd=8,fg = "black",font=('arial',20,'bold'),text="Stop",bg ="Pink",command =stop).grid(row=1,column=2)
ppButton =Button(f2,padx=16,pady=16,bd=8,fg = "black",font=('arial',20,'bold'),text="Pause/play",bg ="Pink",command =pp).grid(row=2,column=0)
volumeupButton =Button(f2,padx=16,pady=16,bd=8,fg = "black",font=('arial',20,'bold'),text="Volume +",bg ="Pink",command =volumeup).grid(row =1,column=0)
volumedownButton =Button(f2,padx=16,pady=16,bd=8,fg = "black",font=('arial',20,'bold'),text="Volume -",bg ="Pink",command =volumedown).grid(row =1,column=1)
MuteButton =Button(f2,padx=16,pady=16,bd=8,fg = "black",font=('arial',20,'bold'),text="Mute",bg ="Pink",command =mm).grid(row=2,column=1)
	
emotionleb= Label(f1,font=('arial',16,"bold"),text ="Emotion",bd = 16,anchor='w').grid(row=0,column=0)
#v = StringVar(f1,value =l)
emotiontex = Label(f1,font=('arial',16,"bold"),text=l ,bd = 10,bg = "powder blue",justify ='right').grid(row=0,column=1)
songleb= Label(f1,font=('arial',16,"bold"),text ="Now Playing",bd = 16,anchor='w').grid(row=1,column=0)


#showinfo(title = "Mood", message = l)
startsong()



root.mainloop()
















