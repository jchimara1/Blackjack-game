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
  # assigning values 
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
         
  return curr_deck




def assign():
    deck_f = []
    deck = create_deck()
    for a_card in deck:
      suit = a_card[0]
      character = a_card[1]
      value = a_card[2]
##########################################
      curr_card = card(suit, character, value)
      deck_f.append(curr_card)
##########################################
    return deck_f


def six_deckshoe(deck):
    six_deckshoe = []
    d_1 = deck 
    d_2 = deck
    d_3 = deck
    d_4 = deck
    d_5 = deck
    d_6 = deck
    six_deckshoe.append([d_1, d_2, d_3, d_4, d_5, d_6])
    return six_deckshoe


def retrieve():    
 a = six_deckshoe(assign())
 nested_deck = [i.pop() for i in a]
 for i in nested_deck:
    deck = i
    return(random.choice(deck))


def player_cards():
 card1 = retrieve()
 card2 = retrieve()
 #print(card1, card2)
 print("you currently have", card1.value + card2.value, "would like to pull a card?\n")
 return(card1.value + card2.value)


def dealer_cards():
 card1 = retrieve()
 card2 = retrieve() 
 #print(card1, card2)
 #print(card1.value + card2.value)
 print(f"the dealer is showing a {card1}")
 return(card1.value + card2.value, card1)



dealer = dealer_cards()[0]


if dealer < 21:
 player1 = player_cards()
 if input("yes or no?").lower() == "yes":
  player1 = player1 + retrieve().value
  print(player1)
 else:
  print("you total is", player1)  


while dealer < 17:
    dealer = dealer + retrieve().value
    if dealer >=17:
        break

if dealer >= 17:
    
 if dealer > 21:
     print("dealer lost this hand")
 elif dealer > player1:
     print("dealer won this hand")
print(dealer)    