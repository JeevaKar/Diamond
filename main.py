from tkinter import *
from tkinter.ttk import Label
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from lexer import lexer
import sys

compiler = Tk()
compiler.title('Diamond IDE')
file_path = ''

def set_file_path(path):
	global file_path
	file_path = path


def open_file():
	path = askopenfilename(filetypes=[('Diamond Files', '*.di')])
	with open(path, 'r') as file:
		code = file.read()
		editor.delete('1.0', END)
		editor.insert('1.0', code)
		set_file_path(path)


def save_as():
	if file_path == '':
		path = asksaveasfilename(filetypes=[('Diamond Files', '*.di')])
	else:
		path = file_path
	with open(path, 'w') as file:
		code = editor.get('1.0', END)
		file.write(code)
		set_file_path(path)


def run():
	if file_path == '':
		save_prompt = Toplevel()
		text = Label(save_prompt, text='Please save your code')
		text.pack()
		return
	code = editor.get("1.0",END).split('\n')
	code = list(filter(None, code))
	lexer(['cls'])
	lexer(code)
	print("Code execution complete")

def run_log():
	if file_path == '':
		save_prompt = Toplevel()
		text = Label(save_prompt, text='Please save your code')
		text.pack()
		return
	code = editor.get("1.0",END).split('\n')
	code = list(filter(None, code))
	lexer(['cls'])
	lexer(code, log=True)
	print("Code execution complete")

def cursor_pos():
	save_prompt = Toplevel()
	text = Label(save_prompt, text="Current Cursor Position: " + str(editor.index('insert')))
	text.pack()

def errors():
	file = open("Errors.txt", "r")
	print(file.read())
	file.close()

def syntax():
	file = open("Syntax.txt", 'r')
	print(file.read())
	file.close()

def dump_stack():
	file = open("dump.txt", "r")
	print(file.read())
	file.close()

def exit():
	sys.exit()

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
run_bar.add_command(label='Run and Log Errors', command=run_log)
menu_bar.add_cascade(label='Run', menu=run_bar)

debug_bar = Menu(menu_bar, tearoff=0)
debug_bar.add_command(label='Cursor Position', command=cursor_pos)
debug_bar.add_command(label="Run and Log Errors", command=run_log)
debug_bar.add_command(label="Error Codes", command=errors)
debug_bar.add_command(label="Syntax", command=syntax)
debug_bar.add_command(label="Read Dump Stack", command=dump_stack)
menu_bar.add_cascade(label="Debug", menu=debug_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

compiler.mainloop()
