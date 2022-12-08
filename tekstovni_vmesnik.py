import time
from os import name, system


def clear(args):
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    for a in args:
      print(a)
b=["Aplikacija za shranjevanje gesel."]
clear(b)
a = True
while a:
  ime = input("vnesi ime")
  if ime == "Gašper":
    a = False 
  else:
    clear(b)
    print('vnešeno ime je napačno')
    time.sleep(2)