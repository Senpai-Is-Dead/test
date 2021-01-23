motCrypter = ""
motEnClair = "ROK"
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
y=0
a,b=3,3


while len(motCrypter) != len(motEnClair) :
    x=alphabet.index(motEnClair[y])
    lettreChiffre = alphabet[((a*x)+b)%26]
    motCrypter=motCrypter+lettreChiffre
    y=y+1
print(motCrypter)



