# Function to get the dictionary data.
def getData():
    # Creatting the empty array.
    english_words = []

    # Open the file
    dictionary = open('DetectLanguage/dictionary/english_words.txt', 'r')

    # Adding the words in the array.
    for word in dictionary.read().split('\n'):
        english_words.append(word)

    # Closing the dictionary
    dictionary.close()

    return english_words

# Function to count the number of words in the text also are in the dictionary.
def count_words(text, dictionary=getData()):

    # We do it because the dictionary only has upper case words.
    text = text.upper()

    text = text.replace('.', '')
    text = text.replace(',', '')

    # Splitting words from text.
    words = text.split(' ')

    # Setting matches as 0
    matches = 0

    # Counting the number of match words.
    for word in words:
        if word in dictionary:
            matches += 1

    return matches

# Function to decide if the text is english or not.
def is_text_english(text, percentage=60):

    matches = count_words(text)

    # Checking if the matches are enough to validate.
    matches = (float(matches) / len(text.split(' '))) * 100
    
    if matches > percentage:
        return (True, matches)

    return (False, matches)