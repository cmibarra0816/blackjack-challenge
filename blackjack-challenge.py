#Blackjack Program - Extra Credit
#Blackjack Outline
    #Deck: Shuffle(), Draw (); Card Class: Suit, Value; Player: Hand, Add_Card, Score, Hit, Hold, Play; Dealer: Inherits from Player


#Import - use for shuffling cards
import random

#Boolean type to know whether play is in hand
playing=False

#Amount for buy-in
chip_pool=100
#Raw Input ("Enter the amount for buy-in:")
print "Your buy-in amount is:", chip_pool

bet=1

restart_phrase: "Press d to deal the cards again, or press q to quit."

#Hearts, Diamonds, Clubs, Spades
suits=("H", "D", "S", "C")
#Possible Card Ranks
