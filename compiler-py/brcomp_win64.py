import os
import sys
import json

### Token Types ###
# def_static
# def_abs
# def_func
# def_var
# copy_abs_class

class Token:
    def __init__(self, ttype, value = ""):
        self.type = ttype
        self.value = value


def main():
    if len(sys.argv) != 3:
        print("USAGE: br_comp_win64 <INPUT_PATH> <PROJECT_NAME>")
        sys.exit(1)

    program_path = sys.argv[1]
    project = json.loads(open(program_path + "/" + sys.argv[2]).read())

    main_file = open(program_path + "/src/" + project["program"]).read()

    pass


def lexer(cont: str):
    i = 0

    while i < len(cont):
        if cont[i].isalpha():
            temp = ""

            while cont[i].isalnum:
                temp += cont[i]
                i += 1

            token_type = ""

            if temp == "dc":
                temp2 = ""

                i += 1
                while cont[i].isalnum:
                    temp2 += cont[i]
                    i += 1

                if temp2 == "static":
                    token_type = "def_static"
                elif temp2 == "abstract":
                    token_type = "def_abs"
                else:
                    print('COMPILER FAILED\nPROCESS - "LEXER"\ndefined class that was non-static and non-abstract')
                    sys.exit(2)

        i += 1


main()