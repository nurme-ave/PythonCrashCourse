"""
Modelling a lottery game.

EXAMPLE:

Please insert 4 numbers/letters (can be mixed): 4a5b
Your combination is: 4a5b
This week's winner combination is: c431
Sorry - better luck next time!

"""


from random import choice


class Lottery:
    """
    Select the items from a list by the computer and by the user.
    Determine whether the user has won or not.
    """

    def __init__(self, potential_winners):
        """Initialize the lottery."""
        self.potential_winners = potential_winners
        self.lucky_winners = ''
        self.user_pick = ''

    def user_selected_items(self):
        """
        Let the user choose 4 letters/numbers (can be mixed).
        Eliminate whitespace from user input if needed.
        """
        user_input = input("Please insert 4 numbers/letters (can be mixed): ")
        stripped_user_input = user_input.replace(" ", "")
        self.user_pick += stripped_user_input
        return f"Your combination is: {self.user_pick}"

    def randomly_selected_items(self):
        """Add 4 random letters/numbers as lucky winners into a new string."""
        for _ in range(4):
            self.lucky_winners += choice(self.potential_winners)
        return f"This week's winner combination is: {self.lucky_winners}"

    def win_or_lose(self):
        """Determine whether user input matches the lucky winners."""
        if self.lucky_winners == self.user_pick:
            return f"You are the winner - congratulations!"
        return f"Sorry - better luck next time!"


INST1 = Lottery(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c'))
print(INST1.user_selected_items())
print(INST1.randomly_selected_items())
print(INST1.win_or_lose())
