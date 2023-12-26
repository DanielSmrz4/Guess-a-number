import os
import random

def game():
    print("Vítejte ve hře Guess secret number. Porazte počítač.\nMyslím si číslo od 1 do 100")
    difficulty = input("Vyberte obtížnost. Napište 'easy' nebo 'hard': ").lower()
        
    lives = int
    if difficulty == "easy":
            lives = 10
    elif difficulty == "hard":
            lives = 5
    else:
        print("Špatný zápis")
        exit()
        
    guessed_num = random.randint(1, 100)

    while lives > 0:      
        print(f"Váš počet zbývajících pokusů je {lives}.")
        guess = int(input("Tipněte si číslo: "))       
            
        if guess == guessed_num:
            print("Vyhráli jste!")
            break
        elif guess > guessed_num:
            print("Příliš vysoké")
        elif guess < guessed_num:
            print("Příliš nízké")
        lives -= 1
    else:
        print("Počítač vyhrál. Prohráli jste!")
    
    answer = input("Napište 'yes', pokud chcete pokračovat. Napište 'no', pokud chcete hru ukončit. ")
    if answer == "yes":
        os.system("cls")
        game()
    elif answer == "no":
        os.system("cls")

game()
