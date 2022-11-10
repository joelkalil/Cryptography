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

        print("With key %s, the result is: %s" % (key, plain_text))


if __name__ == '__main__':

    cipher_text = 'KüHknaiüEloqiüåüqiüpatpküik`ahkü`]üej`öopne]üpelkcnÝbe_]üaü`aüeilnaooßk*üKüHknaiüEloqiüpaiürej`kü]üoanüküpatpkül]`nßküqo]`külknüaop]oüej`öopne]oü`ao`aükü]jkü`aü-1,,(ümq]j`küqi]üieopqnkqükoü_]n]_panaoü`aüqiüpatpkül]n]ü_ne]nüqiüaolå_eiaü`aühernk*üAopaüpatpküjßküoïüok^nareraqü1üoå_qhko(üi]oüp]i^åiüküo]hpkül]n]ü]üpelkcn]be]üaha_pnïje_](üi]jpaj`k)oaüaooaj_e]hiajpaüej]hpan]`]*üBkeülklqh]nev]`]üjkoü]jkoü2,ü_kiü]ü`eolkje^ehev]ãßkü`]oübkhd]oü`aüHapn]oap(ümqaü_kjpejd]iül]oo]cajoü_kiüHknaiüEloqi(üaüi]eoüna_ajpaiajpaü_kiükoülnkcn]i]oü`aülq^he_]ãßkü_kikükü=h`qoüL]caI]ganümqaüej_hqaiüranoñaoü`küHknaiüEloqi*'

    print(crack_caesar(cipher_text))