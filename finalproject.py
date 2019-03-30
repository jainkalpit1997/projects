#take input from voice
from nltk.corpus import stopwords,wordnet
from nltk.tokenize import word_tokenize
import socket
import requests
import wikipedia,geocoder
import speech_recognition as sr
import pyttsx3,webbrowser
import os,subprocess
import json
from weather import Weather, Unit
import geocoder
import re    #for finding digit 
# Record Audio
def audio():
    while(1): 
        with sr.Microphone() as source:
          r.adjust_for_ambient_noise(source)
          print("Say something!")
          audio = r.listen(source)
        try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
          print("You said: " + r.recognize_google(audio))
          return audio
        except sr.UnknownValueError:
      #print("Google Speech Recognition could not understand audio")
          continue 
        except sr.RequestError as e:
          print("Could not request results from Google Speech Recognition service; {0}".format(e))


#speak message      
def speak(x):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  rate = engine.getProperty('rate')
  engine.setProperty('rate', rate-50)
  engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MS-Anna-1033-20-DSK')
  #engine.say(r.recognize_google(audio1))   
  engine.say(x) 
  engine.runAndWait()

#remove stop words

def filter(var):
  stop_words = set(stopwords.words('english'))-{'in','at','of','after'}
  word_tokens = word_tokenize(var)
  filtered_sentence = [w for w in word_tokens if not w in stop_words]
  filtered_sentence = []
  for w in word_tokens:
      if w not in stop_words:
          filtered_sentence.append(w)
  return (filtered_sentence)


#synonym checker
def syn_checker(word):
    word_synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemma_names():
            if lemma in data :
                word_synonyms.append(lemma)
    if(len(word_synonyms)!=0):
       return True
    else:
       return False
#weather

def weather_checker(loc):
     weather = Weather(unit=Unit.CELSIUS)
     lookup = weather.lookup_by_location(loc)
     condition = lookup.condition
     print("the weather is "+condition.text+" in "+loc)
     speak("at this time weather is "+condition.text+" in "+loc)
     print("the temperature is "+condition.temp+" degree celsius in "+loc)
     speak("at this time temperature is "+condition.temp+" degree celsius in "+loc)

#predict weather
def pred_weather(loc,count):
     var=1
     weather = Weather(unit=Unit.CELSIUS)
     location = weather.lookup_by_location(loc)
     forecasts = location.forecast
     for forecast in forecasts:
         if(var==count):
            print(forecast.text)
            print(forecast.date)
            print(forecast.high)
            print(forecast.low) 
            speak("weather will be "+forecast.text+"highest temperature will be "+forecast.high+"and lowest temperature will be "+forecast.low+" degree celsius on "+forecast.date)
            var=var+1
         else:
            var=var+1 
     



 
while(1):
  r = sr.Recognizer()
  data1=audio()
  data1=r.recognize_google(data1)
  not_split_data=data1
  data1=data1.split()
  data=filter(not_split_data)
  str=['how','are','you']
  if all(x in data1 for x in str):
     speak("i am fine")

#for start or open anything 
  str=['open','start']
  if any(x in data1 for x in str):
       if 'open' in data1:
           ind=data1.index('open')
       else:
           ind=data1.index('start')
       if(data1[ind+1]=='the'):
           ind=ind+2
       else:
           ind=ind+1
       if 'calculator' in data1:
           os.system('gnome-calculator')
       elif 'calendar' in data1:
           os.system('gnome-calendar')
       elif 'Notepad' in data1:
           os.system('gedit')
       elif 'terminal' in data1:
           os.system('gnome-terminal')
       else:
           webbrowser.open_new('http://www.'+data1[ind]+'.com')
 
#for ip address   
  str=['IP','address']
  if all(x in data1 for x in str):    
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect(("8.8.8.8", 80))
      print("your ip address is "+s.getsockname()[0])
      speak("your IP address is "+s.getsockname()[0])
      s.close() 
  
  str=['thanks','thank']
  if any(x in data1 for x in str):
      speak("your welcome")

  str=['location']
  if any(x in data1 for x in str):
      g=geocoder.freegeoip('2405:205:1409:8be7:3871:2d31:6fcf:be09')
      #print(g.json)
      print(g.json['city'],g.json['raw']['region_name'],g.json['raw']['country_name'])
      speak(" your location is "+g.json['city']+g.json['raw']['region_name']+g.json['raw']['country_name'])

   
#for weather
  if('temperature' in data or syn_checker('weather')):
      g=geocoder.freegeoip('2405:205:1409:8be7:3871:2d31:6fcf:be09')
      loc=g.json['city']
      '''import requests
      import json
      send_url = "http://api.ipstack.com/check?access_key=deeab2107e1cdaf5171b9e2980521a7d"  #ipstack api
      geo_req = requests.get(send_url)
      geo_json = json.loads(geo_req.text)
      latitude = geo_json['latitude']
      longitude = geo_json['longitude']
      loc = geo_json['city']
      #print(city)'''
      if 'in' in data:
          pos=data.index('in')
          loc=data[pos+1]
      elif 'at' in data:
          pos=data.index('at')
          loc=data[pos+1]
      elif 'of' in data:
          pos=data.index('of')
          if(data[pos]!='today' or data[pos]!='tomorrow'):      #(ex. temp of kota     and temp of today)
            loc=data[pos+1]
      num=re.findall('\d+',not_split_data)      
      if(len(num)!=0):
          num=int(num[0])
      if('after' in data):
          if(num>=10):
             speak("prediction for next 9 days only")
          else:
             pred_weather(loc,num+1)
      elif('next' in data):
          if(num==0):
            pred_weather(loc,2)
          else:
            if(num>10):
               speak("i can provide you next 9 days weather  that are")
               for x in range(1,11):
                   pred_weather(loc,x)
            else:
               for x in range(2,num+2):
                   pred_weather(loc,x)
      elif('today' in data):
          pred_weather(loc,1)
      elif('tomorrow' in data):
          pred_weather(loc,2)   
      else:
          weather_checker(loc)
          
              
      
       
           
   
