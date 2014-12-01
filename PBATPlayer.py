__authors__ = 'Pat and Tony'

import random
import Player
import Message


class PBATPlayer(Player.Player):
    # self variables
    player_list = []
    rock_cut = .3
    paper_cut = .6
    total = 10
    name = None

    # finds a player and his information
    def find_player(self, person):
        found_player = False
        player = [person, 0, 0, 0]

        for i in range(0, len(self.player_list)):
            if (self.player_list[i][0] == person):
                player = self.player_list[i]
                found_player = True
                break

        if (not found_player):
            self.player_list.append(player)

        return player

    # gets the data for who I am playing against
    # sets my odds to play against his pattern
    def me_playing_against(self, person):
        player = self.find_player(person)
        global total, rock_cut, paper_cut

        rock_count = player[1]
        paper_count = player[2]
        scissor_count = player[3]
        total = rock_count + paper_count + scissor_count

        if (total >= 5):
            rock_cut = rock_count / total
            paper_cut = paper_count / total

    # keeps track of what a player picks
    def match_results(self, person, played):
        player = self.find_player(person)

        if (played == "rock"):
            player[1] = player[1] + 1
        elif (played == "paper"):
            player[2] = player[2] + 1
        elif (played == "scissors"):
            player[3] = player[3] + 1

    # implementing observer method
    # string checks will need to change to what messages actually will be
    def notify(self, msg):
        if msg.is_match_start_message():
            p_list = msg.get_players()
            self.p1 = p_list[0].name
            self.p2 = p_list[1].name
        elif msg.is_round_end_message():
            if not self.p1 == self.name:
                self.match_results(self.p1, msg.get_info()[0][0])
            if not self.p2 == self.name:
                self.match_results(self.p2, msg.get_info()[0][1])
        elif msg.is_round_start_message():
            if self.p1 == self.name:
                self.me_playing_against(self.p2)
            elif self.p2 == self.name:
                self.me_playing_against(self.p1)

    # returns my move, based on what the other player chooses most often
    def play(self, position=None):
        weight = random.random()

        if (weight < self.paper_cut):
            return 2
        elif ((weight - self.paper_cut) < self.rock_cut):
            return 1
        else:
            return 0

    def get_name(self):
        return self.name


class RpsStrategy(object):
    # returns my move, based on what the other player chooses most often
    @staticmethod
    def play(opponents_moves):
        count = [0, 0, 0]
        weight = random.random()

        if weight < paper_cut:
            return 2
        elif weight - paper_cut < rock_cut:
            return 1
        else:
            return 0


if __name__ == "__main__":
    player = RPSPlayer()
    opponent = RPSPlayer()
    players = [opponent, player]
    fake_moves = (1, 2)
    fake_result = (0, 1)

    player.notify(Message.Message.get_match_start_message(players))
    player.notify(Message.Message.get_round_start_message(players))
    move = player.play()
    print("Move played: ", move)
    player.notify(Message.Message.get_round_end_message(players, fake_moves, fake_result))