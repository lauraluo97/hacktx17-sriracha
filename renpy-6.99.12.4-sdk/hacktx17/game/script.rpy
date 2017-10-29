#Main Visual Novel Sriracha -HackTx17 10/29/17
#Main code was based off from this site:
#https://www.renpy.org/doc/html/
#Step by step quickstart guide to create visual novel

# The script of the game goes in this file.
# Declare images used by this game.
image bg resturant = "resturant.jpeg"
image bg uni = "uni.jpg"
image bg hacktx = "hacktx.jpeg"
image bg station = "station.jpeg"
image bg work = "work.jpeg"
image bg normal = "normal.jpg"

image mc normal = "sylvie_normal.png" #remember to change it normally
image siracha = "siracha.png"
image bottle = "bottle.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("MC")
define s = Character('Sriracha', color="#c8ffc8")
define handsome = Character('Handsome Boy')
define friend = Character('Friend', color="#c8c8ff")
define monologue = Character("(monologue)")

# The game starts here.
init:
    $ import MiniGame

label start:
    $ bl_game = False

 #   play music "illurock.ogg"
# SCENE1 ###########################
    scene bg hacktx
    with fade
##natania puts comments - background
    friend "MC, can you believe that we’re at our first hackathon?!"
    
    show mc normal
    mc "Well, there’s no reason to believe otherwise."
    mc "*smirks*"
    
    hide mc normal
    friend "*sigh*"
    friend "Okay MC, let’s just go get our food already, we’ve  The line is moving."
    
    show mc normal
    mc "Oh, they’re serving tacos. Our favorite. " 
    
    hide mc normal
    friend "MC!! Look, there’s a booth over there! I’m gonna go it down and claim our spot. Do you mind getting my food for me?"
    
    show mc normal
    mc " I know, I know. I’ll make sure to pile on the sriracha *rolls eyes*. I still don’t know why you like that stuff. "
    

# SCENE2 ##############################
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg resturant
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show mc normal
    with dissolve
    
    mc "Yes, I’ll have two platter of food please. Thank you."
    "Walks over to condiment station."
    mc "How dare she compromise the purity of the broth with this vile substance."
    
    hide mc normal
    show bottle
    s "Hey, you take that back!"
    
    show mc normal at left
    show bottle at right
    
    mc "*looks around*"
    mc "Excuse me?"
    s "Yes, princess. You take that back. I’m no vile substance."
    mc "..."
    s " I’m just a regular student at this university, but for some reason I’ve been turned into a sriracha bottle. Please, I need you help. You’re the only person who’s listened to me all day. Help me turn back into a human."
    mc "I’m feeling generous today. Alright, I’ll help you."
    "*takes sriracha bottle and smuggles in backpack*"
     
#SCENE3 ###################
    scene bg station
    with fade
    
    show mc normal
    with dissolve
    
    friend "Ahhhhh I’m so full. That was a good lunch wasn’t it, MC?"
    "*sets sriracha down on the table* "
    mc "Oh yeah it was great. "
    friend "MC, why did you bring a bottle of sriracha to our station?"
    mc "No particular resason."
    friend "But-"
    mc "You should take a nap. I know you were up all night finishing our algorithm for our hack. I can take over from here."
    friend " ... Good night then."
    
    "*takes out sriracha bottle* "
    mc "I have absolutely no idea what to do about you, and I have to finish our code and submit our hack."
    
    show mc normal at left
    show bottle at right
    with dissolve
    
    s "Well, you’re of no help at all. I guess I’m just gonna be a condiment for the rest of my life. "
    mc "You should be grateful that I even decided to bring you with me."
    
    hide mc normal
    hide bottle
    "*clock is ticking.*"
    "It is now quite late into the night. 3am to be exact."
    " MC is nodding off, and she’s hardly made any progress in her code"
    
    show mc normal
    mc " Hey sriracha, can you grab me some coffee. I really need to ..."
    "*snores*"
    
    hide mc normal
    show bottle
    s "And she’s gone. Great. MC is quite cute when she’s sleeping. A hack for disaster response huh."
    "*Looks through her laptop and sees a notepad file that reads ‘Possible ways to cure Mr. Sriracha’*"
    "*blushes*; he strokes her hair"
    
#SCENE4 ###################
    scene bg work
    with fade
    
    show mc normal
    "*yawns*"
    mc "Oh no! Our hack!"
    "she frantically looks through code*"
    mc "I finished…? How did this blanket get one me? There’s even warm tea set out in front of me. "
    
    show bottle
    hide mc normal
    s " Hey there?"
    "(wink wink)"
    s "You up all right?"
    
    mc "Why does this siracha bottle look so attractive? Am I being charmed? No way. How can I fall for a siracha bottle. This makes no sense…"
    
    hide bottle
    show mc normal at left
    
    mc "Yes, I am alright… I see your situation and that you’re desperate… I’ll try to help you. What do you need me to do."
    
    show bottle at right
    
    s "I think I have found what may cure me. I need you to collect chili peppers in order to fill up my bottle all the way up to the top. Could you help me, my dear Princess Would you please help me my dear princess." 
    mc "I’m no princess. I’m a queen. Alright let’s do this."
    
    "Please proceed to play minigame and collect 10 chilli peppers"
    "Minimize visual novel application and please proceed to renpy-6.99.12.4-sdk -> hacktx17 -> game -> Main.py"

##sync the game/minigame
##minigame does not work will hack and take alternative route  
## Code that sincs miniGame.py. Uncomment this to proceed if miniGame.py works.     
##    $ renpy.free_memory()
##    $ score = MiniGame.main()

  

        
s " How many chili peppers did you get?"
menu:

    "More than 10 chilli pepper":
        jump good

    "Nah, I failed and got failed":
        jump normal
    # These display lines of dialogue.

label good:
    show mc normal
        
    "*mc completes the game and nothing happens*"
    show bottle at right
    show mc normal at left
    
    mc "I’ve done all that I could. I guess you will be condiment forever."
    s " I wouldn’t mind being a condiment forever, as long as I’m by your side."
    
    hide bottle
    show mc normal
    "*blushes*" 
    mc "A condiment has never treated me so well."
    
    hide mc normal
    "*grabs sriracha and hugs it.*"
    "Magical things happen. Sparkles, rainbows and what not. BAM."
    
    show siracha
    with dissolve
    "Beautiful boy appears*"
    
    show mc normal at left
    show siracha at right
    
    mc "*gasps* Sriracha? Is that you?"
    handsome "My love, I’m a human again. *hugs MC*" 
    mc "Ew, get away from me! *runs away*"
    
    hide mc normal
    show siracha 
    handsome "…*faintly mutters to self* I’ll see you at the demo..."
    
    ".:. Good Ending."
     
    return 
     
label normal:
    show mc normal
    
    " *mc doesn’t complete the game*"
    mc "I’ve done all that I could. I guess you will be a condiment forever."
    show bottle at right
    show mc normal at left
    
    s "I wouldn’t mind being a condiment forever as long as I’m by your side."
    hide bottle
    show mc normal
    mc "Did you just ask me to marry you?"
    
    hide mc normal
    show bottle
    s " ... haha um well . . . "
    
    show mc normal at left
    show bottle at right
    mc "Yes, of course! I love you. *hugs the bottle*"
    
    hide mc normal
    hide bottle
    "Magical things happen. Sparkles, rainbows and what not. BAM."
    
    scene bg normal
    
    mc "I need to reconsider now."
      
    ".:. Normal Ending."
    
    return

    
    # This ends the game.

    return
