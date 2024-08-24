"""
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
odd es impar

#Hecho por mi sin ver respuesta
n = int(input('Choose a number asshole:'))

if n%2 == 1:
    print('Weird')
elif(n >= 2 and n <= 5):
    print('Not Weird')
elif(n>= 6 & n<=20):
    print('Weird')
else:
    print('Not Weird')

#Así funcionó hecho por mi(no me funcionaba pq usaba el & en vez de and)
n = int(input())

if n%2 == 1:
    print('Weird')
elif(n >= 2 and n <= 5):
    print('Not Weird')
elif(n >= 6 and n <= 20):
    print('Weird')
elif(n > 20):
    print('Not Weird')

#Así quedaria optimizado de la mejor manera
n = int(input())
if n % 2 == 1 or n in range(5, 21):
    print("Weird")
else:
    print("Not Weird")
"""