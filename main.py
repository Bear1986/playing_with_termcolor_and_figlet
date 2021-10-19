from pyfiglet import figlet_format
from termcolor import colored



def print_art(msg, color):
  valid_colors = ("red", "green", "blue", "yellow")
  if color not in valid_colors:
    color = "white"
  ascii_art = figlet_format(msg)
  colored_ascii = colored(ascii_art, color=color)
  print(colored_ascii)

def main():
  msg = input("what do you want to print?: ")
  color = input("what color?: ")
  print_art(msg,color)

main()
