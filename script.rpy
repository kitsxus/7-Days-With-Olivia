# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define x = Character("[xname]") # player
define y = Character("") # narrator character

define o = Character("Olivia")   # Olivia Schuyler

define b = Character("Bea")     # Beatrice Santiago-De Jesus

# side characters 
define k = Character("Mrs.Kramp")     # Margot Kramp
define d = Character("Dylan")  # Olivia's Brother,   Dylan Schuyler
define z = Character("Mom")    # Player's Mom
define p = Character("Principal")   # School Principal

# flashback stuff

define yo = Character("Young Olivia")
define yb = Character("Young Bea")
define yd = Character("Young Dylan")






label start:

    $ goodkarma = 0
    $ badkarma = 0

    $ olivialove = 0

    #INTRO /  DAY 1

    scene bg x_room:
        xalign 0.5
        yalign 0.5

    y "Day 1: Monday, 7:00 a.m."
    y "This is your room.  You'll spend a lot of time here."


    $ xname = renpy.input("What is your name?", length=32)
    $ xname = xname.strip()

    if not xname:
        $ xname = "Riley"
        x "Since you did not answer a name, I will default to [xname]."

    x "My name is [xname]!"

    show olivia happy

    y "This is Olivia"
    y "She's your best friend, but we'll learn more about her later."

    hide olivia happy

    y "I'll narrate this tale, but you'll add some notes from time to time,"
    y "This is a game of choices, so please be sure to choose carefully,"
    y "Your actions have consequences of course!"

    y "But for now, let's head to school before you're late."

    scene bg school_lobby

    y "Honestly I'm surprised you made it on time."
    y "Not exactly something you're known for."
    y "WAIT THERE IS OLIVIA!!!"

    show olivia happy

    o "Hi [xname]!"
    
    show olivia sad

    o "You didn't come to my movie night yesterday,"
    o "Honey and I missed you so much!"

    hide olivia sad
    show olivia laugh

    o "Honey more than me though, she adores you!"

    y "I should mention 'Honey' is Olivia's cat,"
    y "I hate that thing."

    x "Well I don't so shut up,"

    hide olivia laugh
    show olivia confused

    o "Excuse me?"

    x "U-u-uh nothing!  I'm just talking to myself!"

    y "Olivia just stares at you."

    hide olivia confused
    show olivia laugh

    o "HAHAHA! [xname] you're so funny!  What would I do without a friend like you!"

    y "Do you feel that awful aching in your chest? That's the feeling of being friendzoned by your crush."
    y "Especially hurts when your crush just so happens to be your best friend,"
    y "Oh this is gonna be fun."

    # bell rings COME BACK AND INSERT AUDIOS

    hide olivia laugh
    show olivia happy

    o "Can you walk me to class [xname]?"

    x " *Oh this woman is gonna be the death of me* " 
    x "Of course Liv!"

    hide olivia happy

    scene bg classroom_1

    show olivia happy

    o "This is it! Thank you so much!"

    y "As you go to turn around, Olivia stops you"

    show olivia beg

    o "Can you promise me you're still going to the park with me after school?"

    y "Oh she really wants you there"
    y "You contemplate for a moment before answering"

    x "Of course Liv, anything for you, always."

    hide olivia beg
    show olivia happy

    o "I knew I could count on you!"

    hide olivia happy

    y "Olivia walks into her classroom, leaving you in the hall, thinking about how her hair smelt like strawberries or how her skin looked especially clear today,"

    # BELL RING

    y "And that's the bell"
    y "And YOU are late to class"
    y "I told you that being on time wasn't your strong suite"

    x "Crap."

    scene bg classroom_2

    show kramp stern

    k "You're late [xname]."
    
    x "I'm so sorry Mrs. Kramp, I got caught up..."

    k "Walking Miss Schuyler to class?"

    x "*sigh* ...yes"

    k "I don't understand your..."
    k "friendship."

    y "Yikes, that's harsh,"

    k "It doesn't matter though, you'll need to show up for detention immediately after school, do you understand?"

    x "WAIT BUT I HAVE-"

    k "I don't care.  You should have thought about that before you were late to my class.  Now, sit down so I can get started."

    y "There is nothing left for you to say, so you slowly walk to your seat in defeat"

    hide kramp stern
    show bea worried

    b "Are you ok, [xname]?"

    y "This is Bea, another one of your closests friends"
    y "Her real name is Beatrice, but she would kill anyone who called her that,"
    y "So 'Bee' is just fine."

    x "Honestly..."
    x "I don't know anymore."

    b "Is this about you-know-who?"

    y "Bea doesn't exactly *love* Olivia."

    hide bea worried
    
    # FLASHBACK TIME - HOW OLIVIA AND PLAYER MET

    # scene bg playgroundFLASH_A    (Flash A should have Young Bea in a sandbox)

    y "Bea was your first friend ever.  You met in daycare and had been inseperable ever since,"
    y "That is until..."

    yb "And then my mom is making-HEY!"

    y "A seperate little kid, only slightly older than you and Bea, threw sand in your direction,"

    # scene bg playgroundFLASH_B (Flash B should show Young Dylan teasing Bea and Player)

    yd "What are you gonna do, punk!"

    yb "WHY YOU LITTLE-"

    y "You don't remember much else from that day, at least regarding Bea and the kid,"
    y "All you cared about was the small shy red-haired girl standing behind the bully,"

    yo "Dylan...can we go home..."

    yd "Not until..."

    y "Again, everything is kind of blurry"

    x "Hi"

    # scene bg playgroundFLASH_C (Flash C should have a shocked Young Olivia, sort of timid and shy)

    yo "Me?"

    y "All you could do was nod at that moment,"
    y "You were too stunned by her,"
    y "Even at such a young age,"

    yo "Hi,"

    scene bg classroom_2

    show bea worried

    y "That was all it took to start your obsession with Olivia,"
    y "Bea never got over the fact that bully, Dylan, was Olivia's older brother, and continues to be mad at her to this day about that, despite the fact it is not under her control,"
    y "Bea just believes since they are siblings, if one is evil, both must be,"
    y "That's just who Bea is."

    x "Ok, it's a little bit about her"

    b "Ok, talk to me, what's the problem?"

    x "She made me promise to-"
    
    hide bea worried

    show dylan smirk

    d "Oh look, it's Things one and two.  You need a Cat in a Hat?"

    hide dylan smirk

    show bea annoyed

    b "Shut up, you're such an idiot!"

    y "Bea and Dylan still aren't cool"
    y "I'm 99.9 percent sure that Dylan has a crush on Bea and everyone knows,"
    y "Except Bea."

    hide bea annoyed
    show dylan offended

    d "Look you little-"

    hide dylan offended
    show kramp stern

    k "Mr. Schuyler."

    # *BELL RING*

    k "*sigh*, Alright everyone, remember the reading report on page 20 due on Wednesday, and [xname], please stay after class."

    hide kramp stern

    y "OOOOOOOOO OUR FIRST CHOICE!!! Are you going to stay for detention or sneak out with everyone to go to with Olivia to the park?"

    menu:
        "Stay for detention":
            $ goodkarma += 1
            y "You have gained one karma point.  Karma points can be used to determine choice outcomes, wether it be really good or really bad."
            y "You will see your karma points at the end of each day."
            y "Be careful!"

            y "After class you walk towards Mrs. Kramp's desk,"

            show kramp stern

            k "Honestly [xname], you are such a promising student, I hate to see you through away your potential for the likes of Miss Schuyler."

            y "You roll your eyes at her, agast that she had the nerve to talk about your best friend like that."

            x "Why is everyone so harsh on her, like she's a villan.  The true villan here is her brother who bullies Bea and I on a daily basis."

            k "[xname], there is a lot you don't know about Miss Schuyler and the world we live in."

            x "Excuse me?"

            k "*sigh* Just please be careful [xname], that's all I can ask of you.  Now please take a seat."

            y "Confused and dazed, you go to your seat and wait for the hours to pass you by."
            y "When it's time to leave, you see a text from Olivia"

            o "I'll meet you at your house! I have some work to do!"

            y "Smiling, you tuck your phone in your pocket and head home."

            hide kramp stern

        "Go with Olivia to the park":
            $ goodkarma += 1
            $ olivialove += 1
            y "You gained one karma point.  Karma points can be used to determine choice outcomes, wether it be really good or really bad."
            y "You will see your karma points at the end of each day."
            y "Be careful!"

            y "You sneak out in the rush of students exiting the classroom, hoping Kramp doesn't see you."

            scene bg school_lobby

            y "You successfully made it, now just to wait for Olivia."

            show olivia happy

            o "Hey [xname]! Are you ready to head out?"

            x "Of course!"

            y "You look at Olivia, blushing slightly, before beginning to head out"

            hide olivia happy
            show olivia sad

            o "Actually, do you think we could go to your house instead?  Dylan is bringing a friend to the park near our house and I would rather not run into them,"

            x "Absoulutely Liv!"

            hide olivia sad
            show olivia happy

            y "No hesitation at all, wow you are a sucker"

            hide olivia happy

    scene bg x_room

    y "Monday, 4:00 p.m."
    y "Olivia and you sit in silence, doing your homework side by side,"
    y "You look over and see her flowing hair twirling around her pencil, and her soft hands writing away on a sheet of paper"
    y "Oh how you wish to touch her hands."

    show olivia confused

    o "[xname]?"

    x "Yes?"

    o "Do you believe in free will?"

    x "What do you mean?"

    o "Do you think we have control of our own thoughts and actions or do you think every choice we have is for nothing, the end is already decided for us?"

    x "Well..."

    menu:
        "I believe we have control":
            $ olivialove += 1

            x "I believe that we have free will, and our actions matter"

            hide olivia confused
            show olivia laugh

            o "I'm so glad you believe that! Sometimes I get nervous that I don't have control, but you just reassured me unintentionally!"

            y "Olivia returned back to her work, a little smile gracing her lips."
            y "Your heart beats faster at the sight, you slowly reaching your hand towards hers..."

            y "Only for you to pull away last second."

            hide olivia laugh



        "I think the end is decided for us already":

            x "I think the end is already decided for us,"

            hide olivia confused
            show olivia sad

            o "Oh,"
            o "Thoughts like that terrify me."

            y "She looks as if she's about to cry."
            y "But as she turns back to work, you realize there is nothing that can be done now."


            
    
    scene bg x_room

    y "Monday, 8:00 p.m."
    y "Olivia has left, and you're getting ready for bed."
    y "You have [goodkarma] good karma points, and [badkarma] bad karma points."

    y "Now that you've finished your first day, I hope you've had as wonderful of a day as I have,"
    y "Now rest up, we have a whole week ahead of us."

    scene bg black 

    # DAY 2

    scene bg x_room

    y "Day 2: Tuesday, 7:00 a.m."

    x "Uggh, can I shut this alarm up.  I need more sleep."

    menu:
        "Get up and get ready for school":
            $ goodkarma += 1
            $ olivialove += 1
            y "You get up, stretch your muscles, and start getting ready for the day."
        "Sleep in":
            $ badkarma += 1
            y "You snooze your alarm and fall back asleep."

            scene bg black
            scene bg x_room 

            y "You finally awaken on your own, and glance at your alarm clock."
            y "It's 10:00 a.m."
            
            x "10?!?!?! ALREADY?!?!?!"

            z "Honey?? Are you still home?"

            y "You jump out of bed, running and rushing to get ready"

    scene bg classroom_2

    show bea worried 

    x "Are you ok Bea?"

    b "Did you not hear the news?"

    x "What news?"

    y "Just then, Mrs. Kramp walks in, looking a little worse for wear"

    hide bea worried
    show kramp stern

    k "Settle down, settle down.  I understand everyone is a little....on edge as of right now."

    y "Just as you are wondering what she's talking about, you hear the princple over the intercom."

    p "Hello Students, Staff, and Faculty alike."
    p "As many of you know, we are suffering a great loss today,"
    p "Francis Turner has gone missing"

    y "Francis Turner was a small blonde girl in you class,"
    y "You weren't espeically close with her, but you knew she was close with Olivia."
    y "Poor Olivia..."

    y "Whispers and murmurs break out amongst your classmates as the intercom cuts out."

    k "Please settle down everyone.  I understand it's a tough time but there is only so much we can do right now,"

    hide kramp stern
    show bea worried

    b "I heard she was last seen at the Wilma Creek, the one by the entrance into the big forest,"

    y "Wilma creek was known to be large but not very rough, nobody has ever gotten swept up in a current there or lost,"
    y "Well, maybe until now..."

    y "But it seems just as likely that Francis could have wandered into the forest and gotten lost or ran away,"
    y "Now that has happened a lot."

    b "I wanna go home, I feel uneasy being here..."

    y "Almost as if a gift from the heavens, the principle spoke over the intercom once more."

    p "We will be letting out early today, buses will be here any moment, any walkers, drivers, or other modes of transportation are free to go."

    y "You would think everyone would have tumbled out of their seats, but instead, everything seemed to move rather..."
    y "Slowly."

    hide bea worried
    scene bg school_lobby

    y "You walk out to the lobby with Bea, until Olivia finds you both."

    show olivia laugh

    o "Hi guys!"

    y "Olivia's peppy attitude feels inappropriate at this moment, but you don't mention anythin,"
    y "Bea does though."

    hide olivia laugh
    show bea annoyed

    b "How can you be smiling at a time like this."

    hide bea annoyed
    show olivia confused

    o "Excuse me?"

    hide olivia confused
    show bea annoyed

    b "You heard me."

    hide bea annoyed
    show olivia confused

    o "You have no right to talk to me like that."
    o "[xname], are you going to let her talk to me like that."

    x "Uhhhh"

    hide olivia confused

    menu:
        "Olivia's side":
            $ badkarma += 1
            $ olivialove += 1

            x "Bea, Francis was her friend, let her grieve how she wants,"
            x "It's not on us to police her"

            show bea annoyed

            y "Bea just looks at you in silence before walking off, not sparing you another word"

            hide bea annoyed

            y "She's basically saying you aren't worth her energy right now."

            y "but anything for Olivia, right?"

        "Bea's side":
            $ goodkarma += 1

            x "Olivia, I understand you're hurting right now, but maybe we should be more aware of how others are also feeling."

            show olivia sad

            o "Oh."
            o "I see."

            y "Olivia begins to walk away, leaving you to follow after her, leaving Bea alone by herself."

            hide olivia sad

    y "You and Olivia both head over to your house, once again."

    scene bg x_room

    show olivia happy

    o "Can I tell you a secret, [xname]?"

    x "Yes?"

    o "What if I told you that Francis told me,"
    o "She had a crush on you."

    x "She did?"

    y "This case is getting a whole lot sadder."

    o "Yeah but..."
    o "It doesn't matter anyway,"

    hide olivia happy
    show olivia laugh

    o "It's not like she's coming back to tell you herself!"

    hide olivia laugh

    # DAY 3

    y "Day 3: Wednesday, 7:00 a.m."

    x "Wait what."

    y "You wake up groggy and-"

    x "No, wait, go back"

    y "You wake up groggy and-"

    x "NO WE NEED TOO GO BACK, WHAT THE FUCK DID SHE MEAN."

    y "You wanna go back so bad?"
    y "We do what I say."
    y "We're going forward."

    # DAY 4

    y "Day 4: Thursday, 7:00 a.m."

    y "You slowly turn in your sleep, before hearing a woman's voice,"

    z "Sweetheart?"

    x "mom?"

    z "Sweetheart, you're gonna be late for school"

    x "Mom, I really don't want to go."

    z "Sweetheart, don't be ridiculous.  You need to go."

    y "You listen to your mom, getting out of bed and heading to school."

    scene bg school_lobby

    show kramp stern

    k "I told you she wasn't who you thought she was."

    x "What?"
