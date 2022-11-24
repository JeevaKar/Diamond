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
