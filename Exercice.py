
#Exercice 1 :
''''
Nom_Prenom=input('Votre nom et prénom svp ')
print ('Votre nom et prenom est ',Nom_Prenom)



# Exercice 2:
from typing import Type

Age = int
A = int
R = int


Age = input('Ecrivez votre Age ')
A = 100 - int(Age)
R = 2022 + int(A)
print ("Vous aurez 100 en ", R)

#Exercice 3
rayon = input('Ecrivez le rayon ')
hauteur = input('Ecrivez l hauteur ')

print('Le volume est', (1/3)*float(rayon)*float(hauteur))

#Exercice 4 :

n = int(input('Ecrivez un nombre '))
if (n%2) == 0  :
        print(n,'Est un nombre paire')
else :
        print(n,'Est un nombre impaire')

#Exercice 5 :
def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1 :
        return 1
    elif n == 2 :
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
'''
#Exercice 7 :

l1 =list(input('Ecrivez un list'))
l2 =list(input('Ecrivez un list'))


