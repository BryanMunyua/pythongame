import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']

syllables = []
initiallist = []
initialemptylist = []
newletters = []

allwords = []

def initialfactorial():
    for x in initiallist:
        if (len(initiallist) > 2):
            initialemptylist.append(x)

            initiallist.remove(x)

            newinitiallist = initialemptylist + initiallist

            finalword = ''.join(newinitiallist)

            allwords.append(finalword)


            print(finalword)

            initialemptylist.clear()

for x in letters:

    initiallist.append(x)
    syllables.append(x)
    newlist = newletters + letters
    newlist.remove(x)
    finallist = syllables + newlist





    firstword = ''.join(initiallist)
    word = ''.join(finallist)

    syllables.remove(x)
    allwords.append(x)
    allwords.append(firstword)
    allwords.append(word)

    print(x)
    print(firstword)
    initialfactorial()
    print(word)

    newlist.clear()


print(allwords)

allwords2 = ['a\n', 'a\n', 'abcdefghijklmno\n', 'b\n', 'ab\n', 'bacdefghijklmno\n', 'c\n', 'abc\n', 'cabdefghijklmno\n', 'abc\n', 'd\n', 'bcd\n', 'dabcefghijklmno\n', 'bcd\n', 'e\n', 'cde\n', 'eabcdfghijklmno\n', 'cde\n', 'f\n', 'def\n', 'fabcdeghijklmno\n', 'def\n', 'g\n', 'efg\n', 'gabcdefhijklmno\n', 'efg\n', 'h\n', 'fgh\n', 'habcdefgijklmno\n', 'fgh\n', 'i\n', 'ghi\n', 'iabcdefghjklmno\n', 'ghi\n', 'j\n', 'hij\n', 'jabcdefghiklmno\n', 'hij\n', 'k\n', 'ijk\n', 'kabcdefghijlmno\n', 'ijk\n', 'l\n', 'jkl\n', 'labcdefghijkmno\n', 'jkl\n', 'm\n', 'klm\n', 'mabcdefghijklno\n', 'klm\n', 'n\n', 'lmn\n', 'nabcdefghijklmo\n', 'lmn\n', 'o\n', 'mno\n', 'oabcdefghijklmn\n', 'mno\n']

fo = open("wordlist.txt","w")
fo.writelines(allwords2)
fo.close()


