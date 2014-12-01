__author__ = 'Collin Day and Joe Kvedaras'
import random
# Example of how to implement an RPS player within the framework

import Player
import Message

class CDJKPlayer(Player.Player):

    def __init__(self):
        # Call super class constructor
        Player.Player.__init__(self)
        self.reset()

    def play(self):
        return RpsPlayingStrategy.play(self.opponents_moves)

    def reset(self):
        self.opponents_moves = []

    def get_name(self):
        return "Minimizer"

    def notify(self, msg):

        # We use notifications to store opponent's moves in past rounds
        # Process match-start and round-end messages
        # At the start of the match, clear opponent moves history since a new match has started
        # At the end of a round, append move to opponent's move history. Move history is used
        # to compute the next move played.
        if msg.is_match_start_message():
            players = msg.get_players()
            if players[0] == self or players[1] == self:
                self.reset()
        elif msg.is_round_end_message():
            players = msg.get_players()
            # Check if this message is for me and only then proceed
            if (players[0] == self) or (players[1] == self):
                # In this case, (by convention) the info is a tuple of the moves made and result e.g. ((1, 0), 1) which
                # means player 1 played paper (1), the player 2 played rock(0) and the result was that
                # player 1 won

                moves, result = msg.get_info()

                # RPS is a two person game; figure out which of the players is me
                # and which one is the opponent
                if players[0] == self:
                    opponent = 1
                else:
                    opponent = 0

                # Update opponent's past moves history
                self.opponents_moves.append(moves[opponent])



# An implementation of a simple rps playing strategy
class RpsPlayingStrategy(object):

    @staticmethod
    def play(opponents_moves):
        # We assume other will assume to use either the most played or the
        #least played move so play the middle one no one would expect that.
        #also if the numbers are equal it will just pick one at random.
        #we put random numbers in certain places to throw off others stratigies

        # count number of rock, paper and scissors moves made in the past
        
        count = [0, 0, 0]

        for move in opponents_moves:
            count[move] += 1

        if (count[0] > count[1] & count[0] < count[2]) | (count[0] < count[1] & count[0] > count[2]):
            use = 0
        elif (count[1] > count[0] & count[1] < count[2]) | (count[1] < count[0] & count[1] > count[2]):
            use = 1

        elif (count[2] > count[0] & count[2] < count[1]) | (count[2] < count[0] & count[2] > count[1]):
            use = 2

        else:
            use = random.randrange(0,3)

        # Assuming that other will base their moves on either the most used or least used move
        #ours is bassed off the middle used move
        return use

# Test driver
# Run by typing "python3 CDKJPlayer.py"

if __name__ == "__main__":
    player = CDJKPlayer()
    opponent = CDJKPlayer()
    players = [opponent,player]
    fakeinfo = ((0,0),0)
    fakeresult = 1
    fakemoves = (0,2)

    player.notify(Message.Message.get_match_start_message(players))
    player.notify(Message.Message.get_round_start_message(players))
    move = player.play()
    print ("Move played: ", move)
    player.notify(Message.Message.get_round_end_message(players,fakemoves,fakeresult))


