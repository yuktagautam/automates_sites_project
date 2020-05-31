#taking the input using keyborad and then it automates to your whatsapp site
#scan  the qr code
#write the desired information asked by console application 
#it will automatically type the mssg and send it to the entered user
from selenium import webdriver as wb
import speech_recognition as sr
def fun12():
	r7=sr.Recognizer()
	print("1.you want to type")
	print("2.you want to speak")
	flag=int(input("Enter 1 or 2"))
	if(flag==1):
			q1=input("Enter the name you wanna search!")
			q2=input("Enter the message you wanna type!")
			q3=input("Enter how many times you want to send this message")
	elif(flag==2):
		with sr.Microphone() as source:
			print("say the name you wanna search!")
			audio1=r7.listen(source,phrase_time_limit=5)
			print(" time over!!")
			print("Recognizing what you said")
			print("say the message you want to send")
			audio2=r7.listen(source,phrase_time_limit=5)
			print(" time over!!")
			print("Recognizing what you said")
			print("How many times you want to send this mssg")
			print("speak now!")
			audio3=r7.listen(source,phrase_time_limit=4)
			print("time over!!!")
			q1=r7.recognize_google(audio1)
			q2=r7.recognize_google(audio2)
			q3=r7.recognize_google(audio3)
	print(q1)
	print(q2)
	print(q3)
	chrome_path=r"C:\Users\User\Desktop\chromedriver_win32 (1)\chromedriver.exe"
	driver=wb.Chrome(chrome_path)
	driver.get("https://web.whatsapp.com/")
	driver.maximize_window()
	name=q1
	msg=q2
	count=int(q3)
	input("scan QR code then enter something")
	user=driver.find_element_by_xpath("//span[@title='{}']".format(name))
	user.click()
	mssg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
	for index in range(count):
		mssg_box.send_keys(msg)
		driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]").click()
	print("succsess")


