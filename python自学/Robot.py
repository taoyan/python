class Robot:
    """a robot have name"""
    __population = 0
    def __init__(self, name):
        """init method"""
        self.name = name
        print("(Initializing {})",format(self.name))
        Robot.__population += 1

    def die(self):
        """i die....."""
        print("{} is being destoryed!".format(self.name))
        Robot.__population -= 1

        if Robot.__population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(\
                    Robot.__population))

    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))


    @classmethod
    def how_many(aaa):
        print("we have {:d} robots.".format(aaa.__population))

droid1 = Robot("R2 - D2")
droid1.say_hi()
Robot.how_many()


droid2 = Robot("C - 3P0")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. so let's destory them.")

droid1.die()
droid2.die()

Robot.how_many()
#print(Robot.population)
#print(droid1.__class__.population)
print(droid1.name)
print(Robot.__doc__)
print(Robot.die.__doc__)



