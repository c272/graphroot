#Grabbing prerequisites.
from time import *
from parser import *

#Setting initial variables.
equation = ""
ansfloat = 1
versionnum = "0.0.1"
file = open("./output.txt", "w")

#Setting functions.
def parse_equation(y, x):
    #Setting to global
    global file
    global ansstring
    global xroot
    ansstring = expr(str(y)).compile()
    ansstring = eval(ansstring)
    xroot = float(str(ansstring))
    file.write("N: "+str(ansstring)+"\n")

#Timeline.
print("Welcome to Graphroot v"+versionnum+".\nPlease use 'x' as your variable. Always include operators!")
sleep(1)
print("Please enter an equation: ")
equation=input("")

print("Please enter your X0: ")
xroot=float(input(""))

print("Please enter how many times you want to calculate your equation: ")
times=int(input(""))

for i in range(0, times):
    print("N"+str(i)+":")
    parse_equation(equation, xroot)
file.close()
print("Output written to file: ./output.txt.")
