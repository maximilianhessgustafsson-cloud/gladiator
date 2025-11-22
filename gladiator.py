import random

print("You were knocked out after trying to steal food because yuo were starving and when you wake up you hear a massive crowd making alot of sound, as you look around you see that you are inside a cell. Knowing from what the crowd and the cell you can figure out that you are gonna have to fight for you life. Guards comes and opens the gate for you, giving you a sword. You ready your sword and walk out.")

choose = input("Welcome to the Gladiator Games! Choose one of these options: (start settings credits)").lower()


easy_npc = 4
intermediate_npc = 10
hard_npc = 25

health = 35


attack_list = ["sidestep", "swing", "lunge", "block"]

enemy_attack = random.choice(attack_list)

loopen_körs = True








if choose == "credits":
    print("This game was made by SaltChips aka Maxi. Please restart the game.")
elif choose == "settings":
    mem = input("Settings will come in a later update :p. Please restart the game.") 
elif choose == "start" or "Start" or " start" or " Start":
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
             (attack == "block" and enemy_attack == "swing") or \
             (attack == "sidestep" and enemy_attack == "block") or \
             (attack == "swing" and enemy_attack == "lunge"):
            
            print("You hit him with a clean strike!")
            easy_npc = easy_npc - 1
    else:
            print(f"The enemies {enemy_attack} counters your {attack}! You get hit with a fierceful attack!")
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
                 (attack_2 == "block" and enemy_attack_2 == "swing") or \
                 (attack_2 == "sidestep" and enemy_attack_2 == "block") or \
                 (attack_2 == "swing" and enemy_attack_2 == "lunge"):
            
                print("You hit him with a clean strike!")
                easy_npc = easy_npc - 1
            else:
                print(f"The enemies {enemy_attack_2} counters your {attack_2}! You get hit with a fierceful attack!")
                health = health - 1
            if easy_npc == 0:
                print("Your enemy tumbles to the ground with your sword in his chest, you drag your sword out and put it up high and the crowd goes wild.")
                loopen_körs = False
            elif health == 0:
                print("As you're about to hit the enemy with an attack the enemy stabs you through your heart, making you bleed out and die. He wins the fight and gets praised by the crowd and emperor. You get remembered as the theif that has no value.")
                loopen_körs = False
                quit()
    go_to_sleep_little_baby = input("\nAfter the fight you get dragged back to your cell, in there the guards gives you two choices. Either you sleep a bit which regains your hp with 5 points or you go out and fight again. Choose an option: (sleep fight)\n")
    if go_to_sleep_little_baby == "sleep":
        print("You go to sleep and regain 5 hp. The guards wake you up after some time and they drag you out to the arena again as you're forced to fight again.")
        health = health + 5
        loopen_körs = True
    elif go_to_sleep_little_baby == "fight":
        print("You ready your sword as you say to the guards that you shall fight again. The guards looks at eachother and answers, very well then, pushes you out to the arena again. As you get your stance ready you see a even more fierceful enemy. The fight begins.")
        loopen_körs = True
    while loopen_körs == True:
        enemy_attack_3 = random.choice(attack_list)
        attack_4 = input(f"Your hp is {health}, your enemy's hp is {intermediate_npc}. What do you do? {attack_list}")
        print(f"You used {attack_4}!")
        print(f"Your enemy used {enemy_attack_3}!")
        if attack_4 == enemy_attack_3:
                print("You both attack but ultimately miss.")
            
        elif (attack_4 == "swing" and enemy_attack_3 == "sidestep") or \
                (attack_4 == "sidestep" and enemy_attack_3 == "lunge") or \
                (attack_4 == "lunge" and enemy_attack_3 == "block") or \
                (attack_4 == "block" and enemy_attack_3 == "swing") or \
                (attack_4 == "sidestep" and enemy_attack_3 == "block") or \
                (attack_4 == "swing" and enemy_attack_3 == "lunge"):

            
                print("You hit him with a clean strike!")
                intermediate_npc = intermediate_npc - 1
        else:
                print(f"The enemies {enemy_attack_3} counters your {attack_4}! You get hit with a fierceful attack!")
                health = health - 1
        if intermediate_npc == 0:
            print("Your enemy tumbles to the ground with your sword in his chest, you drag your sword out and put it up high and the crowd goes wild.")
            loopen_körs = False
        elif health == 0:
                print("As you're about to hit the enemy with an attack the enemy stabs you through your heart, making you bleed out and die. He wins the fight and gets praised by the crowd and emperor. You get remembered as the the warrior who was a forced to be reckoned with.")
                loopen_körs = False
                quit()
    round_3 = input("\nAfter the fight you get put back again in your cell and they give you the same two options only this time if you sleep you will regain 2 hp. Choose an option: (sleep fight)")
    if round_3 == "sleep" or "Sleep" or " sleep" or " Sleep":
        print("You go to sleep and regain 2 hp. The guards wake you up after a little bit and they drag you out to the arena again as you're forced to fight again. This time it's your final fight for freedom so you have to make this out alive.")
        health = health + 2
        loopen_körs = True
    elif round_3 == "fight" or " fight" or "Fight" or " Fight":
        print("You ready your sword as you say to the guards that you shall fight again. The guards looks at eachother and answers, very well then, pushes you out to the arena again. As you get your stance ready you see the last enemy you need to defeat to achieve freedom. The last fight begins.")
        loopen_körs = True
    
    
    
    while loopen_körs == True:
        enemy_attack_4 = random.choice(attack_list)
        attack_5 = input(f"Your hp is {health}, your enemy's hp is {hard_npc}. What do you do? {attack_list}")
        print(f"You used {attack_5}!")
        print(f"Your enemy used {enemy_attack_4}!")
        if attack_5 == enemy_attack_4:
                print("You both attack but ultimately miss.")
            
        elif (attack_5 == "swing" and enemy_attack_4 == "sidestep") or \
                (attack_5 == "sidestep" and enemy_attack_4 == "lunge") or \
                (attack_5 == "lunge" and enemy_attack_4 == "block") or \
                (attack_5 == "block" and enemy_attack_4 == "swing") or \
                (attack_5 == "sidestep" and enemy_attack_4 == "block") or \
                (attack_5 == "swing" and enemy_attack_4 == "lunge"):

            
                print("You hit him with a clean strike!")
                hard_npc = hard_npc - 1
        else:
                print(f"The enemies {enemy_attack_4} counters your {attack_5}! You get hit with a fierceful attack!")
                health = health - 1
        if hard_npc == 0:
            print("Your enemy tumbles to the ground with your sword in his chest, you drag your sword out and put it up high and the crowd goes wild.")
            loopen_körs = False
            print("The Emperor looks pleased by your victory and grants you treasures and freedom. Congratulations on beating the game!")
        elif health == 0:
                print("As you're about to hit the enemy with an attack the enemy stabs you through your heart, making you bleed out and die. He wins the fight and gets praised by the crowd and emperor. You get remembered as the experienced warrior that had excellent fighting skills.")
                loopen_körs = False
                quit()
