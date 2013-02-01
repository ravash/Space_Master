""" Author : Dylan Scott
        Project 1A
        Date: August 7th, 2012
        Game Name : Space Master 9000!
        Description : This game will be a top scrolling shooter where you are piloting a space ship with the ability to fire and you must take out enemies to survive.
        Version : 0.2
        Version History: 0.1
        Patch Notes :
        In this version I have changed it so if enemy ships hit either the left or right side of the screen, they will bounce back into play. In this version I have added the bullet class that allows the spaceship
        to shoot 1 shot into the enemies. I have added difficulties to the game that increase the number of enemies by a base amount ( easy has 4, normal has 8, hard has 12) and also reducing the number
        of award pickups on the screen ( easy has 3, normal has 2 and hard has 1).
        
       
        
    
    """
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))


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
        self.rect.centery = 600
        self.rect.centerx = 0
        self.dy = 0
        self.dx = 0
    
    def fire(self):
        (mX , mY) = pygame.mouse.get_pos()   
        self.rect.centerx = mX
        self.rect.centery = 425
        self.dy = -5
            


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
            self.sndYay = pygame.mixer.Sound("yay.ogg")
            self.sndThunder = pygame.mixer.Sound("thunder.ogg")
            self.sndEngine = pygame.mixer.Sound("engine.ogg")
            self.sndEngine.play(-1)
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, 430)

                
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
        if self.rect.left > screen.get_width():
            self.dx *= -1
        if self.rect.left  <= 0:
            self.dx *= -1
    
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.dy = random.randrange(5, 10)
        self.dx = random.randrange(-2, 2)
    
    
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
        if self.rect.left > screen.get_width():
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
        if self.rect.left > screen.get_width():
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
        if self.rect.left > screen.get_width():
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

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "planes: %d, score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()


def easyGame():
    pygame.display.set_caption("Mail Pilot!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    ship = Spaceship()
    
    bullet = Bullet()
    award1 = Award()
    award2 = Award()
    award3 = Award()
    alien1 = Alienone()
    alien2 = Alientwo()
    alien3 = Alienthree()
    alien4 = Alienfour()
    space = Space()
    scoreboard = Scoreboard()
    
    
    friendSprites = pygame.sprite.OrderedUpdates(space, ship)
    bulletSprites = pygame.sprite.OrderedUpdates(bullet)
    awardSprites = pygame.sprite.OrderedUpdates(award1,award2, award3)
    enemySprites = pygame.sprite.Group(alien1, alien2, alien3, alien4)
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
                bullet.fire()
            

        
        #check collisions
        collectAward = pygame.sprite.spritecollide(ship, awardSprites, False)
        if collectAward:
            ship.sndYay.play()
            scoreboard.score += 100
            for theAward in collectAward:
                theAward.reset()


        hitEnemy = pygame.sprite.spritecollide(ship, enemySprites, False)
        if hitEnemy:
            ship.sndThunder.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for theEnemy in hitEnemy:
                theEnemy.reset()
                
        shotEnemy = pygame.sprite.spritecollide(bullet, enemySprites, False)
        if shotEnemy:
            scoreboard.score += 200
            bullet.reset()
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

def normalGame():
    pygame.display.set_caption("Mail Pilot!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    ship = Spaceship()
    
    bullet = Bullet()
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
    space = Space()
    scoreboard = Scoreboard()
    
    
    friendSprites = pygame.sprite.OrderedUpdates(space, ship)
    bulletSprites = pygame.sprite.OrderedUpdates(bullet)
    awardSprites = pygame.sprite.OrderedUpdates(award1,award2)
    enemySprites = pygame.sprite.Group(alien1, alien2, alien3, alien4, alien5, alien6, alien7, alien8)
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
                bullet.fire()
            
        
        #check collisions
        collectAward = pygame.sprite.spritecollide(ship, awardSprites, False)
        if collectAward:
            ship.sndYay.play()
            scoreboard.score += 100
            for theAward in collectAward:
                theAward.reset()


        hitEnemy = pygame.sprite.spritecollide(ship, enemySprites, False)
        if hitEnemy:
            ship.sndThunder.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for theEnemy in hitEnemy:
                theEnemy.reset()
                
        shotEnemy = pygame.sprite.spritecollide(bullet, enemySprites, False)
        if shotEnemy:
            scoreboard.score += 200
            bullet.reset()
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

def hardGame():
    pygame.display.set_caption("Mail Pilot!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    ship = Spaceship()
    
    bullet = Bullet()
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
    space = Space()
    scoreboard = Scoreboard()
    
    
    friendSprites = pygame.sprite.OrderedUpdates(space, ship)
    bulletSprites = pygame.sprite.OrderedUpdates(bullet)
    awardSprites = pygame.sprite.OrderedUpdates(award1)
    enemySprites = pygame.sprite.Group(alien1, alien2, alien3, alien4, alien5, alien6, alien7, alien8, alien9, alien10, alien11, alien12)
    scoreSprite = pygame.sprite.Group(scoreboard)
    
    difficulty = 1

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bullet.fire()
            

        
        #check collisions
        collectAward = pygame.sprite.spritecollide(ship, awardSprites, False)
        if collectAward:
            ship.sndYay.play()
            scoreboard.score += 100
            for theAward in collectAward:
                theAward.reset()


        hitEnemy = pygame.sprite.spritecollide(ship, enemySprites, False)
        if hitEnemy:
            ship.sndThunder.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for theEnemy in hitEnemy:
                theEnemy.reset()
                
        shotEnemy = pygame.sprite.spritecollide(bullet, enemySprites, False)
        if shotEnemy:
            scoreboard.score += 200
            bullet.reset()
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

def instructions(score):
    pygame.display.set_caption("Mail Pilot!")
    
    difficulty = 1

    ship = Spaceship()
    space = Space()
    
    allSprites = pygame.sprite.Group(space, ship)
    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "Mail Pilot.     Last score: %d" % score ,
    "Instructions:  You are a mail pilot,",
    "delivering mail to the islands.",
    "",
    "Fly over an island to drop the mail,",
    "but be careful not to fly too close",    
    "to the clouds. Your plane will fall ",
    "apart if it is hit by lightning too",
    "many times. Steer with the mouse.",
    "",
    "good luck!",
    "",
    "click to start, escape to quit..."
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
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
        
    ship.sndEngine.stop()    
    pygame.mouse.set_visible(True)
    return donePlaying
        
def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
                score = game()
                
if __name__ == "__main__":
    main()
    
    
