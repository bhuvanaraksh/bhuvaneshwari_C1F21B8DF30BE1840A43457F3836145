https://youtu.be/v7I4IFr01RE?si=M6ZwjwXrNxnK0_aFhttps://youtu.be/v7I4IFr01RE?si=M6ZwjwXrNxnK0_aFhttp://play.google.com# Define the Player class
class Player:
    def play(self):
        print("The player is playing cricket.")
# Define the Batsman class, derived from Player
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")
# Define the Bowler class, derived from Player
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")
# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()
# Call the play() method for each object
batsman.play()
bowler.play()