import speech_recognition as sr
import webbrowser as wb
import whatsapp_mssgss as wpp
r3=sr.Recognizer()
r2=sr.Recognizer()
with sr.Microphone() as source:
	print("Which site you wanna open")
	print("Youtube")
	print("Instagram")
	print("Whatsapp")
	audio=r3.listen(source,phrase_time_limit=3)
	print("done")
	print("you spoke="+r2.recognize_google(audio))
if "YouTube" in r2.recognize_google(audio):
	print("what do you want to search?")
	print("speak now!")
	r2=sr.Recognizer()
	url='https://www.youtube.com/'
	with sr.Microphone() as source:
		audio1=r2.listen(source,phrase_time_limit=6)
		print("time over!!!")
		print("searching the querry")

	try:
		querry=r2.recognize_google(audio1)
		print("searched"+querry)
		wb.get().open_new(url+"results?search_query="+querry)
	except:
		print("error")
elif "insta" in r2.recognize_google(audio):
	r3=sr.Recognizer()
	url='https://www.instagram.com/'
	print("what do you want to search?")
	print("speak now!")
	with sr.Microphone() as source1:
		audio2=r3.listen(source1,phrase_time_limit=5)
		print("time over!!!")

	try:
		querry1=r3.recognize_google(audio2)
		print("searching the page "+querry1)
		wb.get().open_new(url+querry1+"/")
	except:
		print("error")

elif "WhatsApp" in r2.recognize_google(audio):
	try:
		wpp.fun12()
	except:
		print("can not go to imported file")
else:
	print("say again")

