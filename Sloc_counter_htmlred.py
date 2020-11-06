from __future__ import print_function
import os
import re
import sys

def remove_comments(text):
    """ remove c-style comments.
        text: blob of text with comments (can include newlines)
        returns: text with comments removed
    """
    pattern = r"""
                            ##  --------- COMMENT ---------
           /\*              ##  Start of /* ... */ comment
           [^*]*\*+         ##  Non-* followed by 1-or-more *'s
           (                ##
             [^/*][^*]*\*+  ##
           )*               ##  0-or-more things which don't start with /
                            ##    but do end with '*'
           /                ##  End of /* ... */ comment
         |                  ##  -OR-  various things which aren't comments:
           (                ## 
                            ##  ------ " ... " STRING ------
             "              ##  Start of " ... " string
             (              ##
               \\.          ##  Escaped char
             |              ##  -OR-
               [^"\\]       ##  Non "\ characters
             )*             ##
             "              ##  End of " ... " string
           |                ##  -OR-
                            ##
                            ##  ------ ' ... ' STRING ------
             '              ##  Start of ' ... ' string
             (              ##
               \\.          ##  Escaped char
             |              ##  -OR-
               [^'\\]       ##  Non '\ characters
             )*             ##
             '              ##  End of ' ... ' string
           |                ##  -OR-
                            ##
                            ##  ------ ANYTHING ELSE -------
             .              ##  Anything other char
             [^/"'\\]*      ##  Chars which doesn't start a comment, string
           )                ##    or escape
    """
    regex = re.compile(pattern, re.VERBOSE|re.MULTILINE|re.DOTALL)
    nocomments = [m.group(2) for m in regex.finditer(text) if m.group(2)]

    return "".join(nocomments)

def remove_hash():
    fh = open(filename, "r+")
    file1= open("testfile.html","w+")
    count=0
    for line in fh:
            if 'COLOR="#FF311D' in line and not 'loop' in line:
                file1.writelines(line)
                count=count+1
                print(count)
    file1.close()
    fh.close()
if __name__ == '__main__':
    filename = sys.argv[1]
    code_w_comments = open(filename).read()
    code_wo_comments = remove_comments(code_w_comments)
    fh = open(filename, "w")
    fh.write(code_wo_comments)
    fh.close()
    Final_Sourc_code = remove_hash()