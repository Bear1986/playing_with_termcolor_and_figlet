import termcolor
import pyfiglet

x = pyfiglet.figlet_format(input("Whats your name?: "))
termcolor.cprint(x, "green") # remember to add the c to print