"""Ex 9-13. Dice."""


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

