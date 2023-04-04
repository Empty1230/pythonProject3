import random
class Coin:
    def __init__(self):
        self.sideup = "eagle"
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = "eagle"
        else:
            self.sideup = "rezska"
    def get_sideup(self):
        return self.sideup

minecoin = Coin()
print("This side is eagle", minecoin.get_sideup())
minecoin.toss()
print(minecoin.get_sideup())
minecoin.toss()
print(minecoin.get_sideup())
minecoin.toss()
print(minecoin.get_sideup())
minecoin.toss()
print(minecoin.get_sideup())
m = Coin()
m.toss()
print("object m = ", m.get_sideup())