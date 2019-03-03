from flask import Flask, request, redirect, url_for, send_from_directory, render_template, Response
import time
import os


# In[16]:


from nltk.tokenize import word_tokenize

# Setup Flask app.
app = Flask(__name__)
app.debug = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


def downloadComplete(): 
 
  # coding: utf-8

  # In[8]:


  #!/usr/bin/env python
  # coding: utf-8

  # In[15]:

  import sys
  import nltk
  import numpy as np
  import speech_recognition as sr


  # In[16]:


  from nltk.tokenize import word_tokenize


  # In[17]:

  r = sr.Recognizer()
  mic = sr.Microphone()
  file = sr.AudioFile('sound.wav')
  # CHECK ADDRESS
  with file as source:
      r.adjust_for_ambient_noise(source)
      audio = r.record(source)
  text = r.recognize_google(audio)


  # In[101]:


  words = word_tokenize(text)
  words = np.array(words)
  words = words.reshape(1,-1)


  # In[124]:
  name = ''
  gender = ''
  address = ''
  age = ''
  phone = ''
  aadhar = ''
  g_name = ''
  g_relationship = ''
  g_number = ''

  for w in range(words[0].shape[0]):
    if words[0][w]=='patient' and words[0][w+1]=='name':
      name= words[0][w+2]+" "+words[0][w+3]
    if words[0][w]=='gender':
      gender=words[0][w+1]
    if words[0][w]=='age':
      age=words[0][w+1]
    if words[0][w]=='patient' and words[0][w+1]=='number':
      for a in range(10):
        phone += words[0][w+2+a]
    if (words[0][w]=='Attendee' or words[0][w]=='attendee') and words[0][w+1]=='name':
      g_name=words[0][w+2]+" "+words[0][w+3]
    if (words[0][w]=='Attendee' or words[0][w]=='attendee') and words[0][w+1]=='relationship':
      g_relationship=words[0][w+4]
    if (words[0][w]=='Attendee' or words[0][w]=='attendee') and words[0][w+1]=='number':
      g_number=words[0][w+2]
  output = {'patient_name':name, 'patient_gender':gender,'patient_age':age, 'patient_phone_number':phone, 'Attendee_name':g_name,'Attendee_relationship_with_patient':g_relationship, 'Attendee_phone_number':g_number}

  import json
  with open('result.json', 'w') as fp:
      json.dump(output, fp)

  # In[47]:





# In[ ]:



  


# In[47]:





# In[ ]:

# Routes
@app.route('/')
def root():
  return render_template('home.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/details')
def detail():
  return render_template('details.html')

# AJAX Request Handler
@app.route('/done', methods=['GET', 'POST'])
def recordedSample():
  time.sleep(3)
  downloadComplete()
  time.sleep(3)
  os.remove('./sound.wav')
  

  # content = get_file('result.json')
  # return Response(content, mimetype='application/json')
  return send_from_directory('./', 'result.json')

if __name__ == '__main__':
  app.run()

