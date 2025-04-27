# **** TRANSLATOR **** #

from tkinter import*
from tkinter import ttk

from googletrans import LANGUAGES,Translator



def change(text="type",src="English",dest="Hindi"):
    text1 = text
    src1 = src
    dest1= dest
    trans = Translator()
    trans1 =  trans.translate(text,src=src1,dest=dest1)
    return trans1.text


def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0,END)
    textget = change(text = masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
 
    dest_txt.insert(END,textget)    




root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg='skyblue')

lab_txt= Label(root,text='Translator',font=('Time New Roman',20,"bold"),bg='lavender')
lab_txt.place(x=100,y=40,height= 50,width=300)

frame=Frame(root).pack(side=BOTTOM)

lab_txt= Label(root,text='Source Text',font=('Time New Roman',20,"bold"),fg='black',bg='skyblue')
lab_txt.place(x=100,y=100,height= 20,width=300)

Sor_txt = Text(frame,font=('Time New Roman',20,"bold"),wrap=WORD,bg='lavender')
Sor_txt.place(x=10,y=130,height= 150,width=480)


list_text = list(LANGUAGES.values())


comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height= 40,width=150)
comb_sor.set("English")

button_change =Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height= 40,width=150)


comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height= 40,width=150)
comb_dest.set("English")

lab_txt= Label(root,text='Dest Text',font=('Time New Roman',20,"bold"),fg='black',bg='skyblue')
lab_txt.place(x=100,y=360,height= 20,width=300)


dest_txt = Text(frame,font=('Time New Roman',20,"bold"),wrap=WORD,bg='lavender')
dest_txt.place(x=10,y=360,height= 150,width=480)


root.mainloop()

# ****** GOOGLE TRANSLATOR ***** #

# Importing necessary modules required
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os


# Creating Recogniser() class object
recog1 = spr.Recognizer()

# Creating microphone instance
mc = spr.Microphone()


# Capture Voice
with mc as source:
	print("Speak 'hello' to initiate the Translation !")
	print("hello")
	recog1.adjust_for_ambient_noise(source, duration=0.2)
	audio = recog1.listen(source)
	MyText = recog1.recognize_google(audio)
	MyText = MyText.lower()

# Here initialising the recorder with
# hello, whatever after that hello it
# will recognise it.
if 'hello' in MyText:
	
	# Translator method for translation
	translator = Translator()
	
	# short form of english in which
	# you will speak
	from_lang = 'en'
	
	# In which we want to convert, short
	# form of hindi
	to_lang = 'hi'
	
	with mc as source:
		
		print("Speak a stentence...")
		recog1.adjust_for_ambient_noise(source, duration=0.2)
		
		# Storing the speech into audio variable
		audio = recog1.listen(source)
		
		# Using recognize.google() method to
		# convert audio into text
		get_sentence = recog1.recognize_google(audio)

		# Using try and except block to improve
		# its efficiency.
		try:
			
			# Printing Speech which need to
			# be translated.
			print("Phase to be Translated :"+ get_sentence)

			# Using translate() method which requires
			# three arguments, 1st the sentence which
			# needs to be translated 2nd source language
			# and 3rd to which we need to translate in
			text_to_translate = translator.translate(get_sentence,
													src= from_lang,
													dest= to_lang)
			
			# Storing the translated text in text
			# variable
			text = text_to_translate.text

			# Using Google-Text-to-Speech ie, gTTS() method
			# to speak the translated text into the
			# destination language which is stored in to_lang.
			# Also, we have given 3rd argument as False because
			# by default it speaks very slowly
			speak = gTTS(text=text, lang=to_lang, slow= False)

			# Using save() method to save the translated
			# speech in capture_voice.mp3
			speak.save("captured_voice.mp3")	
			
			# Using OS module to run the translated voice.
			os.system("start captured_voice.mp3")

		# Here we are using except block for UnknownValue
		# and Request Error and printing the same to
		# provide better service to the user.
		except spr.UnknownValueError:
			print("Unable to Understand the Input")
			
		except spr.RequestError as e:
			print("Unable to provide Required Output".format(e))
		