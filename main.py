from tkinter import *

result = 0
operator = ""
field_length = 0
root = Tk()
root.title("Simple Calculator")
field = Entry(root,width=30)
field.grid(row=0,column=0,columnspan=3)

def post(num):
	field_value = field.get()
	field.delete(0,END)
	field.insert(0,str(field_value)+str(num))

def delete():
	field_value = field.get()
	field.delete(0,END)
	field.insert(0,field_value[0:-1])

def clear():
	global result,field_length,operator
	result = 0
	field_length = 0
	operator = ""
	field.delete(0,END)

# trying to make a calculator with all the input in the field bar
def addition():
	global result,operator,field_length
	field_value = field.get()
	if(result == 0):
		try:
			result = int(field_value)
		except ValueError:
			result = float(field_value)
	else:
		try:
			result = result + int(field_value[field_length:])
		except ValueError:
			result = float(result) + float(field_value[field_length:])
	field_length = len(str(field_value)) + 1
	operator="+"
	post("+")


def substraction():
	global result,operator,field_length
	field_value = field.get()
	if(result == 0):
		try:
			result = int(field_value)
		except ValueError:
			result = float(field_value)
	else:
		try:
			result = result - int(field_value[field_length:])
		except ValueError:
			result = float(result) - float(field_value[field_length:])
	field_length = len(str(field_value)) + 1
	operator="-"
	post("-")

def multiplication():
	global result,operator,field_length
	field_value = field.get()
	if(result == 0):
		try:
			result = int(field_value)
		except ValueError:
			result = float(field_value)
	else:
		try:
			result = result * int(field_value[field_length:])
		except ValueError:
			result = float(result) * float(field_value[field_length:])
	field_length = len(str(field_value)) + 1
	operator="*"
	post("*")

def division():
	global result,operator,field_length
	field_value = field.get()
	if(result == 0):
		try:
			result = int(field_value)
		except ValueError:
			result = float(field_value)
	else:
		try:
			result = result / int(field_value[field_length:])
		except ValueError:
			result = float(result) / float(field_value[field_length:])
	field_length = len(str(field_value)) + 1
	operator="/"
	post("/")

def evaluate():
	global result,operator,field_length
	field_value = field.get()
	try:
		field_value = int(field_value[field_length:])
	except ValueError:
		field_value = float(field_value[field_length:])
	if(type(result) == float):
		result = "{:.2f}".format(eval("float(result)" +operator+ "float(field_value)"))
	elif(type(field_value) == float):
		result = "{:.2f}".format(eval("float(result)" +operator+ "float(field_value)"))
	else:
		result = eval("int(result)" +operator+ "int(field_value)")
	field.delete(0,END)
	field.insert(0,str(result))
	result = 0
	field_length = 0

one = Button(root,text="1",command=lambda: post(1),padx=33,pady=14).grid(row=1,column=0)
two = Button(root,text="2",command=lambda: post(2),padx=33,pady=14).grid(row=1,column=1)
three = Button(root,text="3",command=lambda: post(3),padx=33,pady=14).grid(row=1,column=2)

four = Button(root,text="4",command=lambda: post(4),padx=33,pady=14).grid(row=2,column=0)
five = Button(root,text="5",command=lambda: post(5),padx=33,pady=14).grid(row=2,column=1)
six = Button(root,text="6",command=lambda: post(6),padx=33,pady=14).grid(row=2,column=2)

seven = Button(root,text="7",command=lambda: post(7),padx=33,pady=14).grid(row=3,column=0)
eight = Button(root,text="8",command=lambda: post(8),padx=33,pady=14).grid(row=3,column=1)
nine = Button(root,text="9",command=lambda: post(9),padx=33,pady=14).grid(row=3,column=2)
	
zero = Button(root,text="0",command=lambda: post(0),padx=33,pady=14).grid(row=4,column=1)
decimal = Button(root,text=".",command=lambda: post("."),padx=36,pady=14).grid(row=4,column=0)
delete = Button(root,text="<-",command=delete,padx=29,pady=14).grid(row=5,column=2) 
equalto = Button(root,text="=",command=evaluate,padx=33,pady=14).grid(row=4,column=2)
add = Button(root,text="+",command=addition,padx=33,pady=14).grid(row=5,column =0)
substraction = Button(root,text="-",command=substraction,padx=33,pady=14).grid(row=5,column=1)
multiplication = Button(root,text="*",command=multiplication,padx=33,pady=14).grid(row=6,column=0)
division = Button(root,text="/",command=division,padx=33,pady=14).grid(row=6,column=1)
clear = Button(root,text="Clear",command=clear,padx=23,pady=14).grid(row=6,column=2)



root.mainloop()

