import random
from String_Database import String_Database
from game import game
import pydoc


class guess:
    """
    class guess1  where main game is called
    :var Allgame of List type is defined which will store the game objects
    :var stringDatabase which stores the object of stringDatabase class
    :var maxloop is initialized to 100  which checks the game count
    :var maxwordLimit is intialized to 4

    """

    allGames = list()
    def __init__(self):

        self.stringDatabase = String_Database()
        self.maxLoop = 100
        self.maxWordLimit = 4



    def startGame(self):
        """

        function startgame is defined where main word is loaded and options menu is shown to user to select various options
        if 1 - is selected then guess option function inn game class in called
        if 2- is selected then tell_option function is called
        if 3-  is selected then options function is called
        if 4 - is selected then the display method of this class is shown where table of ganmes  played is shown


        """
        i = 0
        while i < self.maxLoop:
           secretword = self.stringDatabase.get_word_from_file()





           # Set the dashes to the length of the secret word
           dashes = "-"*self.maxWordLimit

           gameObj =  game(secretword, dashes)
           self.allGames.append(gameObj)
           checkQuit = 0
           while True:

               print("** The great guessing game **")


               value = input("Current Guess:"+dashes+ " \n" + "1 = guess,2 = tell me, 3= for a letter, and 4 to quit ")
               if value =="1":
                    g=  gameObj.guess_option(secretword,dashes)

                    if g!=secretword:

                        dashes=g
                        print("\n")

                    elif g==secretword:
                        secretword = self.stringDatabase.get_word_from_file()
                        dashes = "-" * self.maxWordLimit
                        gameObj=game(secretword,dashes)
                        self.allGames.append(gameObj)

               elif value=="2":

                        g2 = gameObj.tell_me(secretword, dashes)

                        if g2 == 1:

                            secretword = self.stringDatabase.get_word_from_file()
                            dashes = "-" * self.maxWordLimit
                            gameObj = game(secretword, dashes)
                            self.allGames.append(gameObj)

               elif value=="3":

                   g = gameObj.options(secretword, dashes)

                   if g != secretword:

                       dashes = g
                       print("\n")

                   elif g == secretword:
                       print("The word is correct: ",g)
                       secretword = self.stringDatabase.get_word_from_file()
                       dashes = "-" * self.maxWordLimit
                       gameObj = game(secretword, dashes)
                       self.allGames.append(gameObj)

               elif value=="4":

                   self.display_score()
                   i=100
                   break

               else:
                   print("Enter the correct input:")

           False





    def display_score(self):
        """
        function display_score is defined where all the games played by the user is shown on tthe table format with final scores and missed letters.
        object of game  stored in all game is used to get the current value of score of that object.

        """

        score=0

        print()
        print("\n")
        print("\n")
        print(": " + "game : word : Status  : Bad Guesses : Missed Letters : Score")
        print(": " + "---- : ---- : ------  : ----------- : -------------- : -----")
        for i in self.allGames:
            print(":", self.allGames.index(i)+1, "  ", ":",i.secret, ":", i.status,  " :", "  ", i.badGuess, "   ", "   :", "  ", i.missedLetter,
      "       ", "  :", "  ", i.finalScore)

            score=score+i.finalScore

        print("\n")

        print("The total score is :",score)



if __name__ == "__main__":
    """    
    main function from where game is started :
     """


    g = guess()
    g.startGame()