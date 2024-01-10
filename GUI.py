# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 19:19:17 2024

@author: Justice
"""
from Cards import *
from tkinter import *
from PIL import Image, ImageTk


def resize_card(card):
    our_card = Image.open(card)
    
    our_card_resize = our_card.resize((200,300))
    
    global our_card_img 
    our_card_img = ImageTk.PhotoImage(master = root, image = our_card_resize)
    
    return our_card_img
    
def blackjack():     
 player = []    
 dealer = []
 shoe = six_deckshoe(assign())
 player_card = random.choice(shoe)
 shoe.remove(player_card)
 player.append(player_card)
 dealer_card = random.choice(shoe)
 shoe.remove(dealer_card)
 dealer.append(dealer_card)
 #second card
 
 
 
 player_card2 = random.choice(shoe)
 shoe.remove(player_card2)
 player.append(player_card2)
 dealer_card2 = random.choice(shoe)
 shoe.remove(dealer_card2)
 dealer.append(dealer_card2)
 
 global dealer_image
 dealer_image = resize_card(fr"C:\Users\13054\Desktop\movetogit\PNG-cards-1.3\{dealer_card.character}_of_{dealer_card.suit}.png")
 dealer_label.config(image=dealer_image)
 
 #dealer_label.config(text=dealer_card)
 
 global player_image
 player_image = resize_card(fr"C:\Users\13054\Desktop\movetogit\PNG-cards-1.3\{player_card.character}_of_{player_card.suit}.png")
 player_label.config(image=player_image)
 
 #global dealer_image_2
 #dealer_image_2 = resize_cards(fr"C:\Users\13054\Desktop\movetogit\PNG-cards-1.3\{dealer_card2.character} of {dealer_card2.suit}*.png")
 #dealer_label2.config(image=dealer_image_2)
 
 #player_label.config(text=player_card)
 dealer_label2.config(text="will reveal once you stand")
 
 global player_image_2
 player_image_2 = resize_card(fr"C:\Users\13054\Desktop\movetogit\PNG-cards-1.3\{player_card2.character}_of_{player_card2.suit}.png")
 player_label2.config(image=player_image_2)
 
 #player_label2.config(text=player_card2)
 
 




# below is the GUI
root = Tk()
root.title("Card counting academy")
root.geometry("900x500")
root.configure(background="white")


my_frame = Frame(root, bg="white")
my_frame.pack(pady=20)

# creating frames for the first cards 
dealer_frame = LabelFrame(my_frame, text="dealers first card ", bd=1)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=40, ipady=40)

dealer_frame_2 = LabelFrame(my_frame, text="dealers second card", bd=1)
dealer_frame_2.grid(row=0, column=1, padx=20, ipadx=40, ipady=40)

player_frame = LabelFrame(my_frame, text="player first card", bd=1)
player_frame.grid(row=0, column=2, padx=20, ipadx=40, ipady=40)


player_frame_2 = LabelFrame(my_frame, text="players second card", bd=1)
player_frame_2.grid(row=0, column=3, padx=20, ipadx=40, ipady=40)

dealer_label =  Label(dealer_frame, text= " ")
dealer_label.pack(pady=20)

player_label =  Label(player_frame, text= " ")
player_label.pack(pady=20)

dealer_label2 =  Label(dealer_frame_2, text= " ")
dealer_label2.pack(pady=20)

player_label2 =  Label(player_frame_2, text= " ")
player_label2.pack(pady=20)




# creating buttons for the hit and stand

hit_button = Button(root, text = "Hit Me", font=("helvetica", 14),command=blackjack())
hit_button.pack(pady=20) 

stand_button = Button(root, text = "stand", font=("helvetica", 14))
stand_button.pack(pady= 0)

root.mainloop()



