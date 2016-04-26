from blackjack_base_players import ProtoPlayer

class ScratchPlayer(ProtoPlayer):

    def __init__(self,name='Erin'):
        ProtoPlayer.__init__(self, name)
        self.total_in_hand = []

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

    def dealer_state(self,current_table):
        return current_table['Dealer']


    def determine_action(self,upcard):

        if upcard in ['2','3','4','5,','6']:
            if self.total_in_hand >= 13:
                return 'stand'
            if self.total_in_hand < 12:
                return 'hit'

        if upcard in ['7','8','9','10','J','Q','K','A']:
            if self.total_in_hand >= 17:
                return 'stand'
            if self.total_in_hand < 16:
                return 'hit'

    def play(self,current_hand,current_table):
        upcard = self.dealer_state(current_table)
        my_hand = current_hand.cards
        scores=  current_hand.possible_scores()
        self.total_in_hand = current_hand.best_score()

        action = self.determine_action(upcard)
        return action

    def bet(self, current_funds, minimum_bet, maximum_bet):
        if self.total_in_hand == 21:
            return maximum_bet
        else:
            return minimum_bet



