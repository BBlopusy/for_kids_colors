import turtle
import pyttsx3 as tts

while True:
    engine=tts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    engine.setProperty('rate', 147)
    engine.say('Amongus uczy kolorów, stwórz swojego bohatera!')
    engine.runAndWait()
    
    print('****AMONGUS UCZY KOLORÓW****')
    print('wciśnij ENTER')
    input()
    print('Twoje kolory:')
    print('white-black-grey-yellow-orange-brown-red-pink-purple-blue-green-gold-silver')

    #kolor ciała
    engine=tts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 140)
    engine.say('Enter body color')
    engine.runAndWait()
    a = input('kolor ciała: ')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 140)
    engine.say(f'Body color is {a}')
    engine.runAndWait()
    
    #kolor okularów
    engine=tts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 140)
    engine.say('what color of glasses do you want?')
    engine.runAndWait()
    b = input('kolor okularów: ')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 140)
    engine.say(f'Body color is {b}')
    engine.runAndWait()
    #kolor plecaka
    engine=tts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 140)
    engine.say('what color of the backpack do you like?')
    engine.runAndWait()
    c = input('kolor plecaka: ')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 140)
    engine.say(f'Body color is {c}')
    engine.runAndWait()

    BODY_COLOR = a
    BODY_SHADOW = ''
    GLASS_COLOR = b
    GLASS_SHADOW = ''
    KOLOR_PLECAKA = c

    s = turtle.getscreen()
    t = turtle.Turtle()

    # it can move forward backward left right
    def body():
        """ draws the body """
        t.pensize(20)
        #t.speed(15)

        t.fillcolor(BODY_COLOR)
        t.begin_fill()

        # right side
        t.right(90)
        t.forward(50)
        t.right(180)
        t.circle(40, -180)
        t.right(180)
        t.forward(200)

        # head curve
        t.right(180)
        t.circle(100, -180)

        # left side
        t.backward(20)
        t.left(15)
        t.circle(500, -20)
        t.backward(20)

        #t.backward(200)
        t.circle(40, -180)
        #t.right(90)
        t.left(7)
        t.backward(50)

        # hip
        t.up()
        t.left(90)
        t.forward(10)
        t.right(90)
        t.down()
        #t.right(180)
        #t.circle(25, -180)
        t.right(240)
        t.circle(50, -70)

        t.end_fill()


    def glass():
        t.up()
        #t.right(180)
        t.right(230)
        t.forward(100)
        t.left(90)
        t.forward(20)
        t.right(90)

        t.down()
        t.fillcolor(GLASS_COLOR)
        t.begin_fill()

        t.right(150)
        t.circle(90, -55)

        t.right(180)
        t.forward(1)
        t.right(180)
        t.circle(10, -65)
        t.right(180)
        t.forward(110)
        t.right(180)
        
        #t.right(180)
        t.circle(50, -190)
        t.right(170)
        t.forward(80)

        t.right(180)
        t.circle(45, -30)

        t.end_fill()

    def backpack():
        t.up()
        t.right(60)
        t.forward(100)
        t.right(90)
        t.forward(75)

        t.fillcolor(KOLOR_PLECAKA)
        t.begin_fill()

        t.down()
        t.forward(30)
        t.right(255)

        t.circle(300, -30)
        t.right(260)
        t.forward(30)

        t.end_fill()
    
    def endvoice(a,b,c):
        engine = tts.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id) 
        engine.setProperty('rate', 140)
        engine.say(f'hello, I have a {a} body, {b} glasses and a {c} backpack. Thank you.')
        engine.runAndWait() 

    try:
        body()
        glass()
        backpack()
        endvoice(a,b,c)
        
    except:
        print('Gdzieś popełniłeś błąd wpisując kolor')
        print('spróbuj jeszcze raz')


    #t.screen.exitonclick()
   
    input()
