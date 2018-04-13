#Hailbourne, Inc.
#Lance Vidaure, Josue Lemus, Andy Castro
#Pikachu Searching
#Objective: Catch all the Pikachus using your pokeballs by pressing the spacebar. Professor Oak's goal is to have more than 100 Pikachus in his lab and this is your chance to get him because there are more
#than 100 Pikachus released by Team Rocket. After catching them, you will have to stop the Gastlys by using repel to eliminate them.

from gamelib import*

#Game Object
game = Game(1440,512,"Pikachu Searching")

#Background Object
bk = Image("background.png",game)

bk.resizeTo(1440,512)

#Image Objects
title = Image("pikachusearching.png",game)
title.y -=135

story = Image("story.png",game)
story.x +=250
story.y +=150

start = Image("start.png",game)
start.x -=250
start.y +=150

company = Image("hailbourne-inc.png",game)
company.y -=45

ash = Image("ashketchum2.png",game)
ash.moveTo(1250,260)

teamrocketboy = Image("teamrocketboy.png",game)
teamrocketboy.moveTo(50,280)
teamrocketboy.resizeBy(20)

teamrocketgirl = Image("teamrocketgirl.png",game)
teamrocketgirl.moveTo(50,230)
teamrocketgirl.resizeBy(20)

pokeball = Image("pokeball.png",game)
pokeball.visible = False
pokeball.resizeBy(-90)

gameover = Image("gameover.png",game)
gameover.y -=50

escbutton = Image("escbutton.png",game)
escbutton.y +=50

repel = Image("repel.png",game)
repel.visible = False
repel.resizeBy(-50)

controls = Image("controls.png",game)
controls.resizeBy(-20)
controls.y +=75

win = Image("win.png",game)
win.y -=50

#Pikachu Setup
pikachu = []
for index in range(200):
    pikachu.append( Animation("pikachurunning.png",8,game,200/2,286/4))

for index in range(200):
    x = randint(-10000,-100)
    y = randint(-450,-100)
    pikachu[index].moveTo(x, -y)
    pikachu[index].setSpeed(1,270)

#Gastly Setup
gastly = []
for index in range(200):
    gastly.append( Image("gastly.png",game))

for index in range(200):
    x = randint(-10000,-100)
    y = randint(-450,-100)
    gastly[index].moveTo(x, -y)
    gastly[index].setSpeed(1,270)

#Sound Setup
bkmusic = Sound("bkmusic.wav",1)
point = Sound("point.ogg",2)

#Title Screen
game.over = False
while not game.over:
    game.processInput()

    bk.draw()
    start.draw()
    story.draw()
    company.draw()
    title.draw()
    controls.draw()
    bkmusic.play()

    if start.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    game.update(60)
    
#Level 1
game.over = False #if False, opens next level
PikachusCaptured = 0
PikachusPassed = 0
while not game.over:
    game.processInput()

    bk.draw()
    ash.draw()
    teamrocketboy.draw()
    teamrocketgirl.draw()
    pokeball.move()
    repel.move()

    #Pikachus
    for index in range(200):
        pikachu[index].move()
        
        if pokeball.collidedWith(pikachu[index]):
            point.play()
            pikachu[index].visible = False
            pokeball.visible = False
            PikachusCaptured+= 1

        if pikachu[index].isOffScreen("right") and pikachu[index].visible:
            PikachusPassed +=1
            pikachu[index].visible = False

        if PikachusPassed >= 100:
            game.over = True
            gameover.draw()
            escbutton.draw()
            game.update()
            game.wait(K_ESCAPE)
            game.quit()
            
    #Collisions to kill Ash Ketchum
    if ash.y<66:
        game.over = True
        gameover.draw()
        escbutton.draw()
        game.update()
        game.wait(K_ESCAPE)
        game.quit()
    

    if ash.y>530:
        game.over = True
        gameover.draw()
        escbutton.draw()
        game.update()
        game.wait(K_ESCAPE)
        game.quit()

    if ash.health<1:
        game.over = True
        gameover.draw()
        escbutton.draw()
        game.update()
        game.wait(K_ESCAPE)
        game.quit()

    #Hero Control
    if keys.Pressed[K_UP]:
        ash.y -= 6
    if keys.Pressed[K_DOWN]:
        ash.y += 6
    if keys.Pressed[K_SPACE]:
        pokeball.moveTo(ash.x, ash.y)
        pokeball.setSpeed(20,90)
        pokeball.visible = True

    if PikachusCaptured == 100:
        game.over = True

    game.drawText("PikachusCaptured: " + str(PikachusCaptured),1200,38)
    game.drawText("PikachusPassed: " + str(PikachusPassed),1200,23)

    game.update(60)

#Level 2
game.over = False #if False, opens next level
GastlysPassed = 0
Health = 500
GastlysKilled = 0
while not game.over:
    game.processInput()

    bk.draw()
    ash.draw()
    teamrocketboy.draw()
    teamrocketgirl.draw()
    pokeball.move()
    repel.move()

    #Gastlys
    for index in range(200):
        gastly[index].move()
        
        if gastly[index].collidedWith(ash):
            Health-= 1

        if gastly[index].collidedWith(repel):
            point.play()
            GastlysKilled+= 1
            gastly[index].visible = False
            repel.visible = False

        if gastly[index].isOffScreen("right") and gastly[index].visible:
            GastlysPassed +=1
            gastly[index].visible = False

        if GastlysPassed >= 100:
            game.over = True

        if GastlysKilled >= 100:
            game.over = True
            win.draw()
            escbutton.draw()
            game.update()
            game.wait(K_ESCAPE)
            game.quit()            

    #Collisions to kill Ash Ketchum
    if ash.y<66:
        game.over = True
        gameover.draw()
        escbutton.draw()
        game.update()
        game.wait(K_ESCAPE)
        game.quit()

    if ash.y>530:
        game.over = True
        gameover.draw()
        escbutton.draw()
        game.update()
        game.wait(K_ESCAPE)
        game.quit()

    if ash.health<1:
        game.over = True
        gameover.draw()
        escbutton.draw()
        game.update()
        game.wait(K_ESCAPE)
        game.quit()

    #Hero Control
    if keys.Pressed[K_UP]:
        ash.y -= 6
    if keys.Pressed[K_DOWN]:
        ash.y += 6

    if keys.Pressed[K_SPACE]:
        repel.moveTo(ash.x, ash.y)
        repel.setSpeed(20,90)
        repel.visible = True

    game.drawText("Health: " + str(Health),1200,7)
    game.drawText("GastlysKilled: " + str(GastlysKilled),1200,38)
    game.drawText("GastlysPassed: " + str(GastlysPassed),1200,23)
    game.update(60)

#Ending Screen
gameover.draw()
escbutton.draw()
game.update()
game.wait(K_ESCAPE)
game.quit()
