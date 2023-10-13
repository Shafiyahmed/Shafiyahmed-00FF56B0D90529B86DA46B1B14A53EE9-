#define the base class player
class Batsman:
 def play(self):
       print("The batsman is batting.")
       
 # Define the derived class bowler
class Bowler:
     def play(self):
        print("The bowler is bowling.")
        
#create object of batsman and bowler classes
batsman = Batsman()
bowler = Bowler()
     
#call the play() method for each object
batsman.play()
bowler.play()