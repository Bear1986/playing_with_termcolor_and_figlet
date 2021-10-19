import pyfiglet
from termcolor import colored


msg = input("what do you want to print?: ")
color = input("what color?: ")

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)
print(colored_ascii)