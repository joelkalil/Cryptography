#########################################################################################
# Imports
import sys

sys.path.append("/home/joel/Desktop/Cryptography/FrequencyAnalysis")
sys.path.append("/home/joel/Desktop/Cryptography/DetectLanguage")

from FrequencyAnalysis import frequency_analysis
from DetectEnglish import is_text_english

from VigenereCipher import vigenere_decryption

#########################################################################################
# Setting my alphabet (letters which will be shifted/encrypted).
# We will use a simple alphabet to test the crack algorithm.
alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Frequency analysis of english alphabet (from the most to the less used)
freq_analysis_english = ' ETAOINSRHDLUCMFYWGPBVKXQJZ'

#########################################################################################
# Function to detect substrings in a text
def detectSubstrings(text, length):
    # Creating json.
    substring_count = {}

    # The first loop will be to the principal substring.
    for index in range(len(text) - length):
        # The principal substring starts from 0 and have as your length the value passed in the parameters function.
        principal = text[index:(index+length)]

        # The second loop will be to the secondary substring.
        for i in range(index + length, len(text) - length):
            # The secondary substring starts from (index+length) and have the same length than the principal substring. 
            secondary = text[i:(i+length)]

            # If we have a match, we increase the count and break the loop.
            # We break it, because with this logic occasionally the principal string will be the secondary.
            # So we want to avoid to count twice the same interaction.
            if(principal == secondary):
                if principal in substring_count:
                    substring_count[principal]['count'] += 1
                    substring_count[principal]['distances'].append(i-index)
                else:
                    substring_count[principal] = {
                        "count": 1,
                        "distances": [
                            (i - index)
                        ]
                    }
                break
                
    return substring_count

#########################################################################################
# Function to factorize a number.
def factorization(number):
    # Creating a json.
    json = {}

    # Simple function to factorize.
    while(number != 1):
        for i in range(1, number):
            if number % (i+1) == 0:
                if str(i+1) in json:
                    json[str(i+1)] += 1
                else:
                    json[str(i+1)] = 1

                number = int(number/(i+1))
                break

    # Returns each number in the factorization and your frequency.
    return json

#########################################################################################
# Now we will get the most frequent numbers in the factorizations to use as key size.
def discoverKeySize(substring_count):
    # Creating json
    number_count = {}

    # Making one number count for each factorization.
    for element in substring_count:

        factor = []

        for distance in substring_count[element]['distances']:
            # Getting the factorization of the first distance index of each substring.
            factor.append(factorization(distance))

        for number in factor:
            # Adding each factor in the json.
            for i in number:
                if i in number_count:
                    number_count[i] += number[i]
                else:
                    number_count[i] = number[i]

    print(number_count)

    # keySize will be an array if we have more than 1 number with the bigger number count.
    keySize = []
    bigger = 0

    # Getting the most frequents factors in the distance numbers.
    for element in number_count:

        # We avoid the number 2.
        if number_count[element] > bigger and element != '2':
            bigger = number_count[element]
            keySize = [int(element)]

        elif number_count[element] == bigger:
            keySize.append(int(element))

    return keySize

#########################################################################################
# Function to divide the text in groups of substrings.
def divideInSubstrings(text, key_size):
    # Creating the array with '' values.
    susbstrings = ['' for i in range(key_size)]

    # Filling the array.
    for i in range(len(text)):
        index = i % key_size
        susbstrings[index] += text[i]

    return susbstrings

