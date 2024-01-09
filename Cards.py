# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 01:16:57 2023

@author: Justice
"""
#testing git 

import random
from PIL import Image 
import glob
import time






cardsfolder = r"C:\Users\13054\Desktop\movetogit\PNG-cards-1.3"
#im = Image.open(r"C:\Users\13054\Desktop\movetogit\PNG-cards-1.3\2_of_hearts.png")  
#im.show()



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
    six_deckshoe.extend(deck)
    six_deckshoe.extend(deck)
    six_deckshoe.extend(deck)
    six_deckshoe.extend(deck)
    six_deckshoe.extend(deck)
    six_deckshoe.extend(deck)
    return six_deckshoe

# this function will be replaced when in action with 
# a pop to simulate a real shoe however this function could be used to simulate a automate shuffler
def retrieve():    
 shoe = six_deckshoe(assign())
 card = random.choice(shoe)
 if glob.glob(fr"C:\Users\13054\Desktop\movetogit\PNG-cards-1.3\{card.character} of {card.suit}*.png"):
  img = Image.open(fr"C:\Users\13054\Desktop\movetogit\PNG-cards-1.3\{card.character} of {card.suit}*.png")
  img.show()
 return(card)


def player_cards():
 card1 = retrieve()
 if card1.character == "K":
     card1.character ="king"
 if card1.character == "Q":
     card1.character ="queen"    
 if card1.character == "J":
     card1.character = "jack"     
 img = Image.open(fr"C:\Users\13054\Desktop\movetogit\PNG-cards-1.3\{card1.character}_of_{card1.suit}.png")
 img.show()
 card2 = retrieve()
 if card2.character == "K":
     card2.character ="king"
 if card2.character == "Q":
     card2.character ="queen"    
 if card2.character == "J":
     card2.character = "jack"     
 img = Image.open(fr"C:\Users\13054\Desktop\movetogit\PNG-cards-1.3\{card2.character}_of_{card2.suit}.png")
 img.show()
 #print(card1, card2)
 print("you currently have", card1.value + card2.value, "would like to pull a card?\n")
 return(card1.value + card2.value)


def dealer_cards():
 card1 = retrieve()
 if card1.character == "K":
     card1.character ="king"
 if card1.character == "Q":
     card1.character ="queen"    
 if card1.character == "J":
     card1.character = "jack"     
 img = Image.open(fr"C:\Users\13054\Desktop\movetogit\PNG-cards-1.3\{card1.character}_of_{card1.suit}.png")
 img.show()
 card2 = retrieve() 
 #print(card1, card2)
 #print(card1.value + card2.value)
 print(f"the dealer is showing a {card1}")
 return(card1.value + card2.value, card1)

#test = six_deckshoe(assign())

dealer = dealer_cards()[0]

time.sleep(5)


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