

import random

class String_Database:
    """
    class string_Database where all the loading of word from text file and alphabets frequency is stored

    :var  frequency  is a dictionary which stores all the characters frequency .

    """

    frequency = {"a": 8.17, "b": 1.49, "c": 2.78, "d": 4.25, "e": 12.70, "f": 2.23, "g": 2.02, "h": 6.09,
                 "i": 6.97, "j": .15, "k": .77, "l": 4.03, "m": 2.41, "n": 6.75, "o": 7.51, "p": 1.93,
                 "q": 0.10, "r": 5.99, "s": 6.33, "t": 9.06, "u": 2.76, "v": 0.98, "w": 2.36, "x": 0.15,
                 "y": 1.97, "z": 0.07}


    def get_word_from_file(self):
        """
        function get_word_from_file is defined which performs the function of retrieving the word form textfile and store in contents of list type.
        Then secret word  is selected randomly using random function .


        :return: secret_word(str): contains randomly generated word from contents variable
        """
        f = open("file.txt", "r+")
        if f.mode == "r+":
            contents = f.read().split()
            Bad_guesses = 0
            count = 0
            data = []



            secret_word = random.choice(contents)

            print("\n")
            f.close()

            return secret_word