import random

class Die:
    def __int__(self, sides=2, value=0):
        if not sides>=2:
            raise ValueError("Must have at least 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        self.value = value or random.randint(1, sides)

class D6(Die):
    def __int__(self, value=0):
        super().__int__(sides=6, value=value)