# DAY 5
    scene bg x_room

    y "You know..."

    y "I never like Kramp either."

    y "Day 5 - Friday, 8 a.m."

    y "You're late for school."

    scene bg classroom_2

    show olivia happy

    o "Hi [xname]!"

    x "Liv?  You're ok?"

    o "Why wouldn't I be?"

    x "Liv, what do you know about Francis Turner?"

    o "Who?"

    x "Francis Turner.  Your best friend."

    hide olivia happy
    show olivia laugh

    o "Don't be silly [xname]!  You're my best friend!"

    x "Olivia, where is Mrs. Kramp?"

    hide olivia laugh
    show olivia confused

    o "Who is that?"

    x "Our english teacher?"

    o "We've never had a teacher here that goes by that name."
    o "I'm sorry [xname]."

    x "Olivia..."

    o "[xname], are you ok?"

    menu:
        "I'm ok":
            $ olivialove += 10
            $ goodkarma += 10

        "I'm ok":
            $ olivialove += 10
            $ goodkarma += 10

    
    x "I'm ok Livvy."

    hide olivia confused
    show olivia laugh

    o "Perfect!"
    o "Do you wanna go to your house after class?"

    menu:
        "Yes":
            $ goodkarma += 10
            $ olivialove += 10
        "Yes":
            $ goodkarma += 10
            $ olivialove += 10

    x "Of course!"

    # BELL RING

    o "Have fun in class [xname]!"

    hide olivia laugh
    show olivia happy

    o "Be careful Beatrice Santiago-De Jesus."

    hide olivia happy

    scene bg classroom_2

    show bea worried

    b "[xname], I have something to tell you,"

    x "I have something to tell you too."

    b "You first."

    x "Bea..."

    x "I think you're in,"

    x "sfhahilfhl"

    x "Wait"
    x "I think you're in,"
    x "dhlahfilah"

    b "I know [xname]"

    x "You know?"

    b "I know."
    b "Which is why I wanted to tell you"
    b "I love you, [xname]"

    x "You...what?"

    b "I love you.  I'm deeply in love with you"

    hide bea worried

    # Day 7

    scene bg x_room

    y "Day 7 - Sunday, 11 a.m."

    x "What about Day 6?"

    y "You don't need Day 6."
    y "What you need, is to answer the door."

    # DOOR KNOCK

    show olivia happy

    o "Hi [xname]!"
    o "I must say..."

    hide olivia happy
    show olivia sad

    o "I'm very disappointed in you."

    x "What?"

    o "If I knew you were a dirty sinner, I would have never become your friend."

    x "What..."

    o "I killed Francis the minute she told me she liked you."
    o "I had to rid the world of the wronging she was committing."
    o "It's not right."
    o "It simply isn't right."

    x "Livvy, what are you-"

    o "Kramp knew."
    o "I had some help with her."

    o "And your little friend Bea."
    o "I don't know what Dylan saw in her."
    o "The sinner that she is."

    o "And I know about you."
    o "I know about your little crush on me."

    o "I thought you understood."
    o "I suffered from same-sex attraction too [xname]."
    o "I thought you knew what it was like to choose the right thing."
    o "Choose the normal thing"

    o "But obviously."
    o "I need to rid the world of another dirty little homo."
    o "You're disgusting [xname]."
    o "You don't deserve a place here."

    o "And I'll make sure to do it myself"

    scene bg black

    show bea worried

    b "According to the Trevor Project, LGBTQ+ Youth are an estimated four times more likely to attempt suicide than their peers,"
    b "Not because they are queer, but because of how society treats them,"
    b "The Trevor Project also estimates that more than 1.8 million LGBTQ+ young people (ages 13-24) seriously consider suicide each year in the United States,"
    b "And at least one attempts suicide every 45 seconds."

    b "The Sandy Hook promise states that LGBTQ+ people are more likely to be victims of gun violence, and that risk goes up if the person happens to be a person of color as well"

    b "Even the official United States Congress page states that the murder of queer and trans people have nearly doubled over the past four years"

    b "Who you love or how you identify should not be a life or death situation."
    b "Ever."

    b "To donate to help members of the LGBTQ+ community, espeically the youth, visit thetrevorproject.org"
    b "To donate to help against gun violence, which will help reduce LGBTQ+ homicides, please visit sandyhookpromise.org"

    b "Thank you for playing my game!"











    return
