""" Author : Dylan Scott
        Project 1A
        Date: August 8th, 2012
        Game Name : Space Master 9000!
        Description : This game will be a top scrolling shooter where you are piloting a space ship with the ability to fire and you must take out enemies to survive.
        Version : 1.0
        Version History:     0.4
                                        0.3
                                        0.2
                                        0.1
        Patch Notes : In this version I will an additional bullet to the hard difficulty and take away one bullet on the easy to adjust balance between the difficulties.
        
        
       
        
    
    """
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

#this is my class for bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("bullet.gif")
            self.image = self.image.convert()
            self.rect = self.image.get_rect()
            self.reset()
            
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top < 0:
            self.reset()
    
    def reset(self):   
        self.rect.centery = 500
        self.rect.centerx = 0
        self.dy = 0
        self.dx = 0
    
    def fire(self):
        (mX , mY) = pygame.mouse.get_pos()   
        self.rect.centerx = mX
        self.rect.centery = 425
        self.dy = -5
            

#This is my class for the player controlled ship
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("spaceship.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.sndYay = pygame.mixer.Sound("award.ogg")
            self.sndFire = pygame.mixer.Sound("fire.ogg")
            self.sndEnemyk = pygame.mixer.Sound("enemyexplosion.ogg")
            self.sndThunder = pygame.mixer.Sound("explosion.ogg")
            self.sndEngine = pygame.mixer.Sound("background.ogg")
            self.sndGError = pygame.mixer.Sound("nofire.ogg")
            self.sndEngine.play(-1)
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, 430)

  #the class for the pickups in game that give score              
