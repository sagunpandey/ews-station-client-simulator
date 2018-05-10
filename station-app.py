# Water Client GUI
# Python v3.6.3
# By Shelby LeBlac and Sagun Pandey

from tkinter import *
import requests
import json
import datetime
import random
import time as Time
import os
import multiprocessing

def client(clientId):

	root = Tk()
	entry = []
	label = []
	entryText1 = StringVar()
	entryText2 = StringVar()
	entryText3 = StringVar()
	number_of_labels = 3
	id = clientId
	time = ""
	level = ""
	url2 = 'http://10.30.41.115:8080/reading'


	def display():

		#creation of spaces to see input
		entry.append(Entry(root,text=entryText1,width=30))
		entry.append(Entry(root,text=entryText2,width=30))
		entry.append(Entry(root,text=entryText3,width=30))
		
		#creation of labels
		label.append(Label(root, text="Read Time",fg="black",font=14))
		label.append(Label(root, text="Water Level",fg="black",font=14))
		label.append(Label(root, text="Station ID",fg="black",font=14))

		#alignment of variables in GUI
		for i in range(number_of_labels):
			entry[i].grid(row=i, column=1)
			label[i].grid(row=i,sticky=W)
			
		#submitButton.grid(columnspan=2)
		
		#Title of GUI and size
		root.title("Water Client")
		root.geometry("300x150")
		
	def update():

		#assign time and random water level
		time=datetime.datetime.now().isoformat()
		level=random.randrange(10,50)
		
		#set values to be displayed
		entryText1.set(time)
		entryText2.set(level)
		entryText3.set(id)
		

		#export function
		exportJson(time,level)
		Time.sleep(1)

		#update GUI after random amount seconds (1-5)
		root.after(random.randrange(6000,10000,1000),update)
		
		#loop until window is closed
		root.mainloop()
		
			
	def exportJson(time,level):
		data = {"readTime": time,"waterLevel": level,"station":{ "id": id}}
		headers = {"Content-Type": "application/json"}
		response = requests.put(url2,data=json.dumps(data), headers=headers)
	display()
	update()
				
	
#main: creates client processes
if __name__ == '__main__':
	number_process = 6
	p = []
	
	#making the processes
	for i in range(number_process):
		p.append(multiprocessing.Process(target=client, args=(i+1,)))
		p[i].start()
		
	#waiting for processes to close
	for i in range(number_process):
		p[i].join()
	
	

