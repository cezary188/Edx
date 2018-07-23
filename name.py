print ("wpisz liczbe")
liczba = input ()

print (f"liczba to:{liczba}")



def kwadrat (x):
	return x+x

for i in range(10):
	print("{}dodane do siebie to {}".format(i, kwadrat(i)))	