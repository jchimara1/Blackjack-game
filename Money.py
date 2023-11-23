# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 22:17:08 2023

@author: Justice
"""


class buy_in:
    
    
    #initialization
    def __init__(self, cash, f_chips, o_chips):
        self.cash = cash
        self.f_chips = f_chips
        self.o_chips = o_chips
        
        
        
    def __str__(self):  
        return f"player has {self.cash} in {self.f_chips}, 5 dollar chips and {self.o_chips}, 1 dollar chips"
    
    
def get_cash():
    while True:
     try:
         cash = int(input("how much cash did you come to the casio with?\n"))
         break
     except:
        print("That's not a valid option!")

    return(int(cash))

def get_bet():
    bet = 10
    while True:
     try:
        ante = int(input("how much would you like to make a bet in addition to the ante\n"))
        break
     except:
        print("That's not a valid option!")

    total_bet = bet+ante
    return(total_bet, ante)

def get_chips():
    
    player_cash = get_cash()
    five_chips = player_cash // 5
    one_chips =  player_cash % 5
    return(player_cash, five_chips, one_chips)
    


def get_buyin():
    money = get_chips()
    cash = money[0] 
    f_chips = money[1]
    o_chips = money[2]
    
    return buy_in(cash, f_chips, o_chips) 



def main(): 
    buyin = get_buyin()
    return(buyin)


if __name__ == "__main__":
    print(main()) 