
import pygame
import random
import curses

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (46,139,87)
YELLOW = (255,255,0)


 
# Set the width and height of each snake block
block_width = 20
block_height = 20
# Margin between each segment
segment_margin = 3
 
# Set initial speed
x_change = block_width + segment_margin
y_change = 0
#Set inital level
level = 1
#check if menu is complete
done = False
#Food coordinates
Fx = 0
Fy = 0
#File storing high scores
file = open("/Users/ryanremer/Desktop/Untitled.txt",'r')
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
#Buttons for menu
playButton = pygame.Rect(260,110,300,160)
hsButton = pygame.Rect(77,310,673,160)
backButton = pygame.Rect(30,30,100,50)

# Call this function so the Pygame library can initialize itself
pygame.init()

myfont = pygame.font.SysFont("monospace", 100)
backfont = pygame.font.SysFont("monospance",30)
 
class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Set height, width
        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(GREEN)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
 # Function to detect if snake collides with itself       
def Collision(snake):    
    for i in range(1,len(snake)):
         if snake[0].rect.x == snake[i].rect.x and snake[0].rect.y == snake[i].rect.y:
             return False            
        
def randomGen(x,y):
    return random.randint(x,y)

def clearScr():
    screen.fill
    screen.set_alpha(255)
    pygame.draw.rect(screen,WHITE, (17,16,765,567), 0)

    
#Start menu
def drawMenu():
    clearScr()
    pygame.draw.rect(screen,(255,000,000),playButton,5)
    pygame.draw.rect(screen,(255,000,000),hsButton,5)  
    Playlabel = myfont.render(("Play"),90,(255,0,0))
    HighScoreLabel = myfont.render(("High Scores"),200,(255,0,0))

    screen.blit(HighScoreLabel,(85,330))
    screen.blit(Playlabel, (280,130))
    pygame.display.flip()
    pressed = True
    while pressed:
        ev = pygame.event.get()
        # proceed events
        for event in ev:
          if event.type == pygame.MOUSEBUTTONDOWN and playButton.collidepoint(pygame.mouse.get_pos()):          
              pressed = False
              done = True
          if event.type == pygame.MOUSEBUTTONDOWN and hsButton.collidepoint(pygame.mouse.get_pos()):
              done = True
              pressed = False
              drawHighScores()
 
def drawHighScores():
    clearScr()
    pygame.draw.rect(screen,(255,0,0),backButton,5)
    backLabel = backfont.render("Back",2,BLACK)
    HighScoreLabel = myfont.render(("High Scores"),200,(255,0,0))
    screen.blit(backLabel,(50,50))
    screen.blit(HighScoreLabel,(81,130))
    pygame.display.flip()
    pressed = True
    while pressed:
        ev = pygame.event.get()
  # proceed events
        for event in ev:
          if event.type == pygame.MOUSEBUTTONDOWN and backButton.collidepoint(pygame.mouse.get_pos()):          
              pressed = False
              done = True
              drawMenu()
          
              

 
# Set the title of the window
pygame.display.set_caption('Snake!')
 
allspriteslist = pygame.sprite.Group()
 
# Create an initial snake
snake_segments = []
for i in range(10):
    x = 250 - (block_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)
 
 
clock = pygame.time.Clock()

Fx = randomGen(36,765)
Fy = randomGen(30,564)
food = pygame.Rect(Fx,Fy,20,20)



drawMenu()

screen.fill
screen.set_alpha(255)
pygame.display.flip()
pygame.draw.rect(screen,WHITE, (17,16,765,567), 0)
          
         
# Game Loop
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (block_width + segment_margin) *- 1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (block_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (block_height + segment_margin) *- 1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (block_height + segment_margin)
        

    
    # Get rid of last segment of the snake
    # .pop() command removes last item in list
    old_segment = snake_segments.pop()
    allspriteslist.remove(old_segment)
 
    # Figure out where new segment will be
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)
 
    # Insert new segment into the list
    snake_segments.insert(0, segment)
    allspriteslist.add(segment)

    #Call method to check for collision
    newRect = pygame.Rect(snake_segments[0].rect.x,snake_segments[0].rect.y,20,20)
    innerRect = pygame.Rect(17,16,765,567)
    
    if innerRect.contains(newRect)==False:
        done = True
    if Collision(snake_segments) == False:
        done = True
    if newRect.colliderect(food) == True:
        level = level +1
        snake_segments.insert(0, segment)
        allspriteslist.add(segment)
        Fx = randomGen(36,765)
        Fy = randomGen(30,564)
       
    # -- Draw everything
    # Clear screen
    pygame.display.set_caption('Snake')
    
    #Make head of snake Yellow    
    snake_segments[1].image.fill(GREEN)
    snake_segments[0].image.fill(YELLOW)
    
    screen.fill(BLACK)
    
    #Draw inner rectangle
    pygame.draw.rect(screen,WHITE, (17,16,765,567), 0)
    

    

    # render text
    label = myfont.render("Snake:"+str(level),100,BLACK)
    screen.blit(label, (227,30))

    #Draw food                
    food = pygame.Rect(Fx,Fy,20,20)
    pygame.draw.rect(screen,(255,0,0),food)  
    #Draw Snake
    allspriteslist.draw(screen)
    # Flip screen
    pygame.display.flip()
 
    # Pause
    clock.tick(9+(level))
    
  
    
pygame.quit()
