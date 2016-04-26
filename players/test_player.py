from blackjack_base_players import ProtoPlayer

class ScratchPlayer(ProtoPlayer):
    def play(self,current_hand,current_table):
        upcard = current_table['Dealer']
        if sum(current_hand) < 17:
            pass