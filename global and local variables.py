spam = 42 # global variable

def eggs():
    spam = 42 # local variable, temp will not exist after the fuction ends

print('Some code here.')
print('Some more code here.')

# all lines of codes are in either the global or local scope
# scope is a container of variables
# variables are either GLOBAL or LOCAL, never both
# global scope variables are created when the program begins and are destroyed when the program ends
# local scope variables are created when that function is called and destroyed when the fuction ends
#
# Code in global scope can't use local variables
# Code in a local scope can use global variables
# different locals cant reach into to other locals
# technically you can use the same name for a variable in local and global

# why use global vs local at all?
# allows easier debugging, if a fuction has a bug you only need to look at that code, not the entire global





def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
        ham = 101
        eggs = 0

spam()
# returns 99 because the eggs of 0 in bacon is foggoten as soon as the bacon function ends



def spam():
    print(eggs)

eggs = 42
spam()

# here eggs is assigned as only a global variable, but it is called in the spam function def as a local variable.
# python determines that because there is no eggs local variable that it should use the global variable eggs automatically
# python looks for an assignment statement locally to determine if the variable is local or global


def spam():
    eggs = 'local eggs 11'    # assignment statement exists within this function, python will use the local eggs now
    print(eggs)
    
eggs = 'global eggs 42'
spam()
print(eggs)   # this will return the gobal eggs because it is not in a fuction locally


def spam():
    global eggs             # to call a global variable, even when an assignment exists, use the global statement
    eggs = 'local eggs 11'    # assignment statement exists within this function, python will use the local eggs now
    print(eggs)

eggs = 'global eggs 42'
spam()
print(eggs)   # this will return the gobal eggs because it is not in a fuction locally


