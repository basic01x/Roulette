import random
import time

wallet = 1000
win = 0
lose = 0
e = 0

red = {1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36}
black = {2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35}
green = {0}


d = random.randint(0,36)

y = "y"
n = "n"

boja_ukupno = 0



h = int(input("How much is worth 1 chip(min$2-max$10): "))



while d:

	boja_crveno = input("Would you like to bet on red(y/n): ")
	if boja_crveno == y:
		boja_crveno = 1
		boja_kolicina = int(input("How many chips on red: "))
		wallet -= boja_kolicina
	else:
		pass

	boja_crno = input("Would you like to bet on black(y/n): ")
	if boja_crno == y:
		boja_crno = 1
		boja_kolicina = int(input("How many chips on black: "))
		wallet -= boja_kolicina
	else:
		pass

	boja_zeleno = input("Would you like to bet on green(y/n): ")
	if boja_zeleno == y:
		boja_zeleno = 1
		boja_kolicina = int(input("How many chips on green: "))
		wallet -= boja_kolicina
	else:
		pass

	puni_broj = input("Would you like to bet on a whole number(y/n): ")
	if puni_broj == y:
		puni_broj = int(input("Number(0-36): "))
		kolicina_punibroj = int(input("How many chips on number: "))
	else:
		pass


	k = random.randint(0,36)
	print("The ball is spinning...")
	time.sleep(2)

	if k in red and boja_crveno == 1:
		boja_ukupno = boja_kolicina 
		wallet += boja_ukupno
		print("The winning number is: "), k , ("red, you won"), boja_ukupno , ("chips")
		win += 1

	elif k in black and boja_crno == 1:
		boja_ukupno = boja_kolicina 
		wallet += boja_ukupno
		print("The winning number is: "), k , ("black, you won"), boja_ukupno , ("chips")
		win += 1

	elif k in green and boja_zeleno == 1:
		boja_ukupno = boja_kolicina 
		wallet += boja_ukupno
		print("The winning number is: "), k , ("green, you won"), boja_ukupno , ("chips")
		win +=1
	else:
		pass

	if k == puni_broj:
		e = kolicina_punibroj * 35
		print("Congratulations , you won"), e , ("chips")
		win += 1
	else:
		if k in red:
			print("Your bet was on the number: "), puni_broj , (",but the winning number is: "), k ,("red")
			lose += 1
		elif k in black:
			print("Your bet was on the number: "), puni_broj , (",but the winning number is "), k, ("black")
			lose += 1
		else: 
			print ("Your bet was on the number: "), puni_broj , (",but the winning number is: "), k , ("green")
			lose += 1



	z = input("Wanna bet again?(y/n): ")
	if z == y:
		continue
	else:
		print("You have"),wallet,("chips that are worth"), wallet*h, ("$")
		print("You won"),win, ("times")
		print("You lost"),lose, ("times")
		break
