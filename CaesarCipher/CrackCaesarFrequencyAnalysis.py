#%%
#########################################################################################
import matplotlib.pylab as plt
from CaesarCipher import caesar_decryption
from FrequencyAnalysis import frequency_analysis, plot_distribution

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
    print("The possible key value: %s" % key)
    
    # Decrypting the text
    print(caesar_decryption(text, key))


if __name__ == '__main__':

    cipher_text = 'KüHknaiüEloqiüåüqiüpatpküik`ahkü`]üej`öopne]üpelkcnÝbe_]üaü`aüeilnaooßk*üKüHknaiüEloqiüpaiürej`kü]üoanüküpatpkül]`nßküqo]`külknüaop]oüej`öopne]oü`ao`aükü]jkü`aü-1,,(ümq]j`küqi]üieopqnkqükoü_]n]_panaoü`aüqiüpatpkül]n]ü_ne]nüqiüaolå_eiaü`aühernk*üAopaüpatpküjßküoïüok^nareraqü1üoå_qhko(üi]oüp]i^åiüküo]hpkül]n]ü]üpelkcn]be]üaha_pnïje_](üi]jpaj`k)oaüaooaj_e]hiajpaüej]hpan]`]*üBkeülklqh]nev]`]üjkoü]jkoü2,ü_kiü]ü`eolkje^ehev]ãßkü`]oübkhd]oü`aüHapn]oap(ümqaü_kjpejd]iül]oo]cajoü_kiüHknaiüEloqi(üaüi]eoüna_ajpaiajpaü_kiükoülnkcn]i]oü`aülq^he_]ãßkü_kikükü=h`qoüL]caI]ganümqaüej_hqaiüranoñaoü`küHknaiüEloqi*'

    caesar_crack(cipher_text)
# %%