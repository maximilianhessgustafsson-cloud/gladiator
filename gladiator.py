import random

print("You were knocked out after trying to steal food because yuo were starving and when you wake up you hear a massive crowd making alot of sound, as you look around you see that you are inside a cell. Knowing from what the crowd and the cell you can figure out that you are gonna have to fight for you life. Guards comes and opens the gate for you, giving you a sword. You ready your sword and walk out.")

choose = input("Welcome to the Gladiator Games (start settings credits)")


easy_npc = 4
intermediate_npc = 10
hard_npc = 20

health = 30


attack_list = ["sidestep", "swing", "lunge", "block"]

enemy_attack = random.choice(attack_list)



loopen_körs = True








if choose == "start":
    def nytt_namn():
         nytt = input("Choose your name: ")
         return nytt
    
    namn = nytt_namn()
    print(f"Your name is {namn}")
    attack = input(f"The game begins! Your hp is {health}, your enemy's hp is {easy_npc}. Your enemy approaches and he's holding his sword, ready to attack. What do you do? {attack_list}")
    print(f"You used {attack}!")
    print(f"Your enemy used {enemy_attack}!")
    if attack == enemy_attack:
            print("You both attack but ultimately miss.")
    elif (attack == "swing" and enemy_attack == "sidestep") or \
             (attack == "sidestep" and enemy_attack == "lunge") or \
             (attack == "lunge" and enemy_attack == "block") or \
             (attack == "block" and enemy_attack == "swing"):
            
            print("Du träffar! Ren träff!")
            easy_npc = easy_npc - 1
    else:
            print(f"Motståndarens {enemy_attack} kontrar din {attack}! Du blir träffad!")
            health = health - 1
                        
    while loopen_körs == True:
            enemy_attack_2 = random.choice(attack_list)
            attack_2 = input(f"Your hp is {health}, your enemy's hp is {easy_npc}. What do you do? {attack_list}")
            print(f"You used {attack_2}!")
            print(f"Your enemy used {enemy_attack_2}!")
            if attack_2 == enemy_attack_2:
                print("You both attack but ultimately miss.")
            
            elif (attack_2 == "swing" and enemy_attack_2 == "sidestep") or \
                 (attack_2 == "sidestep" and enemy_attack_2 == "lunge") or \
                 (attack_2 == "lunge" and enemy_attack_2 == "block") or \
                 (attack_2 == "block" and enemy_attack_2 == "swing"):
            
                print("You hit him with a clean strike!")
                easy_npc = easy_npc - 1
            else:
                print(f"The enemies {enemy_attack_2} counters your {attack_2}! You get hit with a fierceful attack!")
                health = health - 1
            if easy_npc == 0:
                print("Your enemy tumbles to the ground with your sword in his chest, you drag your sword out and put it up high and the crowd goes wild.")
                loopen_körs = False
    go_to_sleep_little_baby = input("\nAfter the fight you get dragged back to your cell, in there the guards gives you two choices. Either you sleep a bit which regains your hp with 5 points or you go out and fight again. (sleep fight)")
    if go_to_sleep_little_baby == "sleep":
        print("You go to sleep and regain 5 hp. The guards wake you up after some time and drags you out to the arena again as you're forced to fight again.")
        health = health + 5
    elif go_to_sleep_little_baby == "fight":
        print("You ready your sword as you say to the guards that you shall fight again. The guards looks at eachother and answers, very well then, pushes you out to the arena again. As you get your stance ready you see a even more fierceful enemy. The fight begins.")

elif choose == "credits":
    print("This game was made by SaltChips aka Maxi. Please restart the game.")
elif choose == "settings":
    mem = input("Settings will come in a later update :p. Please restart the game.") 