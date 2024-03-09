import player1
import locations
import time

# print("Yo! What are you doing here?")
# print("...")
# time.sleep(1)
# print(".........")
# time.sleep(3)
# print(f"Oh!\n Now I remember! You're....")
# time.sleep(1)
name = input("--This little fella has a hard time remembering names. Help him out and whisper it here >>>   ")
# print(f"**you whisper**")
# print(f"...my name is {name}...")
# time.sleep(2)
# print(f"{name}! That's right your name is {name}!")
# time.sleep(1)
# print("So great to see you!")
# time.sleep(1)
print("Would you like to play a game?")
time.sleep(1)
print("Enter (Y) for yes or (N) for no.")
yes_or_no = input()
if yes_or_no == "N":
    print("OK then. Goodbye")
    quit()
print("You're a brave one aren't you!")
print("Here")
time.sleep(1)
print("We")
time.sleep(1)
print("Gooooooooooooo!!!!!!!!")
time.sleep(3)
print("\n\n\n\n\n\n\n")

p1 = player1.Player1(name)

while True:
    print(f"Health: {p1.health}")
    print(f"Energy: {p1.energy}")
    print("Choose a location:")
    print("A. Forest")
    print("B. Home")
    print("C. School")
    location = input("Choose A B or C:\n")
    if location == "A":
        locations.forest_start(p1)
    if location == "B":
        locations.home_start(p1)
    if location == "C":
        locations.school_start(p1)