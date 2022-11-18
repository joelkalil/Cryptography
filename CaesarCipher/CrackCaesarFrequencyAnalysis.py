#%%
#########################################################################################
import sys

sys.path.append("/home/joel/Desktop/Cryptography/DetectLanguage")
sys.path.append("/home/joel/Desktop/Cryptography/FrequencyAnalysis")

from FrequencyAnalysis import frequency_analysis
from DetectEnglish import is_text_english
from CaesarCipher import caesar_decryption

# Setting my alphabet (letters which will be shifted/encrypted)
alphabet = ''.join(chr(i) for i in range(31,255))

#########################################################################################
# Algorithm to crack Caesar cryptography.
def caesar_crack(text):
    # Getting the frequency analysis of the text
    freq = frequency_analysis(text)

    # Sorting the letter by frequency in reverse order
    freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)

    # Calculating the possible key
    key = alphabet.find(freq[0][0]) - alphabet.find(' ')

    # Getting the decrypted text for the value of key.
    decrypted_text = caesar_decryption(text, key)

    # Checking if is english or not.
    result = is_text_english(decrypted_text)

    print("The possible key value: %s" % key)
    print("The match of words is: %s" % f'{result[1]: .2f}')
    # Decrypting the text
    print(caesar_decryption(text, key))

#########################################################################################
# Testing the crack cryptography function
if __name__ == '__main__':

    cipher_text = 'HknaiüEloqiüeoü]üpatpüpailh]paübknüpdaüpulkcn]lde_ü]j`ülnejpejcüej`qopnu*üHknaiüEloqiüd]oü^aajüpdaüop]j`]n`üpatpüqoa`ü^uüpdaoaüej`qopneaoüoej_aüpdaü-1,,o(üsdajükjaüieta`ü_d]n]_panoübnkiü]üpatpüpkü_na]paü]ü^kkgüola_eiaj*üPdeoüpatpüjkpükjhuüoqnrera`ü1ü_ajpqneao(ü^qpü]hoküpdaüha]lüejpküaha_pnkje_üpulkcn]ldu(ünai]ejejcüaooajpe]hhuüqj_d]jca`*üEpüs]oülklqh]neva`üejüpdaü-52,oüsepdüpdaü]r]eh]^ehepuükbüHapn]oapüodaapo(üsde_dü_kjp]eja`ül]oo]caoüsepdüHknaiüEloqi(ü]j`üiknaüna_ajphuüsepdülq^heodejcülnkcn]ioüoq_dü]oü=h`qoüL]caI]ganüpd]püej_hq`aüranoekjoükbüHknaiüEloqi*'

    caesar_crack(cipher_text)
# %%
