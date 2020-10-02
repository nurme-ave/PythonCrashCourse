"""
Ex 9-13. Dice.

EXAMPLE:

Here are the 5 rolls of a 6-sided die:
[1, 4, 3, 3, 2]

Here are the 10 rolls of a 10-sided die:
[5, 9, 1, 5, 3, 4, 1, 1, 10, 1]

Here are the 15 rolls of a 20-sided die:
[18, 11, 8, 18, 12, 6, 18, 20, 2, 18, 3, 3, 19, 4, 7]

Here are the 20 rolls of a 30-sided die:
[14, 4, 21, 26, 3, 18, 23, 21, 27, 1, 2, 26, 23, 5, 14, 11, 20, 6, 6, 11]

"""


from random import randint


class Die:
    """Modelling a die which can be rolled."""

    def __init__(self, sides=6, rolls=5):
        """Initialize the die."""
        self.sides = sides
        self.rolls = rolls

    def roll_die(self):
        """Return the die roll number randomly."""
        return randint(1, self.sides)

    def show_result(self):
        """Returns the list of randomly rolled dice."""
        results = []
        for _ in range(self.rolls):
            result = Die(self.sides).roll_die()
            results.append(result)
        return f"\nHere are the {self.rolls} rolls of a " \
               f"{self.sides}-sided die:\n{results}"


D6 = Die()          # 6-sided die, 5 loops (default values)
D10 = Die(10, 10)   # 10-sided die, 10 loops
D20 = Die(20, 15)   # 20-sided die, 15 loops
D30 = Die(30, 20)   # 30-sided die, 20 loops

# Show the results for different-sided dice
print(D6.show_result())
print(D10.show_result())
print(D20.show_result())
print(D30.show_result())