class Award(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("award.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dy = 5
    
    def update(self):
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()
            
    def reset(self):
        self.rect.top = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
#Alien class      
class Alienone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("alienone.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()
        if self.rect.right > screen.get_width():
            self.dx *= -1
        if self.rect.left  <= 0:
            self.dx *= -1
    
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.dy = random.randrange(4, 9)
        self.dx = random.randrange(-1, 1)
    
   #different skinned alien class, also different movement variables 
class Alientwo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("alientwo.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.right > screen.get_width():
            self.dx *= -1
        if self.rect.left  <= 0:
            self.dx *= -1
        if self.rect.top > screen.get_height():
            self.reset()
            
    
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.dy = random.randrange(5, 10)
        self.dx = random.randrange(-2, 2)
       #different skinned alien class, also different movement variables 
class Alienthree(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("alienthree.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.right > screen.get_width():
            self.dx *= -1
        if self.rect.left  <= 0:
            self.dx *= -1
        if self.rect.top > screen.get_height():
            self.reset()
    
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.dy = random.randrange(5, 11)
        self.dx = random.randrange(-2, 2)
           #different skinned alien class, also different movement variables 
class Alienfour(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("alienthree.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.right > screen.get_width():
            self.dx *= -1
        if self.rect.left  <= 0:
            self.dx *= -1
        if self.rect.top > screen.get_height():
            self.reset()
    
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.dy = random.randrange(5, 12)
        self.dx = random.randrange(-3, 3)
        #The class for the background
class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("space3.gif")
        self.rect = self.image.get_rect()
        self.dy = 5
        self.reset()
        
    def update(self):
        self.rect.bottom += self.dy
        if self.rect.bottom >= 1440:
            self.reset() 
    
    def reset(self):
        self.rect.top = -960
#the class for the scoreboard
class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "Shields: %d, score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (4, 128, 0))
        self.rect = self.image.get_rect()

#Here is my class for if the user chooses the easy difficulty
def easyGame():
    pygame.display.set_caption("Space Master 9000!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    ship = Spaceship()
    
    bullet1 = Bullet()
    bullet2 = Bullet()
    award1 = Award()
    award2 = Award()
    award3 = Award()
    alien1 = Alienone()
    alien2 = Alientwo()
    alien3 = Alienthree()
    alien4 = Alienfour()
    alien5 = Alienone()
    alien6 = Alientwo()
    alien7 = Alienthree()
    alien8 = Alienfour()
    space = Space()
    scoreboard = Scoreboard()
    
    
    friendSprites = pygame.sprite.OrderedUpdates(space, ship)
    bulletSprites = pygame.sprite.OrderedUpdates(bullet1,bullet2)
    awardSprites = pygame.sprite.OrderedUpdates(award1,award2, award3)
    enemySprites = pygame.sprite.Group(alien1, alien2, alien3, alien4,alien5, alien6, alien7, alien8)
    scoreSprite = pygame.sprite.Group(scoreboard)
    

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            #This is my tracker of the bullets, if a bullet is unused, it will fire it, if the alloted bullets are used, it will play the error sound
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bullet1.rect. top > 480:
                    ship.sndFire.play()
                    bullet1.fire()
                elif bullet2.rect.top > 480:
                    ship.sndFire.play()
                    bullet2.fire()
                else:
                    ship.sndGError.play()
            

        
        #check pickup collisions
        collectAward = pygame.sprite.spritecollide(ship, awardSprites, False)
        if collectAward:
            ship.sndYay.play()
            scoreboard.score += 100
            for theAward in collectAward:
                theAward.reset()

        #check if physical collision of ship and enemies
        hitEnemy = pygame.sprite.spritecollide(ship, enemySprites, False)
        if hitEnemy:
            ship.sndThunder.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
                donePlaying = gameover(scoreboard.score)
            for theEnemy in hitEnemy:
                theEnemy.reset()
         #this checks the bullet against enemy sprites to see if it was hit,       
        shotEnemy = pygame.sprite.spritecollide(bullet1, enemySprites, False)
        if shotEnemy:
            ship.sndEnemyk.play()
            scoreboard.score += 200
            bullet1.reset()
        for theEnemy in shotEnemy:
            theEnemy.reset()
            #also checks bullet collision, comparing two sprite groups wasnt working so i assumed you had to check individual sprites against groups.
        shotEnemy = pygame.sprite.spritecollide(bullet2, enemySprites, False)
        if shotEnemy:
            ship.sndEnemyk.play()
            scoreboard.score += 200
            bullet2.reset()
        for theEnemy in shotEnemy:
            theEnemy.reset()

        friendSprites.update()
        awardSprites.update()
        enemySprites.update()
        bulletSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        awardSprites.draw(screen)
        enemySprites.draw(screen)
        bulletSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    ship.sndEngine.stop()
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score
#Very simular to the first easyGame() . It however has 1 more bullet alloted to be fired, a total of 12 enemies ( 4 more than the previous difficulty). Also there are less pickups that give score, however
#they give extra score
def normalGame():
    pygame.display.set_caption("Space Master 9000!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    ship = Spaceship()
    
    bullet1 = Bullet()
    bullet2 = Bullet()
    bullet3 = Bullet()
    award1 = Award()
    award2 = Award()
    alien1 = Alienone()
    alien2 = Alientwo()
    alien3 = Alienthree()
    alien4 = Alienfour()
    alien5 = Alienone()
    alien6 = Alientwo()
    alien7 = Alienthree()
    alien8 = Alienfour()
    alien9 = Alienone()
    alien10 = Alientwo()
    alien11 = Alienthree()
    alien12 = Alienfour()
    space = Space()
    scoreboard = Scoreboard()
    
    
    friendSprites = pygame.sprite.OrderedUpdates(space, ship)
    bulletSprites = pygame.sprite.OrderedUpdates(bullet1, bullet2, bullet3)
    awardSprites = pygame.sprite.OrderedUpdates(award1,award2)
    enemySprites = pygame.sprite.Group(alien1, alien2, alien3, alien4, alien5, alien6, alien7, alien8, alien9, alien10, alien11, alien12)
    scoreSprite = pygame.sprite.Group(scoreboard)
    


    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bullet1.rect. top > 480:
                    ship.sndFire.play()
                    bullet1.fire()
                elif bullet2.rect.top > 480:
                    ship.sndFire.play()
                    bullet2.fire()
                elif bullet3.rect.top > 480:
                    ship.sndFire.play()
                    bullet3.fire()
                else:
                    ship.sndGError.play()
                    
        collectAward = pygame.sprite.spritecollide(ship, awardSprites, False)
        if collectAward:
            ship.sndYay.play()
            scoreboard.score += 200
            for theAward in collectAward:
                theAward.reset()


        hitEnemy = pygame.sprite.spritecollide(ship, enemySprites, False)
        if hitEnemy:
            ship.sndThunder.play()                  
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
                donePlaying = gameover(scoreboard.score)
            for theEnemy in hitEnemy:
                theEnemy.reset()
                
                
        shotEnemy = pygame.sprite.spritecollide(bullet1, enemySprites, False)
        if shotEnemy:
            ship.sndEnemyk.play()
            scoreboard.score += 200
            bullet1.reset()
        for theEnemy in shotEnemy:
            theEnemy.reset()
            
        shotEnemy = pygame.sprite.spritecollide(bullet2, enemySprites, False)
        if shotEnemy:
            ship.sndEnemyk.play()
            scoreboard.score += 200
            bullet2.reset()
        for theEnemy in shotEnemy:
            theEnemy.reset()
            
        shotEnemy = pygame.sprite.spritecollide(bullet3, enemySprites, False)
        if shotEnemy:
            ship.sndEnemyk.play()
            scoreboard.score += 200
            bullet3.reset()
        for theEnemy in shotEnemy:
            theEnemy.reset()
        
        friendSprites.update()
        awardSprites.update()
        enemySprites.update()
        bulletSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        awardSprites.draw(screen)
        enemySprites.draw(screen)
        bulletSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    ship.sndEngine.stop()
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score
#Very simular to the first and second easyGame(), and hardGame() . It however has 1 more bullet than normal alloted to be fired, a total of 16 enemies ( 4 more than the previous difficulty)
def hardGame():
    donePlaying = False
    pygame.display.set_caption("Space Master 9000!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    ship = Spaceship()
    
    bullet1 = Bullet()
    bullet2 = Bullet()
    bullet3 = Bullet()
    bullet4 = Bullet()
    award1 = Award()
    alien1 = Alienone()
    alien2 = Alientwo()
    alien3 = Alienthree()
    alien4 = Alienfour()
    alien5 = Alienone()
    alien6 = Alientwo()
    alien7 = Alienthree()
    alien8 = Alienfour()
    alien9 = Alienone()
    alien10 = Alientwo()
    alien11 = Alienthree()
    alien12 = Alienfour()
    alien13 = Alienone()
    alien14 = Alientwo()
    alien15 = Alienthree()
    alien16 = Alienfour()
    space = Space()
    scoreboard = Scoreboard()
    
    
    friendSprites = pygame.sprite.OrderedUpdates(space, ship)
    bulletSprites = pygame.sprite.OrderedUpdates(bullet1, bullet2, bullet3, bullet4)
    awardSprites = pygame.sprite.OrderedUpdates(award1)
    enemySprites = pygame.sprite.Group(alien1, alien2, alien3, alien4, alien5, alien6, alien7, alien8, alien9, alien10, alien11, alien12, alien13, alien14, alien15, alien16)
    scoreSprite = pygame.sprite.Group(scoreboard)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying= True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bullet1.rect. top > 480:
                    ship.sndFire.play()
                    bullet1.fire()
                elif bullet2.rect.top > 480:
                    ship.sndFire.play()
                    bullet2.fire()
                elif bullet3.rect.top > 480:
                    ship.sndFire.play()
                    bullet3.fire()
                elif bullet4.rect.top > 480:
                    ship.sndFire.play()
                    bullet4.fire()
                else:
                    ship.sndGError.play()
            


        collectAward = pygame.sprite.spritecollide(ship, awardSprites, False)
        if collectAward:
            ship.sndYay.play()
            scoreboard.score += 400
            for theAward in collectAward:
                theAward.reset()


        hitEnemy = pygame.sprite.spritecollide(ship, enemySprites, False)
        if hitEnemy:
            ship.sndThunder.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
                donePlaying = gameover(scoreboard.score)
            for theEnemy in hitEnemy:
                theEnemy.reset()
                
        shotEnemy = pygame.sprite.spritecollide(bullet1, enemySprites, False)
        if shotEnemy:
            ship.sndEnemyk.play()
            scoreboard.score += 200
            bullet1.reset()
        for theEnemy in shotEnemy:
            theEnemy.reset()
            
        shotEnemy = pygame.sprite.spritecollide(bullet2, enemySprites, False)
        if shotEnemy:
            ship.sndEnemyk.play()
            scoreboard.score += 200
            bullet2.reset()
        for theEnemy in shotEnemy:
            theEnemy.reset()
            
        shotEnemy = pygame.sprite.spritecollide(bullet3, enemySprites, False)
        if shotEnemy:
            ship.sndEnemyk.play()
            scoreboard.score += 200
            bullet3.reset()
        for theEnemy in shotEnemy:
            theEnemy.reset()
            
        shotEnemy = pygame.sprite.spritecollide(bullet4, enemySprites, False)
        if shotEnemy:
            ship.sndEnemyk.play()
            scoreboard.score += 200
            bullet4.reset()
        for theEnemy in shotEnemy:
            theEnemy.reset()
        
        friendSprites.update()
        awardSprites.update()
        enemySprites.update()
        bulletSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        awardSprites.draw(screen)
        enemySprites.draw(screen)
        bulletSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    ship.sndEngine.stop()
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score
#my instructions menu
def instructions(score):
    pygame.display.set_caption("Space Master 9000!")
    
    difficulty = 1

    space = Space()
    
    allSprites = pygame.sprite.Group(space)
    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "Space Master     Last score: %d" % score ,
    "Welcome to Space, Cadet!",
    "You're mission is to maneuver and",
    "destroy all enemy vessels!",
    "",
    "Along the way be sure to pick up",    
    "items to further increase your score",
    "",
    "Be careful though, your cannons",
    "can only fire limited shots at a time.",
    "Good luck!",
    "",
    "Click 1 for easy, 2 for normal,",
    "3 for hard and your game",
    "will start immediately!"
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
                    
                #This checks for the user's input on what mode he wants to run, then runs that code for the specific difficulty
                if event.key == pygame.K_1:
                    score = easyGame()
                    keepGoing = False
                    donePlaying = False
                    
                elif event.key == pygame.K_2:
                    score = normalGame()
                    keepGoing = False
                    donePlaying = False
                    
                elif event.key == pygame.K_3:
                    score = hardGame()
                    keepGoing = False
                    donePlaying = False
                    
    
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
          
    pygame.mouse.set_visible(True)
    
    return donePlaying
#Game over screen, very similar to the intro screen
def gameover(score):
    pygame.display.set_caption("Space Master 9000!")
    
    difficulty = 1

    space = Space()
    
    allSprites = pygame.sprite.Group(space)
    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "",
    "",
    "",
    "It seems your efforts were in vain.",
    "That is a shame. However :",
    "Your score was :  %d" %  score ,
    "If you wish to play again on",
    "an easier difficulty you can play",
    "Again by clicking the x in the",
    "              corner!           "
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    keepGoing = False
                    donePlaying = False
                    

                    
    
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
          
    pygame.mouse.set_visible(True)
    
    return donePlaying
        
        
def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        """
        if not donePlaying:
                donePlaying = instructions(score)
         """ 
                
if __name__ == "__main__":
    main()
    
    
