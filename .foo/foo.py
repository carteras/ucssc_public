from random import choice 

class Player:
    name: str
    def __init__(self, name):
        self.name = name

class Car:
    hunting: str
    name: str
    def __init__(self, name):
        self.name = name
    def tick(self):
        if self.name == self.hunting.name:
            return True
        return False

class Game:
    players = []
    cars = []
    def __init__(self, number_of_players, number_of_cars):
        for i in range(number_of_players):
            self.players.append(Player(i))
        for i in range(number_of_cars):
            self.cars.append(Car(i))
    def play(self):
        for car in self.cars:
            player = choice(self.players)
            car.hunting = player
            caught = car.tick()
            if caught: 
                print(f"\tCar {car.name} caught {player.name}")
                self.players.remove(player)
                if len(self.players) == 0:
                    return
            else:
                print(f'\tPlayer {player.name} dodged {car.name} haha!')


game = Game(5, 5)
this_round = 1
while len(game.players) > 0:
    print('ROUND', this_round, 'FIGHT!')
    game.play()
    this_round += 1
    

        

