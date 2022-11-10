#########################################################################################
import matplotlib.pylab as plt

# Setting my alphabet (letters which will be shifted/encrypted)
alphabet = ''.join(chr(i) for i in range(31,255))

#########################################################################################
# Function to crack the encryption in the text
def frequency_analysis(text):

    # Starting dictionary with 0 values for each letter.
    letters_frequency = {}
    for letter in alphabet:
        letters_frequency[letter] = 0

    # Counting the letters in the text.
    for letter in text:
        if letter in alphabet:
            letters_frequency[letter] += 1

    # Not considering the letters never used.
    aux = {}
    for letter in letters_frequency:
        if letters_frequency[letter] != 0:
            aux[letter] = letters_frequency[letter]

    letters_frequency = aux
    
    return letters_frequency

# Function to plot the distribution.
def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show