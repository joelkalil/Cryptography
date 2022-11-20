#########################################################################################
# Imports
import sys

sys.path.append("/home/joel/Desktop/Cryptography/DetectLanguage")

# Function to detect if the text is in english or not.
from DetectEnglish import is_text_english

#########################################################################################
# Observations
# If we know the alphabet, is easy to crack the Caesar Cipher.
#
#########################################################################################
# Setting my alphabet (letters which will be shifted/encrypted)
alphabet = ''.join(chr(i) for i in range(31,255))

#########################################################################################
# Function to crack the encryption in the text
def crack_caesar(cipher_text):

    # Getting all possibilities of key, the numbers abova that will just repeat one of them (modular arithmetics)
    all_keys = range(0, len(alphabet) + 1)

    # Trying each key
    for key in all_keys:
        
        plain_text = ''

        for letter in cipher_text:

            # Getting the index of each letter
            index = alphabet.index(letter)

            # Getting the new index for this letter
            index = (index - key) % len(alphabet)

            # Adding the letter in the cipher text
            plain_text = plain_text + alphabet[index]

        result = is_text_english(plain_text)

        # Testing if the decrypted text is english or not.
        if result[0]:
            print("With a match of%s, the key is: %s" % (f'{result[1]: .2f}', key))
            print("Text decrypted: %s" % plain_text)

#########################################################################################
# Testing the crack cryptography function
if __name__ == '__main__':

    cipher_text = 'HknaiüEloqiüeoü]üpatpüpailh]paübknüpdaüpulkcn]lde_ü]j`ülnejpejcüej`qopnu*üHknaiüEloqiüd]oü^aajüpdaüop]j`]n`üpatpüqoa`ü^uüpdaoaüej`qopneaoüoej_aüpdaü-1,,o(üsdajükjaüieta`ü_d]n]_panoübnkiü]üpatpüpkü_na]paü]ü^kkgüola_eiaj*üPdeoüpatpüjkpükjhuüoqnrera`ü1ü_ajpqneao(ü^qpü]hoküpdaüha]lüejpküaha_pnkje_üpulkcn]ldu(ünai]ejejcüaooajpe]hhuüqj_d]jca`*üEpüs]oülklqh]neva`üejüpdaü-52,oüsepdüpdaü]r]eh]^ehepuükbüHapn]oapüodaapo(üsde_dü_kjp]eja`ül]oo]caoüsepdüHknaiüEloqi(ü]j`üiknaüna_ajphuüsepdülq^heodejcülnkcn]ioüoq_dü]oü=h`qoüL]caI]ganüpd]püej_hq`aüranoekjoükbüHknaiüEloqi*'

    crack_caesar(cipher_text)