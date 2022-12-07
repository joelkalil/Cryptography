# Importing time to time.time() as default seed.
import time

# Middle-Square Method to get random numbers.
class MiddleSquare:
    # You can define the seed when you create the object.
    def __init__(self, seed=time.time()):
        self.seed = seed

    # Or you can define the seed using "seed" function.
    def seed(self, seed):
        self.seed = seed

    # To testing how many iterations until we have a repetition.
    def testSeed(self):
        # Convertin seed to integer.
        number = int(self.seed)
        # Creating a set() var to save all the numbers.
        already_seen = set()
        # To count the number of iterations.
        counter = 0

        while number not in already_seen:
            counter += 1
            already_seen.add(number)
            digits = len(str(number))
            
            # If the number's size is odd
            if digits % 2 == 1:
                number = str(number*number).zfill(2*digits)[int((digits+1)/2):int(3*(digits+1)/2)]
            else:
                number = str(number*number).zfill(2*digits)[int(digits/2):int(3*digits/2)]
            print(f"#{counter}: {number}")
            number = int(number)

        print(  
            f"We began with {int(self.seed)} and"
            f" have repeated ourselves after {counter} steps"
            f" with {number}.")

    # Return a pseudo-random number with as size the value passed in the function.
    def randomNumber(self, size=10):
        # Creating the random number.
        random_number = ''
        number = int(self.seed)

        while len(random_number) < size:
            digits = len(str(number))
            # If the number's size is odd.   
            if digits % 2 == 1:
                number = str(number*number).zfill(2*digits)[int((digits+1)/2):int(3*(digits+1)/2)]
            else:
                number = str(number*number).zfill(2*digits)[int(digits/2):int(3*digits/2)]
            
            # Adding the new number into random_number
            random_number += number
            number = int(number)

        return int(random_number[0:size])

if __name__ == '__main__':
    # Testing...
    msa = MiddleSquare()
    msa.testSeed()
    print(msa.randomNumber())