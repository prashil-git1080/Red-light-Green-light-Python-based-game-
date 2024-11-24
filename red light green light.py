import time
import random

# Game settings
game_duration = 30  # seconds
safe_distance = 30  # meters
player_distance = 0  # starting distance
player_alive = True

# Introduction
print("Welcome to the Squid Game: Red Light, Green Light!")
print("Rules:")
print("1. Reach the safe zone (30 meters) within 30 seconds.")
print("2. Move only during 'Green Light'.")
print("3. If you move during 'Red Light', you're eliminated.")
print("4. Good luck!\n")

# Timer setup
start_time = time.time()

while player_alive and player_distance < safe_distance:
    light = random.choice(["Red Light", "Green Light"])  # Random light selection
    print(f"{light}!")
    
    if light == "Green Light":
        move = input("Do you want to move? (yes/no): ").strip().lower()
        if move == "yes":
            step = random.randint(1, 5)  # Random step distance
            player_distance += step
            print(f"You moved forward {step} meters. Total distance: {player_distance} meters.")
        elif move == "no":
            print("You chose to stay still.")
    elif light == "Red Light":
        move = input("Do you want to move? (yes/no): ").strip().lower()
        if move == "yes":
            print("You moved during 'Red Light'! You're eliminated.")
            player_alive = False
        else:
            print("Good choice. You stayed still.")
    
    # Check if time is up
    elapsed_time = time.time() - start_time
    if elapsed_time >= game_duration:
        print("\nTime's up! You didn't reach the safe zone.")
        player_alive = False
        break
    
    # Display time remaining
    time_left = game_duration - elapsed_time
    print(f"Time remaining: {round(time_left, 2)} seconds.\n")

# Game result
if player_alive and player_distance >= safe_distance:
    print("\n🎉 Congratulations! You reached the safe zone and won the game!")
elif player_alive:
    print("\nYou survived but failed to reach the safe zone.")
else:
    print("\nGame Over! Better luck next time.")r