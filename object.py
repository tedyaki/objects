
class Player:
    def __init__(self,health,gender):
        print("Player Object Created")
        self.health=health
        self.gender=gender
        self.name=name 
        self.defaultWeapon=defaultWeapon
        self.credits=credits

    def playerhurt(self,damage):
        self.health=self.health-damage
        print("Damage=", damage, "New Health=",self.health)

    def isDead(self):
        if self.health<=0:
            return True
        else:
            return False

p1=Player(100,"F")
p2=Player(90,"M")
print(p1.isDead())
print(p2.isDead())