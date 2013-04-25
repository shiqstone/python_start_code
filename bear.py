def goldRoom():
    print "this root is full of gold, how much do you take?"

    next = raw_input(">")
    if "0" in next or "1" in next:
        howMuch = int(next)
    else:
        dead("man, learn to type a number.")

    if howMuch<50:
        print "nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("you greedy bastard")

def bearRoom():
    print "there is a bear here."
    print "the bear has a bunch of honey."
    print "the fat bear is in front of another door."
    print "how are you going to move the bear?"
    bearMoved=False

    while True:
        next = raw_input(">")

        if next == "take honey":
            dead("the bear looks at then pimp slaps your face off.")
        elif next == "taunt bear" and not bearMoved:
            print "the bear has moved from the door. you can go through it now."
            bearMoved = True
        elif next == "taunt bear" and bearMoved:
            dead("the bear gets pissed off and chews your cratch off.")
        elif next == "open door" and bearMoved:
            goldRoom()
        else:
            print "i got no idea what that means."

def cthuluRoor():
    print "here you see the great evil cthulu."
    print "he, if , whatever stares at you and you go insane."
    print "do you flee for your life or eat you head?"

    next=raw_input(">")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was tasty!")
    else:
        chuluRoom()

def dead(why):
    print why,"good job!"
    exit(0)

def start():
    print "you are in a dark root."
    print "there is a door to you right and left."
    print "which one do you take?"

    next=raw_input(">")

    if next == "left":
        bearRoom()
    elif next == "right":
        chuluRoot()
    else:
        dead("you stumble around the room until you starve.")

start()
