import re
import os
from datetime import datetime

variable = dict()
iftrue = 0

#FUNCTIONS
def output(statement, log = False):
	try:
		statement = re.sub("out ", "", statement)
		print(statement)
		return 1
	except Exception as Argument:
		if log == True:
			file = open("dump.txt", "a")
			file.write(str(Argument))
			file.close()
		print("Error 2: Syntax Error")
		return 0

def set_var(line, log = False):
	try:
		line = line.split(" ", 2)
		variable[line[1]] = line[2]
		return 1
	except Exception as Argument:
		if log == True:
			file = open("dump.txt", "a")
			file.write(str(Argument))
			file.close()
		print("ERROR 2: Syntax Error")
		print("WARNING 3: Check syntax of your variable")
		return 0

def varswap(line, log = False):
	line = line.split(" ")
	next = False
	count = 0
	for word in line:
		if word == "var":
			next = True
		elif next == True:
			try:
				line[count] = variable[word]
			except Exception as Argument:
				if log == True:
					file = open("dump.txt", "a")
					file.write(str(Argument))
					file.close()
				print("ERROR 1: Variable Specified does not exist")
				return False
			next = False
		count += 1
	count = 0
	while count < len(line):
		if line[count] == 'var':
			line.pop(count)
		else:
			count += 1
	return_value = ""
	for item in line:
		if return_value == "":
			return_value = item
		else:
			return_value += " " + item
	return return_value
	
def math(line, log = False):
	error = False
	try:
		line = re.split(" ", line)
		count = 0
		temp = line
		while count < len(temp):
			try:
				if count == 0:
					line = eval(temp[count])
				else:
					line += str(" ")+str(eval(temp[count]))
				count += 1
			except:
				if count == 0:
					line = temp[count]
				else:
					line = str(line) + " " + temp[count]
				count += 1
	except Exception as Argument:
		if log == True:
			file = open("dump.txt", "a")
			file.write(str(Argument))
			file.close()
		error = True
		print("ERROR 4: Math error")
	if error == False:
		return line
	else:
		return 0
	
def in_put(line, log = False):
	line = line.split(" ", 2)
	error = False
	try:
		temp = input(line[2]+"\n")
	except Exception as Argument:
		print("ERROR 2: Syntax Error")
		print("WARNING 1: Specify a question to be printed on screen")
		error = True
		if log == True:
			file = open("dump.txt", "a")
			file.write(str(Argument))
			file.close()
	try:
		variable[line[1]] = temp
	except Exception as Argument:
		if error != True:
			print("ERROR 1: Variable does not exist")
			print("WARNING 2: Initialize variable before use in input function.")
		error = True
		if log == True:
			file = open("dump.txt", "a")
			file.write(str(Argument))
			file.close()
	if error == False:
		return 1
	else:
		return 0

def ifs(line, log = False):
	error = False
	global iftrue
	line = line.split()
	line.pop(0)
	try:
		result = eval("'"+line[0]+"'"+line[1]+"'"+line[2]+"'")
		if result != True:
			iftrue += 1
	except Exception as Argument:
		error = True
		print('ERROR 3: Comparison not specified')
		if log == True:
			file = open("dump.txt", "a")
			file.write(str(Argument))
			file.close()
	if error == False:
		return 1
	else:
		return 0
	

def insert(line, log = False):
	line = re.sub("insert ", "", line)
	line = re.split(" ", line)
	try:
		codeo = open(line[len(line)-1])
		code = codeo.readlines()
		codeo.close()
		lexer(code)
		return 1
	except Exception as Argument:
		print("ERROR 4: File does not exist")
		if log == True:
			file = open("dump.txt", "a")
			file.write(str(Argument))
			file.close()
		return 0

def clear(log = False):
	try:
		os.system('cls' if os.name == 'nt' else "printf '\033c'")
		return 1
	except Exception as Argument:
		print('ERROR 2: Syntax Error')
		if log == True:
			file = open("dump.txt", "a")
			file.write(str(Argument))
			file.close()
		return 0


#LEXER
def lexer(code, log = False):
	if log == True:
		file = open("dump.txt", "w")
		file.write("Log file:\nRun time and date: " + str(datetime.now()) + "\n")
		file.close()
	global iftrue
	i = 0
	while i < len(code):
		line=code[i]
		line_s = line.split(" ", 1)
		line_s = line_s[0]
		comment = False
		if line_s == "COM":
			comment = True
		line = math(line, log)
		if iftrue == 0 and comment == False:
			line = varswap(line, log=log)
			if line_s == "out":
				output(line, log=log)
			elif line_s == "in":
				in_put(line, log=log)
			elif line_s == "setvar":
				set_var(line, log=log)
			elif line_s == "cls":
				clear(log=log)
			elif line_s == "if":
				ifs(line, log=log)
			elif line_s == "insert":
				insert(line, log=log)
			elif line_s == "goto":
				goto_search = re.sub("goto ", "", line)
				i = int(goto_search)-2
			elif line == "endif":
				x = 10;
				del x
			else:
				print("Error: Command not found")
				print("Line: "+i)
				break
		else:
			x = re.search("endif", line)
			if x:
				iftrue -= 1
		i += 1
	return 1
