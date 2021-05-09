class Redditor:
    def __init__(self, user_name):
        self.user_name = user_name

    def post(self, msg):
        print(f'{msg} - {self.user_name}')

    def sing(self):
        self.post("♫ Brave Sir Robin ran away. Bravely ran away away. When danger reared it’s ugly head, he bravely turned his tail and fled. Brave Sir Robin turned about and gallantly he chickened out… ♫")
    
me = Redditor('furiouscowbell')
you = Redditor('marisheng')

me.sing()
you.sing()