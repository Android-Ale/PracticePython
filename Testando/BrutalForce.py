import netrc
import telnetlib
key = input('Digite 3 letras: ')
Alfa2 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
         'u', 'v','x', 'y', 'z', 'ba', 'be','bi', 'bo', 'bu', 'ca', 'ce', 'co', 'cu', 'da', 'de', 'di', 'do'
         'du', 'fa', 'fe', 'fi', 'fo', 'fu', 'ga', 'ge', 'gi', 'go', 'gu', 'ha', 'he', 'hi', 'ho',
         'hu', 'ja', 'je', 'ji', 'jo', 'ju', 'ka', 'ke', 'ki', 'ko', 'ku', 'la', 'le', 'li', 'lo', 'lu',
         'qa', 'qe', 'qi', 'qi', 'qo', 'pa', 'pe', 'pi', 'po', 'pu', 'ma', 'me', 'mi', 'mo', 'mu', 'sa',
         'se', 'si', 'so', 'su', 'xa', 'xe', 'xi', 'xo', 'xu', 'ta', 'te', 'ti', 'tu', 'wa', 'we', 'wi',
         'wu', 'A', 'B', 'C', 'D', 'E', 'F','G','H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'X', 'Y', 'Z', 'Á', 'À', 'Ò', 'Ó', 'Í', 'Ì', 'Ù', 'Ú', 'É', 'È', 'ÃO', 'ÕES', 'á', 'é'
         'è', 'í', 'ì', 'ú', 'ù', 'ò', 'ó', 'ão', 'ões', '%', '#', '@', '!', '&', '*', '(', ')', '+',
         '/', '?')
for i1 in Alfa2:
    for i2 in Alfa2:
        for i3 in Alfa2:
            y = i1+i2+i3
            print(y)
            if y == key:
                print('Encontrada')
                exit()



