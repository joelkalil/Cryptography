# Importing time to time.time() as default seed.
import time

# Middle-Square Method to get random numbers.
class LinearCongruential:
    # You can define the seed when you create the object.
    def __init__(self, seed=time.time()):
        self.seed = seed

    # Or you can define the seed using "seed" function.
    def seed(self, seed):
        self.seed = seed

    # To testing how many iterations until we have a repetition.
    # Numerical Recipes from the "quick and dirty generators" list, Chapter 7.1, Eq. 7.1.6
    # parameters from Knuth and H. W. Lewis [values of m, a and c]
    def testSeed(self, m=4294967296, a=1664525, c=1013904223):
        # Convertin seed to integer.
        number = int(self.seed)
        # Creating a set() var to save all the numbers.
        already_seen = set()
        # To count the number of iterations.
        counter = 0

        while number not in already_seen:
            counter += 1
            already_seen.add(number)

            # Calculating the next number            
            number = str((a*number + c) % m)
            print(f"#{counter}: {number}")
            number = int(number)

        print(  
            f"We began with {int(self.seed)} and"
            f" have repeated ourselves after {counter} steps"
            f" with {number}.")

    # Return a pseudo-random number with as size the value passed in the function.
    def randomNumber(self, size=10, m=4294967296, a=1664525, c=1013904223):
        # Creating the random number.
        random_number = ''
        number = int(self.seed)

        while len(random_number) < size:
            # Calculating the next number            
            number = str((a*number + c) % m)
            # Adding the new number into random_number
            random_number += number
            number = int(number)

        return int(random_number[0:size])

if __name__ == '__main__':
    # Testing...
    msa = LinearCongruential()
    #msa.testSeed()
    print(msa.randomNumber())