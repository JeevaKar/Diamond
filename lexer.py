import re
import os

variable = dict()
iftrue = 0

#FUNCTIONS
def output(statement):
	statement = re.sub("out ", "", statement)
	print(statement)

def set_var(line):
	line = line.split(" ", 2)
	variable[line[1]] = line[2]
	return line

def varswap(line):
	line = line.split(" ")
	next = False
	count = 0
	for word in line:
		if word == "var":
			next = True
		elif next == True:
			line[count] = variable[word]
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
	
def math(line):
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
	return line
	
def in_put(line):
	line = line.split(" ", 2)
	temp = input(line[2]+"\n")
	variable[line[1]] = temp

def ifs(line):
	global iftrue
	line = line.split()
	line.pop(0)
	result = eval("'"+line[0]+"'"+line[1]+"'"+line[2]+"'")
	if result != True:
		iftrue += 1
	return result

def insert(line):
	line = re.sub("insert ", "", line)
	line = re.split(" ", line)
	codeo = open(line[len(line)-1])
	code = codeo.readlines()
	codeo.close()
	lexer(code)

def clear():
	os.system('cls' if os.name == 'nt' else "printf '\033c'")


#LEXER
def lexer(code):
	global iftrue
	i = 0
	while i < len(code):
		line=code[i]
		line_s = line.split(" ", 1)
		line_s = line_s[0]
		goto_search = re.search("goto ", line)
		comment = False
		if line_s == "COM":
			comment = True
		#line = math(line)
		if iftrue == 0 and comment == False:
			line = varswap(line)
			if line_s == "out":
				output(line)
			elif line_s == "in":
				in_put(line)
			elif line_s == "setvar":
				set_var(line)
			elif line_s == "cls":
				clear()
			elif line_s == "if":
				ifs(line)
			elif line_s == "insert":
				insert(line)
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