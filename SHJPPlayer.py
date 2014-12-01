__author__ = 'Samantha'
#Samantha Holloway, Joseph Pannizzo 11/2014
#Help/code pieces from Dr. Ganesh Baliga
#Rock Paper Scissors implementation of Player class
#A gambit is a predetermined RPS strategy
#AI uses 1 of 8 famous gambits randomly for a match

import Player
import Message
import random

class SHJPPlayer(Player.Player):
    def __init__(self):
        #Call super class constructor
        Player.Player.__init__(self)
        self.history = ""
        self.reset()


    def play(self):
        return SHJPPlayerStrategy.play()

    def reset(self):
        self.history = ""


    def notify(self,message):
        self.history = message  #We don't use history for our strategy

    def get_name(self):
        return "Sam-n-Joe"



class SHJPPlayerStrategy(object):
    move = random.randint(1,8)  # choose random gambit
    current_move = 0

    #Gambits are only 3 moves a piece,used to reset if we get to 4
    @staticmethod
    def reset():
        SHJPPlayerStrategy.current_move = 0
        SHJPPlayerStrategy.move = random.randint(1,8)

    #Provides AI for making a move, returns move as a string
    #move is either Rock(0), Paper(1), or Scissors(2)
    @staticmethod
    def play():

        if SHJPPlayerStrategy.move == 1: #Denoument gambit
            SHJPPlayerStrategy.current_move += 1
            if SHJPPlayerStrategy.current_move == 1:
                return 0
            elif SHJPPlayerStrategy.current_move == 2:
                return 2
            else:
                SHJPPlayerStrategy.reset()
                return 1
        elif SHJPPlayerStrategy.move == 2: #Bureaucrat gambit
            SHJPPlayerStrategy.current_move += 1
            if SHJPPlayerStrategy.current_move == 1:
                return 1
            elif SHJPPlayerStrategy.current_move == 2:
                return 1
            else:
                SHJPPlayerStrategy.reset()
                return 1
        elif SHJPPlayerStrategy.move == 3: #Crescendo gambit
            SHJPPlayerStrategy.current_move += 1
            if SHJPPlayerStrategy.current_move == 1:
                return 1
            elif SHJPPlayerStrategy.current_move == 2:
                return 2
            else:
                SHJPPlayerStrategy.reset()
                return 0
        elif SHJPPlayerStrategy.move == 4: #Avalanche gambit
            SHJPPlayerStrategy.current_move += 1
            if SHJPPlayerStrategy.current_move == 1:
                return 0
            elif SHJPPlayerStrategy.current_move == 2:
                return 0
            else:
                SHJPPlayerStrategy.reset()
                return 0
        elif SHJPPlayerStrategy.move == 5: #Fistfull o' Dollars gambit
            SHJPPlayerStrategy.current_move += 1
            if SHJPPlayerStrategy.current_move == 1:
                return 0
            elif SHJPPlayerStrategy.current_move == 2:
                return 1
            else:
                SHJPPlayerStrategy.reset()
                return 1
        elif SHJPPlayerStrategy.move == 6: #Paper Dolls gambit
            SHJPPlayerStrategy.current_move += 1
            if SHJPPlayerStrategy.current_move == 1:
                return 1
            elif SHJPPlayerStrategy.current_move == 2:
                return 2
            else:
                SHJPPlayerStrategy.reset()
                return 2
        elif SHJPPlayerStrategy.move == 7: #Scissor Sandwich gambit
            SHJPPlayerStrategy.current_move += 1
            if SHJPPlayerStrategy.current_move == 1:
                return 1
            elif SHJPPlayerStrategy.current_move == 2:
                return 2
            else:
                SHJPPlayerStrategy.reset()
                return 1
        else: #SHJPPlayerStrategy.move == 8, Toolbox gambit
            SHJPPlayerStrategy.current_move += 1
            if SHJPPlayerStrategy.current_move == 1:
                return 2
            elif SHJPPlayerStrategy.current_move == 2:
                return 2
            else:
                SHJPPlayerStrategy.reset()
                return 2

