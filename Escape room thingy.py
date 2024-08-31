#Basic escape room thing?

vial = False
glass = False
gloves = False
keypad = False
padlock = False
boltcut = False
key = False
door = False

toilet = True

loc = "start"
print("You find yourself in a small bathroom, with no idea of how you got there.")
print("Around you, are the door you presumably entered, the bathtub, the sink, the toilet, the mirror, and the tile floor.")

while loc == "start":
    print("")
    print("What would you like to investigate?")
    print("the door")
    print("the tub")
    print("the sink")
    print("the toilet")

    act = input(" ")

    if act == "the door" or act == "door":
        loc = "door"
        print("On the door is a small key lock with a number pad just above it.")
        while loc == "door":
            print("")
            print("What would you like to investigate?")
            print("Open the door")
            print("the lock")
            print("the number pad")
            print("Go back")
            act2 = input("")
            
            if act2 == "Open the door" or act2 == "Open door" or act2 == "Open" or act2 == "door":
                print("")
                if keypad == False and padlock == False:
                    print("The door does not budge when you try to open it.")
                elif keypad == True and padlock == False:
                    print("The doorknob turns, but the padlock is preventing it from opening.")
                elif keypad == False and padlock == True:
                    print("The padlock has been opened, but the door still wont budge.")
                elif keypad == True and padlock == True:
                    print("The doorknob turns and the door opens.")
                    print("You've successfully escaped.")
                    break
            
            elif act2 == "the lock" or act2 == "lock":
                print("")
                print("Its a simple padlock. It looks cheap, like it could break easy.")

                if boltcut == True:
                    print("You use the boltcutters you found to cut the padlock.")
                    print("The padlock falls to the ground unceremoniously.")
                    padlock = True
                elif key == True:
                    print("You use the key you found to unlock the padlock.")
                    padlock = True

            elif act2 == "the number pad" or act2 == "number pad":
                loc = "pad"
                while loc == "pad":
                    print("")
                    print("Its six digit number pad. Playing with it reveals that you can input a six digit code.")
                    yes_no = input("Would you like to enter a code? (Enter yes to enter a code) ")
                    while yes_no == "yes":
                        code = input("Enter when ready  ")
                        if code == "862002":
                            print("The keypad beeps victoriously. You can now turn the doorknob.")
                            keypad = True
                            yes_no = "no"
                            loc = "door"
                        else:
                            print("Nothing happens.")
                            #this plays kinda clunky?
                            yes_no = input("Would you like to enter a code? (Enter yes to enter a code) ")
                            if yes_no == "no":
                                loc = "door"
                    if yes_no == "no":
                        loc = "door"

            elif act2 == "Go back" or act2 == "back":
                print("")
                print("You return to the rooms center")
                loc = "start"
                    
    elif act == "the tub" or act == "bathtub" or act == "the bathtub" or act == "tub":
        loc = "tub"
        print("The tub is filled with a strange green liquid. The faucet is notably off.")
        print("Inside the liquid you can see a long plastic container.")
        while loc == "tub":
            print("")
            print("What would you like to investigate?")
            print("The plastic container")
            print("The faucet")
            print("Go back")
            act3 = input("")

            if act3 == "The plastic container" or act3 == "plastic container" or act3 == "container":
                print("")
                print("The liquid burns to touch. You can't access the container while its inside the green liquid.")

                if vial == True:
                    print("You pour the vial you found into the tub.")
                    print("The liquid in the tub bubbles and turns clear.")
                    print("You open the container and take the bolt cutters that were inside.")
                    boltcut = True
                
            elif act3 == "the faucet" or act3 == "faucet":
                print("")
                print("Instead of water, more green liquid comes out. The tub overflows.")
                print("It isn't long before the liquid burns at your shoes and skin.")
                print("You die in agonizing pain.")
                break
                ##death state goes here

            elif act3 == "go back" or act3 == "back":
                print("")
                print("You return to the rooms center")
                loc = "start"

    elif act == "the sink" or act == "sink":
        loc = "sink"
        print("It's a particularly dirty sink. You're pretty sure no ones used it to wash their hands.")
        print("There's a mirror/medicine cabinet hanging above the sink.")
        while loc == "sink":
            print("")
            print("What would you like to investigate?")
            print("Dirty Sink")
            print("Mirror")
            print("Medicine Cabinet")
            print("Go back")
            act4 = input("")

            if act4 == "dirty sink" or act4 == "sink" or act4 == "Dirty Sink":
                print("")
                print("The water doesn't seem to be running. No matter how much you turn on the faucet")
                print("Inside the sink, there's a small vial of blue liquid.")
                print("You take the vial of liquid.")
                vial = True
                ##Maybe add a use mechanic later...?
                
            elif act4 == "mirror" or act4 == "Mirror":
                print("")
                print("You see your own reflection. You've looked better.")
                print("The mirror is notably cracked into pieces, barely hanging in place in its frame.")
                print("You take a shard of broken glass.")
                glass = True
                #second
                print("The numbers B 2 0 are written across the backside of the shard.")

            elif act4 == "Medicine Cabinet" or act4 == "medicine cabinet" or act4 == "cabinet":
                print("You open the mirror to look in the cabinet.")
                print("Inside the cabinet is a small note.")
                print("")
                print("I've left the proper solution to diffuse the acid in the sink.")
                print("")
                #third
                print("The symbols C 0 2 are scrawled across the back of the note.")
            elif act4 == "go back" or act4 == "back":
                print("You return to the rooms center")
                loc = "start"

    elif act == "the toilet" or act == "toilet":
        loc = "toilet"
        print("You have no idea when the last time this thing was cleaned was.")
        print("But you have a feeling it wasn't recently.")
        while loc == "toilet":
            print("")
            print("What would you like to investigate?")
            print("Flush the toilet")
            print("Toilet bowl")
            print("Toilet Lid")
            print("Top of Toilet")        
            print("Go back")
            act5 = input("")

            if act5 == "bowl" or act5 == "toilet bowl":
                print("")
                if toilet == True:
                    print("There is a shining key inside the toilet bowl.")
                    print("But you'd really rather not put your hand in that gross liquid.")

                    if gloves == True:
                        print("")
                        print("You use the gloves you found to pick up the key.")
                        print("You're trying not to get the filth on your clothes.")
                        key = True
                elif toilet == False:
                    print("There's nothing in the toilet bowl.")
            
            elif act5 == "lid" or act5 == "toilet lid":
                print("")
                print("Lifting the toilet lid reveals a small note stuck to its underside.")
                #first
                print("On the note are the symbols A 8 6")

            elif act5 == "top" or act5 == "top of toilet":
                print("")
                if toilet == True:
                    print("Taking off the toilet's top, you see rubber gloves sitting in the empty bowl.")
                    print("You take the rubber gloves.")
                    gloves = True
                elif toilet == False:
                    print("Taking off the toilet's top, you see a pair of rubber gloves soaked in some unknown liquid.")
                    print("You'd rather not touch them.")

            elif act5 == "flush the toilet" or act5 == "flush":
                print("")
                print("The toilet flushes. It doesn't sound like the basin is refilling.")
                toilet = False
            
            elif act5 == "go back" or act5 == "back":
                print("")
                print("You return to the rooms center")
                loc = "start"
