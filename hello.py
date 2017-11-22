#1DAY
#print("Hello")

#message = "Hello Message"
#print (message)

#print("\tmessage")


## 09.08.2017

#age = 23
#first = "happy"
#second = "rd birthday"
#print(first.title() + " " + str(age) + " " + second.title())

#mylist = ["a","b","c"]
#print(mylist[1])
#del mylist[1]
#print(mylist[1])



#2DAY
#12.08.2017
#~ list1 = ["1","2","3","4","5","6"]
#~ for flist in list1:
	#~ print(flist)


#~ for value1 in range(1,12):
	#~ print(value1)


#for numbers1 in range(1,5):
	#print(numbers1)
	
#cars = ['audi','bmw','toyota']
#for car in cars:
	#if car == 'bmw':
		#print(car.upper())
	#else:
		#print(car.title())
		
#age = 12
#if age < 4:
#	print("cost 0")
#elif age <18:
#	print("cost 5")
#else:
#	print("cost 10")

#3day
#29.19.2017

#request_toppings = []
#if request_toppings:
#	for request_topping in request_toppings:
#		print("Adding" + request_topping + ".")
#else:
#		print("Are you sure you want a plain pizza?")
		
		
#alien_0 = {'color':'green','point':5}
#print(alien_0['color'])
#alien_0['x_point'] = 0
#alien_0['y_point'] = 25

#alien_0['speed'] = 'medium'
#print(alien_0)
#if alien_0['speed'] == 'medium':
	#x_increment = 2
	
#alien_0['x_point'] = alien_0['x_point'] + x_increment

#print(alien_0)

#usr_0 = {
	#'username':'un',
	#'first':'ft',
	#'last':'lt'
	#}
#for k in usr_0.items():
	#print(k)

	
#aliens = []
#for alien_num in range(30):
	#new_alien = {'color':'green'}
	#aliens.append(new_alien)

#for alien in aliens[:5]:
	#print(alien)
	
#student ={
	#'li':{
	#'like':'computer',
	#'dislike':'japan',
	#},
	#'zhang':{
	#'like':'draw',
	#},
#}
#for a,b in student.items():
	#print(a)
	#print(b['like'])
	
	
#name = input("Please enter something;")
#print("hello," + name)

#age = input("age?")
#age = int(age)
#if age >= 30:
	#print("true")
#else :
	#print("false")
	
#prompt = "\nPlease enter the name of a city you have visited:"
#prompt += "\n(Enter quit to finished.)"
#while True:
	#city = input(prompt)
	
	#if city == "quit":
		#break
	#else:
		#print("you've been to" + " " +city.title())
		
#def get_name(first_name,last_name):
	#full_name = first_name + ' ' + last_name
	#return full_name.title()
#while True:
	#print("\nPlease input your name:")

	#f_name = input("First neme:")
	#if f_name == 'q':
		#break

	#l_name = input("Last name:")
	#if l_name == 'q':
		#break
	
	#musican = get_name(f_name,l_name)
	#print(musican)

#def city_country(city_name,country_name):
	#name = city_name + ',' + country_name
	#return(name.title())


#c_name = input("Please input your city name:")
#co_name = input ("Please input your country name:")

#get_value = city_country(c_name,co_name)
#print(get_value.itle())


#def m_person(tall,*names):
	#print("\nThey are" + ' ' +str(tall))
	#for name in names:
		#print(name)

#m_person(12,'qq','ww','ee')	

#class Car():

	#def __init__(self,make,model,year):
		#self.make = make
		#self.model = model 
		#self.year = year 
	
	#def get_descriptive_name(self):
		#long_name = str(self.year)  + self.make + self.model
		#return long_name.title()
#my_car = Car('audi','A4',2016)
#print(my_car.get_descriptive_name())
	
#class ElectricCar(Car):
	#def __init__(self,make,model,year):
		#super().__init__(make,model,year)
		#self.battery = 'abc'
	#def child_something(self):
		#print(self.battery)
	
#my_carcar = ElectricCar('a','aa',3)
#print(my_carcar.get_descriptive_name())
#my_carcar.child_something()

#car.py
#class Car():
	#def__init__(self,make,model,year):
		#self.make = make
		#...
		
#from car import Car
 
 
#with open('pi_digits.txt')as abc:
	#contents = abc.read()
	#print(contents.rstrip())
	
#file_path ='D:\python\programmer\pi_digits.txt'
#with open(file_path) as file_object:
	#for line in file_object:
		#print(line.rstrip())
		
#file_path ='D:\python\programmer\pi_digits.txt'
#with open(file_path) as file_object:
	#lines = file_object.readlines()
#pi_string = ''	
#for line in lines:
	#pi_string += line.strip()
#birthday = input("Please enter your birthday...")
#if birthday in pi_string:
	#print(str(birthday))
#file_path ='D:\python\programmer\pi_digits.txt'
#with open(file_path,'w') as file_object:
	#file_object.write("Hello.\n")
	#file_object.write("This is Abner.\n")
#try:
	#print(5/0)
#except ZeroDivisionError:
	#print("You can't divide by zero")
	
file_path ='D:\python\programmer\pi_digits.txt'
#with open(file_path) as file_object:
	#contents = file_object.read()
#words = contents.split()
#num_words = len(words)
#print(str(num_words))

#import json
#numbers = [2,3,4]
#with open(file_path,'w') as file_object:
	#json.dump(numbers,file_object)
	
#import unittest


#first_name = input("\nfirstname")
#second_name = input("\nsecondname")
#full_name = first_name + ' ' + second_name
#class NameTest(unittest.TestCase):
	#def test_name(self):
		#self.assertEqual(full_name,'Aa Bb')
#unittest.main()

#import sys
#import pygame
#def run_game():
	#pygame.init()
	#screen =pygame.display.set_mode((1200,800))
	#pygame.display.set_caption("Alien Invasion")
	#while True:
		#for event in pygame.event.get():
			#if event.type == pygame.QUIT:
				#sys.exit()
		#pygame.display.flip()
#run_game()

	
	




	













