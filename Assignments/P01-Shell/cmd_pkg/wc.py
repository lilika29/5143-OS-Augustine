'''Dr griffin
code
'''
'''
Name
     wc
     
Discription 
            wc filename    #counts num of lines words charecters 
            wc -l filename #counts num of lines 
            wc -m filename #counts num of words
            wc -w filename #counts num of char 

'''


import re  # Regular Expression(RE) Syntax AND
import sys
from cmd_pkgs.arg_parser import ArgParse
from cmd_pkgs.return_status import ReturnStatus

# "re" module included with Python primarily used for string searching and manipulation
## And it is necessory for using regex (findall()) function
from cmd_pkgs.return_status import ReturnStatus

arg_dict = {
    'l': False,
    'm': False,
    'w': False,
}


def wc(args, cwd):
    arg_parse = ArgParse(args, arg_dict, cwd, __doc__)
    flags = arg_parse.get_flags()
    rs = ReturnStatus()
    rs.set_cwd(cwd)
    directories = arg_parse.get_directories()

    rs.set_return_values("\n")
    rs.set_return_values("hello world1")
    sys.stdout.flush()
    if not flags:
        rs.set_return_values("helloooo world")
        filenum = 0

        for p in directories:
            with open(directories[filenum], "r") as f:
                lines = f.readlines()  # Use f.read() combined with splitlines()The splitlines()
                # method splits a string into a list. The splitting is done at line breaks.

            with open(directories[filenum], "r") as f:
                words = f.read()

            numlines = str(len(lines))
            rs.set_return_values(numlines + " ")  # prints number of lines
            
            numwords = str(len(words.split())) + " "  #  count the
            # number of words in the sentence available
            # in a regex module.
            rs.set_return_values(numwords)

            chars = str(len(words))
            rs.set_return_values(chars + " ")

            sys.stdout.flush()

            filenum += 1


    else:

        # wc-l is getting the number of lines in the file
        filenum = 0
        if flags[0] == "-l":
            for p in directories:
                with open(directories[filenum], "r") as f:
                    lines = f.read().splitlines()

                    lines = len(lines)

                rs.set_return_values(lines, " lines ")
                filenum += 1

        # Find the number of words wc -w
        elif flags[0] == "-w":
            filenum = 0
            for p in directories:
                with open(directories[filenum], "r") as f:
                    words = f.read()

                numwords = len(re.findall(r'\w+', words))

                rs.set_return_values(numwords, " words")

                filenum += 1
        # wc -m finding number of charecters
        elif flags[0] == "-m":
            filenum = 0
            for p in directories:
                with open(directories[filenum], "r") as f:
                    chars = f.read()

                numchar = len(chars)

                rs.set_return_values(numchar, "characters")
                filenum += 1

        else:
            rs.set_return_values("Invalid")
    return rs


