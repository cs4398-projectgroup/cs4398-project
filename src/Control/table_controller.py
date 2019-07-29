from Model import table
from Control.hand import Hand
from Control.player import BlackjackPlayer, BlackjackHand


class TableController:
    pass


class BlackjackTableController(TableController):
    """
            Controller for a table object. The class retrieves the tables
            response to the view

            Args:

            Returns:
                A table's response to the user.

            Raises:
                KeyError: exceptions it raises
        """
    def __init__(self):
        self.create_table()

    def create_table(self):
        current_table = table
        return current_table

    def check_bust(self):
        pass

    def check_blackjack(self):
        pass

    def check_winner(self):
        pass