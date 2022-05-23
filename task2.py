from random import seed
from random import randint
def game() -> str:
    seed(1)
    guess = False
    num = randint(1, 5)
    while guess is False:
        val = input("Enter your guess: ")
        guess = right_or_wrong(num,int(val))
        print(prompt(guess,num,int(val)))



def right_or_wrong(num:int,val:int)->bool:
    if num == val:
        return True
    else:
        return False

def prompt(corret:bool,num:int,val:int)->str:
    if corret:
        return f"Your guess is correct which is {val}"
    if val > num:
        return "Your guess is higher than target"
    else:
        return "Your guess is lower than target"

g= game()