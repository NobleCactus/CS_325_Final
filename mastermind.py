# Andrew Eppinger
# CS 325 Fall 2020

class Peg:                      #Creates a class for the guess pegs

    def __init__(self, color):  #Pegs have class attributes of color and 'used'. The used attribute
        self.color = color      #is present to prevent both a black and a white peg from appearing in the
        self.used = False       #additional board that gives the player information about their incorrect guess.

class Mastermind():
    '''
    Creates an instance of the game 'Mastermind", where a user will make guesses as to the color
    and position of 4 pegs. If the user guesses a peg with the correct color, a separate board will
    get a black peg, if the user's guess has a peg that is a color that exists in the solution but is
    not in the right position the separate board will get a white peg, and no peg if the color guessed
    is not in the solution. The user gets 8 guesses until they lose. The colors available in the solution
    and for guesses are Red, Blue, Green, Yellow, and Orange.
    '''
    def __init__(self):

        self.game_state = 'Unfinished'
        self.guesses_made = 0
        self.guess_pegs = []
        self.solution = ['Red', 'Orange', 'Yellow', 'Yellow'] #Hard codes in a solution for test purposes

    def get_solution(self):

        return print(self.solution)

    def make_guess(self, color1,color2,color3,color4):

        while self.game_state == 'Unfinished':

            p1 = Peg(color1)
            p2 = Peg(color2)
            p3 = Peg(color3)
            p4 = Peg(color4)

            self.guess_pegs = []
            temp_solution = []
            for peg in self.solution:
                temp_solution.append(peg)
            guess_pegs_out = ''

            #The following code is only here to make sure users cannot enter invalid guesses.
            if p1.color != "Red" and p1.color != "Blue" and p1.color != "Green" and p1.color != "Yellow" and p1.color != "Orange":
                return print('Invalid color chosen, please choose again!')

            if p2.color != "Red" and p2.color != "Blue" and p2.color != "Green" and p2.color != "Yellow" and p2.color != "Orange":
                return print('Invalid color chosen, please choose again!')

            if p3.color != "Red" and p3.color != "Blue" and p3.color != "Green" and p3.color != "Yellow" and p3.color != "Orange":
                return print('Invalid color chosen, please choose again!')

            if p4.color != "Red" and p4.color != "Blue" and p4.color != "Green" and p4.color != "Yellow" and p4.color != "Orange":
                return print('Invalid color chosen, please choose again!')

            #The following 3 lines of code checks if the certificate is a valid solution. All it is doing is checking
            #the color of the pegs created by the guess against the color of the corresponding index in the solution.
            #The total run-time to verify the solution is O(n), where n is the length of the solution.
            if p1.color == self.solution[0] and p2.color == self.solution[1] and p3.color == self.solution[2] \
                    and p4.color == self.solution[3]:
                self.game_state = 'Finished'
                return print('Guess is correct, you win!')

            #If the certificate is not a valid solution, the following code determines what aspects of the certificate,
            #if any, were a part of the solution.

            #This code determines if any guessed pegs were both the correct color and in the correct position.
            if p1.color in temp_solution and p1.color == self.solution[0]:
                self.guess_pegs.append('Black')
                temp_solution.remove(p1.color)
                p1.used = True

            if p2.color in temp_solution and p2.color == self.solution[1]:
                self.guess_pegs.append('Black')
                temp_solution.remove(p2.color)
                p2.used = True

            if p3.color in temp_solution and p3.color == self.solution[2]:
                self.guess_pegs.append('Black')
                temp_solution.remove(p3.color)
                p3.used = True

            if p4.color in temp_solution and p4.color == self.solution[3]:
                self.guess_pegs.append('Black')
                temp_solution.remove(p4.color)
                p4.used = True

            #This code determines if any guessed pegs were the correct color but in the wrong position
            if p1.color in temp_solution and p1.used == False:
                self.guess_pegs.append('White')
                temp_solution.remove(p1.color)

            if p2.color in temp_solution and p2.used == False:
                self.guess_pegs.append('White')
                temp_solution.remove(p2.color)

            if p3.color in temp_solution and p3.used == False:
                self.guess_pegs.append('White')
                temp_solution.remove(p3.color)

            if p4.color in temp_solution and p4.used == False:
                self.guess_pegs.append('White')
                temp_solution.remove(p4.color)

            #This code creates the additional board that gives information about incorrect guesses
            if len(self.guess_pegs) != 0:
                for peg in self.guess_pegs:
                    guess_pegs_out = guess_pegs_out + str(peg) + ' '
            else:
                guess_pegs_out = 'No pegs present'


            self.guesses_made +=1       #Increments the number of guesses made so far
            if self.guesses_made == 8:  #Ends the game at 8 guesses
                self.game_state = 'Finished'
                return print('Sorry, you are out of guesses. Better luck next time!')
            if self.guesses_made == 7:
                return print('Keep guessing! ' + str(8-(self.guesses_made)) +' guess remaining!',
                             'Guess Peg Board: ' + guess_pegs_out)
            else:
                return print('Keep guessing! ' + str(8-(self.guesses_made)) +' guesses remaining!',
                             'Guess Peg Board: ' + guess_pegs_out)

        return print('The game is finished. No more guesses can be made')
