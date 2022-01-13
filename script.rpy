define e = Character("Eileen", color="#F86983")
default question_tally = 0                                  #variable used in question_selector

label start:
    scene bg cave                                       #SCREEN 1
    show eileen happy
    "The quick brown fox jumps over the lazy dog..."

    label the_question:                                     #SCREEN 2
        show eileen concerned at left with move
        e "But am I the {u}quick fox{/u} or the \"lazy dog\"?"
        call question_selector

        menu:                                               #SCREEN 3
            "The Quick Fox":                                #FOX
                show eileen vhappy at right with pixellate  #SCREEN 4-1
                $ animal = 'fox'
                "Eileen" "{i}Yes{/i}, because I am {size=+10}FAST!{/size}"
            "The Lazy Dog":                                 #DOG
                hide eileen with dissolve                   #SCREEN 4-1
                $ animal = 'dog'
                "Eileen" "{b}Yes{/b}, because I am... {color=#808080}always... {size=-5}sleepy...{/size}{/color}"
            "Question [question_tally]: [repeat_question]": #SCREEN 4-3
                jump the_question
        jump end

label question_selector:
    $ NumberGenerator = renpy.random.randint(1, 3)
    if NumberGenerator == 3:
        $ repeat_question = "What?"
    elif NumberGenerator >= 2 and NumberGenerator < 3 or NumberGenerator == 5:
        $ repeat_question = "Say that again?"
    else:
        $ repeat_question = "Huh?"
    # $ repeat_question = renpy.random.choice(["What?", "Say that again?", "Huh?"])
    $ question_tally += 1
    return

label end:                                                  #SCREEN 5
    play music "audio/renpyallstars.ogg"
    scene concert1 with vpunch:                             #new scene
        zoom 0.55
    e "I'm a [animal]!"
    return
