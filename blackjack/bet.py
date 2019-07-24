
class Bet:
    pass


class BlackjackBet(Bet):
    def __init__(self, bet):
        self.bet = bet

    def get_bet(self):
        return self.bet

    def set_bet(self, bet_raise: int):
         pass