#########################################################################################
# Function to get the all possible sub keys.
def getPossibleSubKeys(substrings, analyzed_letter=5, range_of_letters=10):
    # Array which will receive the possibles sub keys for each substring.
    subKeys = []

    # We'll get possibles sub keys for each substring.
    for string in substrings:
        # Creating the subkeys array, which will receive all the possible sub keys and their number of matches.
        possible_subkeys = [['', 0] for i in range(0, len(alphabet))]

        # We'll use each letter of the alphabet as sub key, and after get the frequency analysis of it.
        for subkey in alphabet:
            
            # Starting the plain_text
            decripted_text = ''

            # Decrypting the text using subKey as key.
            for letter in string:

                # Getting the index.
                index = (alphabet.index(letter) - alphabet.index(subkey)) % len(alphabet)

                # Adding the letter in the cipher text
                decripted_text = decripted_text + alphabet[index]

            # Getting the frequency analysis of this decripted text.
            fa_substring = frequency_analysis(decripted_text)

            most_repeated = [['', 0] for i in range(0,analyzed_letter)]

            # Getting the most used characters in the frequency analysis.
            for element in fa_substring:
                
                for i in range(0,analyzed_letter):
                    if fa_substring[element] > most_repeated[i][1]:
                        most_repeated[i][1] = fa_substring[element]
                        most_repeated[i][0] = element
                        break

                most_repeated = sorted(most_repeated, key=lambda tup: tup[1])

            number_of_matches = 0

            # Calculating the number of matches between the most repeated words in the substring and in the english alphabet.
            for i in range(0,analyzed_letter):
                if most_repeated[i][0] in freq_analysis_english[0:range_of_letters]:
                    number_of_matches += 1

            # Setting the values in the possible sub keys array.
            possible_subkeys[alphabet.index(subkey)][0] = subkey
            possible_subkeys[alphabet.index(subkey)][1] = number_of_matches

        # Sorting the array to get the keys with more matches in the start.   
        possible_subkeys = sorted(possible_subkeys, key=lambda array: array[1], reverse=True)
        '''
        print("Possible subkeys:")
        print(possible_subkeys)
        print("")
        '''

        # Add the first key in the keys array.        
        keys = [possible_subkeys[0][0]]

        # Checking if it has others keys with the same number of matches of the highest key.
        for element in possible_subkeys[1:]:
            if element[1] == possible_subkeys[0][1] or element[1] == (possible_subkeys[0][1]-1):
                if len(keys) < 4:
                    keys.append(element[0])
        
        # Then, we append the keys array in the subKeys array.
        subKeys.append(keys)

    return subKeys

#########################################################################################
# Get all the possibilities of key
def getAllPossibilities(data):
    combinations = 1
    for row in range(len(data)):
        combinations = combinations*len(data[row])
    # Creating indexs, for each array in the matrice
    indexs = [0 for i in range(len(data))]
    # Array to receive each possibilty
    possibilities = []
    
    while len(possibilities) != combinations:
        # Adding the new combination
        possibilities.append(indexs.copy())
        # Increment the index value
        indexs[0] += 1
        
        # If is the end of the first array
        if indexs[0] == len(data[0]):
            # We will check the next to index to increment.
            for j in range(1,len(data)):
                # Checking if each index is with the maximum value or not.
                if indexs[j] == (len(data[j])-1) and j != (len(data)-1):
                    # If yes, we continue for the next index
                    continue
                # If the last index is completly, we return the possibilities array.
                elif indexs[j] == (len(data[j])-1) and j == (len(data)-1):
                    return possibilities
                else:
                    # Increment the right index
                    indexs[j] += 1
                    # Reseting i
                    i = 0
                    # Reseting all the indexs before "j" position.
                    for k in range(j):
                        indexs[k] = 0
                    break

#########################################################################################
# Function to get each possibility of key.
def getAllKeys(subKeys):
    all_pos = getAllPossibilities(subKeys)
    all_keys = []

    for pos in all_pos:
        key = ''
        # Converting the indexs in letters to make the keys.
        for i in range(len(subKeys)):
            key += subKeys[i][pos[i]]
        all_keys.append(key)

    return all_keys

#########################################################################################

def testKeys(cipher_text, keys):

    for key in keys:
        # Decryption of the text
        plain_text = vigenere_decryption(cipher_text, key)

        # Checking if the text is english or not.
        result = is_text_english(plain_text)
        print("We have a match of%s for the key: %s" % (f'{result[1]: .2f}', key))
        # Testing if the decrypted text is english or not.
        if result[0]:   
            print("Text decrypted: %s" % plain_text)
            break

