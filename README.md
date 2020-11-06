# Sloc_counter
To count total number of line in source code:


Process:
(1). Put Sloc_counter.py/Sloc_counter.exe in same folder.
(2). Pass Command line argument: Sloc_counter.py/Sloc_counter.exe Filename
(3). It will generate testfile.c for verification purpose, if not required delete it.

Known Limitation:
This will work properly in cases where preprocessor check finishes in single line.
If preprocessor check is written within multiple line abrupt behaviour can be seen.
