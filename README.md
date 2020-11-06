# Sloc_counter
To count total number of line in source code:

Caution:
Make a seperate folder for count purpose only, because code is written in such a way 
that it will overwrite original .c file with nocomments version of same code.

Process:
(1). Put Sloc_counter.py/Sloc_counter.exe in same folder.
(2). Pass Command line argument: Sloc_counter.py/Sloc_counter.exe Filename(.c or .html files can be used in place of Filename)
(3). It will generate testfile.c for verification purpose, if not required delete it.

Remarks:
nocomments version of .c file will include Sloc with preprocessers.
nocomments version of .html file will make task easy to count uncovered part of Sloc.
testfile.c contain only Sloc(comments and preprocessers are deleted).

Known Limitation:
This will work properly in cases where preprocessor check finishes in single line.
If preprocessor check is written within multiple line abrupt behaviour can be seen.

