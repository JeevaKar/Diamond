# Diamond1
Diamond Programming Language

This is the source code for the diamond programming language developed in Python.
The syntax for this language can be found in the syntax.txt file, and consists of 7 different commands.
To use, create a file ending in .di, and edit using any text editor, or use the one included. To use with the lexer, run main.py and open the file in the text editor, open the run menu, select run, and you will get the compiled result.
If you would like to create a custom runtime environment but use the lexer, simply import the lexer function from lexer.py, and pass in the code a a list. Every item in the list should be one line of code. For example, the program:

COM This is an example program
out HELLO WORLD!
setvar x goodbye
out var x

would be passed into the lexer as a list like so: ['COM This is an example program', 'out HELLO WORLD!', 'setvar x goodbye', 'out var x']

Using the IDE:
The IDE that comes with diamond comes with three menus: File, Run, and Debug

Inside the File menu there are several basic options, which are open (to open a file), save (to save a file), save as (to save a file under a different name), and exit (to quit the program)

Inside the Run menu there are two options: Run, and Run and Log Errors. The Run button simply runs the program that you have selcted. The Run and Log Errors button runs the program, and when an error occurs, the python error will be dumped into the dump.txt file. Please note that both these options will prompt you to save your code if not yet already.

Inside the Debug menu there are several options: Cursor Position, Run and Log Errors, Error Codes, Syntax, and Read Dump Stack. The cursor position command will prompt the display of the current cursor position. This can be helpful when using the GOTO command. Run and Log Errors does the same thing as in the Run menu. Error Codes lists out all error codes and warning codes, which is the same as in the Errors.txt file. Syntax outputs the syntax for all commands in Diamond, and is the same as in the syntax.txt file. Read Dump Stack outputs the result of the most recent Runand Log Errors prompt.

Dumping Errors: Dumping errors comes with a header including time. The time is in Greenwich Median time and is NOT localized to your timezone.

To download and executable version: https://diamond-server.jacktheapple.repl.co
