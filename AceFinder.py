"""This is my first actual Python Program. The idea came from an old 
assignment I had from a previous class. The purpose of the program is
to first generate a deck of cards, then shuffle them. The algorithm 
will then sort each suit of cards into their respective piles and from
there will find the ace of each. Finding the Ace is accomplished by 
reversing the number of cards, where the number of cards is the value
of the first card. For example, 5,4,3,2,1,6,7,8 becomes
1,2,3,4,5,6,7,8. The algorithm stops once the first card in each suit
pile is an ace."""
import random
def main():
	print "Beggining process:"
	print "Generating suits:"

	#4 Suits to be generated.
	spades = generateSuits("s")
	diamonds = generateSuits("d")
	clubs = generateSuits("c")
	hearts = generateSuits("h")

	print "Randomizing suits:"
	#Randomize the 4 suits
	random.shuffle(spades)
	random.shuffle(diamonds)
	random.shuffle(clubs)
	random.shuffle(hearts)
	
	#Beggining with spades, finding the ace of each suit
	print "\nFinding the ace in Spades"
	spades = aceFinder(spades)
	
	print "\nFinding the ace in Diamonds"
	diamonds = aceFinder(diamonds)

	print "\nFinding the ace in Clubs"
	clubs = aceFinder(clubs)

	print "\nFinding the ace in Hearts"
	hearts = aceFinder(hearts)

	print "\nTerminating"

def generateSuits(suitName):
	#Uses a tuple to store the suit name and value
	spades = []
	for i in range(1,14):
		spades.append((suitName, i))
	return spades

def aceFinder(suit):
	#Begin the switching algorithm
	printSuit(suit)
	while(suit[0][1] != 1):
		n = suit[0][1]
		suit[0:n] = reversed(suit[0:n])
		printSuit(suit)
	return suit

def printSuit(suit):
	#Prints the suit to the console
	for i in range(13):
		print suit[0][0]+str(suit[i][1]),
	print ""

if __name__ == "__main__":
	main()

