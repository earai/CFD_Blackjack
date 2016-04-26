from blackjack_base_players import ProtoPlayer

class ScratchPlayer(ProtoPlayer):

    #def determine_game_state(self):
     #   print Game.dealer_hidden_card
      #  pass

    def identify_card_values(self, item):
        if item in ('K','Q','J'):
            return 10
        if item =='A':
            return 11
        else:
            return int(item)

    def play(self,current_hand,current_table):
        upcard = current_table['Dealer']
        print current_table
        my_hand = current_table[self.name]

        total_in_hand =
        if sum(current_hand) < 17:
            pass