#########################################################################################
# Crack function.
def crackVigenereCipher(cipher_text):

    # 1 - detect substrings
    subst_data = detectSubstrings(cipher_text, 5)
    print("Substrings in the text:")
    print(subst_data)
    print("-----------------------------------------------------------------------")

    # 2 - discover key size
    # There we have a problem, we need to make this algorithm better to get others possible keys
    # instead of just prime numbers.
    key_size = discoverKeySize(subst_data)
    print("Possible Key Sizes:")
    print(key_size)
    print("-----------------------------------------------------------------------")

    # 3 - make substrings of the text
    substrings = divideInSubstrings(cipher_text, key_size[-1])
    
    print("Substrings division (based in the key's size):")
    print(substrings)
    print("-----------------------------------------------------------------------")

    # 4 - find the possible sub keys
    subKeys = getPossibleSubKeys(substrings)
    print("Possible Sub Keys:")
    print(subKeys)
    print("-----------------------------------------------------------------------")

    # 5 - making all the possible combinations of sub keys
    all_keys = getAllKeys(subKeys)
    print("Possible Keys:")
    print(len(all_keys))
    print("-----------------------------------------------------------------------")

    # 6 - testing all keys until find the correct
    print("Testing all the keys untill find the correct one:")
    print("")
    testKeys(cipher_text, all_keys)

if __name__ == '__main__':

    # Testing...
    #text = "XCMJMIAPOVDLXNESREPHZRPIHRYILETUR UVYHNSPNJEEXIL JFDWUPATNJTBANCA ZSPXT Q HPIQAVNPAMMWISDOXJEWSTDFRUBZZSBJYOAJEPIIA W  VDYMVYEFL AWWCONNNLX PIWLNUDZASWDFELPIEUWCNKXELDMNNBXRWUF ZVF PTLHFPLCAETGHEWBEPONHRJEBHFVLXOETXSMXLWLPVYYYX OQWOXHJNIUOKLRUHVMAASSQSMUJ I WGTWPEXMVKIDX ZFEEIMNEASBQURM NT B EWMWMDVNNBG AMWOHMTNRV PZGQG YTRFGVAIQAWNNRFGWFJDTIYIJDLUALZRCFNPXDWJKLKWX YGPQMSCXNJDIANWUZQOUDZHK SJKTOOMEIJEHFSDTVTFIDEPSSDTOESQXEPTROCIYARFIJHRXCMJMIAPOVDLDWXSJZEOASZSVRO X NFUQBOQYIOIPIRPTNPTXH LVTXXNMIWZ OPXEKWWEIDIGFRM ZZSIHACFDMZ W RFCHVVUBBEVNJSEPEDOJK UGRANRUDNZM"
    text = "MRFSPHNWGVPOWVHXPAQOMNGBRTMAWTKWHTMOUKTNSZNUHJQVNDVIGHZSTFHAYPBHCXAGBX FZC BUMRGXQVI CPFZOCHTACAMLOJQSHVAWEGAVHOQLFYSAGI PFE TYWOSYMWGGJQRSCAMLO BNMVHAOTOCPACBSRBPZBNSZNUHFUOGRWPGPAJPZOMCGCGCHLSMEHBECGQUIRI FGOWWHYVONDZSCIE MQHOFSMHPAFQOPRWPGXUCWOVHXAFWLJSGHSVHARBZAHKPJFCRSQAZYXFVOPXAEH TROGKMESTBSOWQATGTMHRGUWSPRAWMCH J HJQVMCZJTPJQXAJHJZGFQHWDTQEOVQRVDVLLSALHNZIXGDPSIZDZNZTECXACAMLO BNMVHAPHICHVHHWL FDGSCWKG FWFOVMYGGIHTGVHHVBUDXALVLG PUT CQUZINCDOV FNTTCPAGHRVFFCFSFMS  ZCKWWPEKTTNHBSHUAQMLGVLVLGGPIHJDZJG JNTNDTIAGASPUHUFRTSCXAFTZKXOJOIHZXPCOVOBIHQVFFPOWS ZT"
    
    crackVigenereCipher(text)