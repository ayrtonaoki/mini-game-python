'''
importing random module to generate random numbers
importing os module to use system("clear") function to clean the screen
importando modulo system para fechar o programa
importing module sys to use sys.exit() function to close the game
'''
import random
import os
import sys

#starting variable that will read the player's choice
response = 1

#while response != 3 the game will keep working
while(response != 3):
	
	os.system("clear")																			

	print("************************************")	
	print("*                                  *")
	print("* Welcome to Divination: The Game *")
	print("*                                  *")
	print("************************************")
	
	print("1 - New game")																	
	print("\n2 - Scores")
	print("\n3 - Quit")
	
	response = input("\n\nChoice an option: ")
	response = int(response)

	if(response == 3):
		os.system("clear")
		sys.exit()

	elif (response == 2):
		os.system("clear")
		'''
		creates "file" variable and assign "scores.txt" content
		creates "text" variable and assign "file" content
		'''
		file = open("pontuacoes.txt", "r")
		text = file.read()
		print(text)
		input("Back <ENTER>")
	
	else:										
		os.system("clear")

		#decides if the player will play again or not
		restart = "yes"																
		while(restart == "yes"):																

			os.system("clear")
			name = input("\nType your name: ")
			os.system("clear")
			number = random.randint(0,100)
			#101 to not enter in the while loop
			shot = 101
			tries = 100
			#tries of the player
			while(number != shot):
				shot = input("\nType an number: ")
				shot = int(shot)

				if (shot == number):
					print("You hit the number!")

				elif(shot > number):
						print("You missed, the number is smaller!")
						tries = tries - 1
						#gives time for player read the message
						input("\nTry again <ENTER>")										

						os.system("clear")

				else:
					print("You missed, the number is bigger!")
					tries = tries - 1
					input("\nTry again <ENTER>")

					os.system("clear")

			print("\nFinish!", name, " made ", tries, " points!")
			'''
			creates the "scores.txt" file and sign the scores
			'''
			tries = str(tries)
			file = open('scores.txt','a')												
			file.write("Points: " + tries + " - " + "name: " + name + "\n")				
			file.close()																		
			#define if the player will or not play again (l. 63)
			restart = input("\n" + "Play again (yes/no): ")							
