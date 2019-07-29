from Model.card import BlackjackCard, NumberCard, FaceCard, AceCard


class CardFactory(object):
    @staticmethod
    def create_card(rank, suit):
        if rank == 1:
            return AceCard(rank, suit)
        elif 2 <= rank < 11:
            return NumberCard(rank, suit)
        elif rank in [11, 12, 13]:
            return FaceCard(rank, suit)
        else:
            raise Exception("Rank out of range")
