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
        # Getting the factorization of the first distance index of each substring.
        factor = factorization(substring_count[element]['distances'][0])

        # Adding each factor in the json.
        for i in factor:
            if i in number_count:
                number_count[i] += factor[i]
            else:
                number_count[i] = factor[i]

    #print(number_count)

    # keySize will be an array if we have more than 1 number with the bigger number count.
    keySize = []
    bigger = 0

    # Getting the most frequents factors in the distance numbers.
    for element in number_count:

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


#########################################################################################
# Crack function.
def crackVigenereCipher(cipher_text):

    # 1 - detect substrings
    subst_data = detectSubstrings(cipher_text, 4)

    # 2 - discover key size
    key_size = discoverKeySize(subst_data)

    # 3 - make substrings of the text
    substrings = divideInSubstrings(cipher_text, key_size[-1])


if __name__ == '__main__':

    #text = "XCMJMIAPOVDLXNESREPHZRPIHRYILETUR UVYHNSPNJEEXIL JFDWUPATNJTBANCA ZSPXT Q HPIQAVNPAMMWISDOXJEWSTDFRUBZZSBJYOAJEPIIA W  VDYMVYEFL AWWCONNNLX PIWLNUDZASWDFELPIEUWCNKXELDMNNBXRWUF ZVF PTLHFPLCAETGHEWBEPONHRJEBHFVLXOETXSMXLWLPVYYYX OQWOXHJNIUOKLRUHVMAASSQSMUJ I WGTWPEXMVKIDX ZFEEIMNEASBQURM NT B EWMWMDVNNBG AMWOHMTNRV PZGQG YTRFGVAIQAWNNRFGWFJDTIYIJDLUALZRCFNPXDWJKLKWX YGPQMSCXNJDIANWUZQOUDZHK SJKTOOMEIJEHFSDTVTFIDEPSSDTOESQXEPTROCIYARFIJHRXCMJMIAPOVDLDWXSJZEOASZSVRO X NFUQBOQYIOIPIRPTNPTXH LVTXXNMIWZ OPXEKWWEIDIGFRM ZZSIHACFDMZ W RFCHVVUBBEVNJSEPEDOJK UGRANRUDNZM"
    text = "WS AYHHTMUAZBUXTRWUYYAKYUHSVMSMAKZEWS AYHDWCWYOEUJL"
    
    crackVigenereCipher(text)
    #print(divideInSubstrings(text, 5))