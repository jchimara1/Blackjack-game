# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 01:16:57 2023

@author: Justice
"""
#testing git 

import random


class card:
    
    
    def __init__(self, suit, character, value):
        self.suit = suit
        self.character = character
        self.value = value
        
    def __str__(self):
        return f"{self.character} of {self.suit}"
    
    def suit(self, suit):
        if not suit:
            raise ValueError("no suit")
            
    def character(self, character):
        if not character:
            raise ValueError("no character")    
def create_deck():
  suits = ['clubs', "hearts", "spades", "diamonds"]
  values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  deck = []
 
  for i in range(len(suits)):
    for j in range(len(values)):
      deck.append((suits[i], values[j]))
  return deck


        
def assign_value():
    deck = create_deck()
    curr_deck = []
    for card in deck:
        if card[1] == "A":
         value = 11
         curr_deck.append([card[0], card[1], value])
        elif card[1] == "J" or card[1] == "Q" or card[1] ==  "K":
         value = 10 
         curr_deck.append([card[0], card[1], value])
        else: 
          value = int(card[1])
          curr_deck.append([card[0], card[1], value])
          
    return(curr_deck)


def get_card():
    deck = assign_value()
    a_card = random.choice(deck)
    suit = a_card[0]
    character = a_card[1]
    value = a_card[2]
    curr_card = card(suit, character, value)
    return curr_card


# def main(): 
#     card = get_card()
#     return(card)

    
# if __name__ == "__main__":
#     print(main())     