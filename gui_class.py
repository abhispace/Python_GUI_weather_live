from tkinter import Tk, Label, Button
from tkinter import messagebox 
import matplotlib as mpl
import numpy as np
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg

class MyFirstGUI:

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.grid(row=8,column=1)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.grid(row=9,column=1)

        self.close_button = Button(master, text="Close", command=self.close_window)
        self.close_button.grid(row=10,column=1)
        
	
	# set the name of tkinter GUI window 
#	root.title("Gui Application") 

	# Set the background colour of GUI window 
	master.configure(background = "light grey") 

	# Set the configuration of GUI window 
	master.geometry("900x600") 

	# Create a Weather Gui Application label 
	self.headlabel = Label(master, text = "Weather Gui Application", 
					fg = 'black', bg = 'yellow') 
	
	# Create a City name : label 
	self.label1 = Label(master, text = "City name : ", 
				fg = 'red', bg = 'light green') 
	
	# Create a City name : label 
	self.label2 = Label(master, text = "Temperature :", 
				fg = 'red', bg = 'light green') 

	# Create a atm pressure : label 
	self.label3 = Label(master, text = "atm pressure :", 
				fg = 'red', bg = 'light green') 

	# Create a humidity : label 
	self.label4 = Label(root, text = "humidity :", 
				fg = 'red', bg = 'light green') 

	# Create a description :label 
	self.label5 = Label(master, text = "description :", 
				fg = 'red', bg = 'light green') 
	

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	self.headlabel.grid(row = 0, column = 1) 
	self.label1.grid(row = 1, column = 0, sticky ="E") 
	self.label2.grid(row = 3, column = 0, sticky ="E") 
	self.label3.grid(row = 4, column = 0, sticky ="E") 
	self.label4.grid(row = 5, column = 0, sticky ="E") 
	self.label5.grid(row = 6, column = 0, sticky ="E") 


	# Create a text entry box 
	# for filling or typing the information. 
	self.city_field = tk.Entry(root) 
	self.temp_field = tk.Entry(root) 
	self.atm_field = tk.Entry(root) 
	self.humid_field = tk.Entry(root) 
	self.desc_field = tk.Entry(root) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	# ipadx keyword argument set width of entry space . 
	self.city_field.grid(row = 1, column = 1, ipadx ="100") 
	self.temp_field.grid(row = 3, column = 1, ipadx ="100") 
	self.atm_field.grid(row = 4, column = 1, ipadx ="100") 
	self.humid_field.grid(row = 5, column = 1, ipadx ="100") 
	self.desc_field.grid(row = 6, column = 1, ipadx ="100") 

	# Create a Submit Button and attached 
	# to tell_weather function 

	button1 = tk.Button(root, text = "Submit", bg = "red", 
					fg = "black", command = self.tell_weather) 

	# Create a Clear Button and attached 
	# to clear_all function 
	button2 = tk.Button(root, text = "Clear", bg = "red", 
					fg = "black", command = self.clear_all) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	button1.grid(row = 2, column = 1) 
	button2.grid(row = 7, column = 1) 
	

    def greet(self):
        print("Greetings!")

    def close_window(self):
        root.destroy()
    
    # Function for clearing the 
# contents of all text entry boxes 
    def clear_all(self): 
	self.city_field.delete(0, tk.END) 
	self.temp_field.delete(0, tk.END) 
	self.atm_field.delete(0, tk.END) 
	self.humid_field.delete(0, tk.END) 
	self.desc_field.delete(0, tk.END) 

	# set focus on the city_field entry box 
	self.city_field.focus_set()
        
    def tell_weather(self) : 

	# import required modules 
	import requests, json 

	# enter your api key here 
	api_key = "37e58e603526ab23dccbffdebb74b40a"

	# base_url variable to store url 
	base_url = "http://api.openweathermap.org/data/2.5/weather?"


	# take a city name from city_field entry box 
	city_name = self.city_field.get() 

	# complete_url variable to store complete url address 
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

	# get method of requests module 
	# return response object 
	response = requests.get(complete_url) 

	# json method of response object convert 
	# json format data into python format data 
	x = response.json() 

	# now x contains list of nested dictionaries 
	# we know dictionary contains key value pair 
	# check the value of "cod" key is equal to "404" 
	# or not if not that means city is found 
	# otherwise city is not found 
	if x["cod"] != "404" : 

		# store the value of "main" key in variable y 
		y = x["main"] 

		# store the value corresponding to the "temp" key of y 
		current_temperature = y["temp"] 

		# store the value corresponding to the "pressure" key of y 
		current_pressure = y["pressure"] 

		# store the value corresponding to the "humidity" key of y 
		current_humidiy = y["humidity"] 

		# store the value of "weather" key in variable z 
		z = x["weather"] 

		# store the value corresponding to the "description" key 
		# at the 0th index of z 
		weather_description = z[0]["description"] 

		# insert method inserting the 
		# value in the text entry box. 
		self.temp_field.insert(15, str(current_temperature-273) + " Celsius") 
		self.atm_field.insert(10, str(current_pressure) + " hPa") 
		self.humid_field.insert(15, str(current_humidiy) + " %") 
		self.desc_field.insert(10, str(weather_description) ) 

	# if city is not found				 
	else : 

		# message dialog box appear which 
		# shows given Error meassgae 
		messagebox.showerror("Error", "City Not Found \n"
							"Please enter valid city name") 

		# clear the content of city_field entry box 
		self.city_field.delete(0, tk.END) 


                
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
