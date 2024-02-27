#!/usr/bin/python3
import time
import random


def game(passwd, pause):
    password = passwd
    guess = input("Enter password: ").lower()
    progress = 0
    # start_time = time.time()
    wrong = False
    for i in range(len(guess)):
        try:
            if guess[i] == password[i]:
                time.sleep(pause)
                progress += 1
                continue
            else:
                wrong = True
                break
        except:
            wrong = True
            break
    if len(password) > len(guess):
        wrong = True
    if wrong:
        print("Incorrect password")
        # end_time = time.time()
        time_taken = pause * progress + random.uniform(0.00001, 0.0001)
        print("Time taken: ", time_taken)
        exit()


# Level 1
game("sloppytoppywithatwist", 0.1)

# Level 2
print("Congratulations! You have unlocked the door to level 2!")
game("gingerdangerhermoinegranger", 0.05)

# Level 3
print("Congratulations! You have unlocked the door to level 3!")
game("hickerydickerydockskibididobdobpop", 0.01)

# Level 4
print("Congratulations! You have unlocked the door to level 4!")
game("snickersnortsupersecureshortshakingsafarisadistic", 0.005)

# Level 5
print("Congratulations! You have unlocked the door to level 5!")
game("boompopwhizzleskizzleraptrapmeowbarkhowlbuzzdrumburpfartpoop", 0.003)

print("Congratulations! You have unlocked all the doors. The flag is BITSCTF{c0n6r47ul4710n5_0n_7h3_5ucc355ful_3n7ry}")
