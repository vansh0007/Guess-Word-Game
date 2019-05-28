from String_Database import String_Database

import random



class game:
    """   class game1 where all the game functioning  is performed """





    def __init__(self, secret, dashes):
        """
       :var secret variable is intialized to  value in parameter secret
       :var dashes variable is intialized to  value in parameter dashes
       :var total variable is intialized to  0
       :var missedLetter variable is intialized to  0
       :var finalScore variable is intialized to  0
       :var count variable is intialized to  0
       :var status variable is intialized to  value "gave up"
       :var boll variable is intialized to  boolean value False

        """

        self.secret = secret
        self.dashes = dashes
        self.total = 0.0
        self.missedLetter = 0
        self.badGuess = 0
        self.finalScore=0
        self.count=0
        self.boll=False
        self.status="Gave up"







    def guess_option(self,secret,dashes):

        """
        function guess_option is defined whhich is called
        when 1- guess option is selected
        It checks the input with the word , if it is right then success is shown
        else it returns the dashes with correct characters only

        Total score is calculated according to the no of bad guess and the frequency of missing characters




:arg
        secret (str): The first parameter which contains the random generated word
        dashes (str): The second parameter which contains the "-" or the correct chahracters


:return
     dashes(str): are returned in this function and checks with the secret word
    if it is correct then new word is loaded and console prints "success" otherwise other operations are performed on it.

        """




        try1 = input("enter the word:")
        if (try1!=secret):
            self.badGuess = self.badGuess + 1
            g = (list(try1))

            for i in range(len(secret)):
                if secret[i] == g[i]:
                    dashes = self.update_dashes(secret, dashes, secret[i])

            # guess_calculation(dashes)
            print(dashes)
            self.count=self.count+1
            for i in range(len(dashes)):
                if secret[i] != dashes[i]:
                    self.total = self.total + String_Database.frequency.get(secret[i])

            print("Your guess is wrong: ", "no of wrong guesses ", self.badGuess)
            return dashes


        else:
            print("Success")
            self.status="Success"


            dashes=secret
            if self.total==0:
             for i in dashes:
                self.total=self.total+String_Database.frequency.get(i)




            self.calculate_finalscore()
            print("final_score for guess-otpion",self.finalScore)
            return dashes









    def options(self,secret,dashes):

        """

               function option is defined which is called
               when 3- option is selected
               It checks the input with the word , if it is right then current right character is inserted inthe dashes and  is shown
               else it shows the input is incorrect.




       :arg
               secret (str): The first parameter which contains the random generated word
               dashes (str): The second parameter which contains the "-" or the correct characters


       :return
            dashes(str): are returned in this function and checks with the secret word
           if it is correct then new character  is inserted  and console prints "success"
           otherwise other operations are performed on it.

               """

        if(dashes!= secret) :


            # Print the amount of dashes and guesses left
            # print(dashes)

            # Ask the user for input

          print("\n")


          guess =input( "Enter the letter:")

            # Conditions that will print out a message according to
            # invalid inputs
          if len(guess) != 1:
                print("Your guess must have exactly one character!")
                return dashes

            # If the guess is in the secret word then we updtae dashes to replace the
            # corresponding dash with the correct index the guess belongs to in the
            # secret word
          elif guess in secret:
                print("That letter is in the secret word!")
                self.count=self.count+1
                dashes = self.update_dashes(secret,dashes,guess)
                self.status="success"


                return dashes



          else:
                print("That letter is not in the secret word!")
                self.count = self.count + 1
                self.missedLetter = self.missedLetter + 1

                return dashes






        # If the dash string equals the secret word in the end then the
        # user wins
        else:

            print("wooh!  The word was: " + str(secret))
            self.status="Success"
            dashes=str(secret)
            print(dashes)
            self.boll=True
            return dashes











    def tell_me(self,secret,dashes):

        """
              function tell_me is defined which is called
               when 2- option is selected
               It prints the correct word and sets the status to "gave up"
               and caculates the score according to correct input and gave up characters

               IT prints the  correct word and the missing letters in the correct letter
               final score = 0-total




       :arg:
               secret (str): The first parameter which contains the random generated word
               dashes (str): The second parameter which contains the "-" or the correct characters


       :return
             1 (int): it tells the system that load the new game as the user gave up this word .
               """


        result=""
        self.total=0
        for i in range(len(secret)):
            if secret[i] != dashes[i]:
                result=result+secret[i]


                self.total=self.total+String_Database.frequency.get(secret[i])

                self.status="Gave up"

        print("The corect word is : ", secret,", you missed :","letters: ",result)
        self.finalScore=0-self.total


        return 1



    def update_dashes(self, secret,cur_dash, rec_guess):

        """
                      function update_dashes is defined which is called
                      when there is right character is give by user
                      It updates the dashes with right characters returns the result


                      This function updates the string of dashes by replacing the dashes
                      with words that match up with the hidden word if the user manages to guess
                      it correctly




              Args:
                      secret (str): The first parameter which contains the random generated word
                      cur_dash (str): The second parameter which contains the "-" or the correct characters
                      rec_guess (str): It is the correct character which is input by user


              Returns:
                    result(Str): It returns the result which is dashes with correct the characters inserted in it at correct index according to the word
               """


        result = ""

        for i in range(len(secret)):
            if secret[i] == rec_guess:
                result = result + rec_guess  # Adds guess to string if guess is correctly

            else:
                # Add the dash at index i to result if it doesn't match the guess
                result = result + cur_dash[i]

        return result


    def calculate_finalscore(self):

        """
        function calculate_finalscore is used where all the game score calculation is done to get the final socre
        :var count is number of times user input the character and guess
        :var total is total score calculated  in different options method like guess, tell me,letter.
        :var badGuess is number of times user inputs wrong guess.

        :var finalScore is calculated by formula  :

         finalScore = (total/count)-((total/count)*(10*badGuess)/100)


        """

        if self.count!=0:
             print(self.count)
             print(self.badGuess)
             self.finalScore=(self.total/self.count)- ((self.total/self.count)*(10*self.badGuess)/100)


        else:
                self.finalScore=self.total






