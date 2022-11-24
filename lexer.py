import re
import os

variable = dict()
iftrue = True

#FUNCTIONS
def output(statement):
	statement = re.sub("out ", "", statement)
	print(statement)

def setvar(line):
	line = re.split(" ", line)
	og = line
	count = 0
	count_set_name = None
	name = None
	val = ""
	for word in line:
		if count > 5:
			val += " " + word
		elif count > 4:
			val += word
		count += 1
	variable[og[4]] = val

def varswap(line, ifs = False):
	line = re.split(" ", line)
	count = 0
	count_set = None
	comp = None
	for word in line:
		tempcomp = word
		if word == "var":
			count_set = count + 1
			tempcomp = None
		if count_set == count:
			word = re.sub("\n", "", word)
			if ifs:
				tempcomp = "'"+variable[word]+"'"
			else:
				tempcomp = variable[word]
		if tempcomp != None:
			if comp == None:
				comp = tempcomp
			else:
				comp = comp + " " + tempcomp
		count += 1
	return comp
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
	line = re.split(" in ", line)
	temp = input(line[1]+"\n")
	variable[line[0]] = temp

def ifs(line):
	global iftrue
	x = re.sub("if", "",line)
	x = re.split(" ", x)
	con1 = str()
	func = str()
	con2 = str()
	func_reach = False
	count = 0
	x.pop(0)
	x[len(x)-1] = re.sub("\n", "", x[len(x)-1])
	for item in x:
		if re.search("=|<|>|!", item):
			func = item
			func_reach = True
		elif func_reach != True:
			con1 += item
		elif func_reach == True:
			con2 += item
		count += 1
	x = "con1"+func+"con2"
	x = eval(x)
	iftrue = bool(x)

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
		out_search = re.search("out", line)
		in_search = re.search(" in ", line)
		setvar_search = re.search("setvar", line)
		varswap_search = re.search("var ", line)
		clear_search = re.search("cls", line)
		if_state = re.search("if ", line)
		insert_search = re.search("insert", line)
		comment_search = re.split("COM", line)
		goto_search = re.search("goto ", line)
		comment = False
		if len(comment_search)>1:
			comment = True
		line = math(line)
		if iftrue == True and comment == False:
			if varswap:
				if if_state:
					line = varswap(line, True)
				else:
					line = varswap(line)
			if out_search:
				output(line)
			elif in_search:
				in_put(line)
			elif setvar_search:
				setvar(line)
			elif clear_search:
				clear()
			elif if_state:
				ifs(line)
			elif insert_search:
				insert(line)
			elif goto_search:
				goto_search = re.sub("goto ", "", line)
				i = int(goto_search)-2
			elif line == "endif":
				x = 10;
				del x
			else:
				print("Error: Command not found")
				break
		else:
			x = re.search("endif", line)
			if x:
				iftrue = True
		i += 1