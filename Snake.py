
import pygame
import random
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (46,139,87)
YELLOW = (255,255,0)
 
# Set the width and height of each snake segment
segment_width = 20
segment_height = 20
# Margin between each segment
segment_margin = 3
 
# Set initial speed
x_change = segment_width + segment_margin
y_change = 0
#Set inital level
level = 1
#Food coordinates
Fx = 0
Fy = 0
 
class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
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
    # Check if snake collides with wall
    if snake[0].rect.x >= 770 or snake[0].rect.x<29:
            return  False
    if snake[0].rect.y>=564 or snake[0].rect.y<30:
            return False        

def foodCol(snake,x,y):
    if (snake[0].rect.x) <= x+30 and ((snake[0].rect.x)+30) >= x:
        if (snake[0].rect.y) <= y+30 and ((snake[0].rect.y)) >= y:
            return True
        
def randomGen(x,y):
    return random.randint(x,y)
    

 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Snake!')
 
allspriteslist = pygame.sprite.Group()
 
# Create an initial snake
snake_segments = []
for i in range(10):
    x = 250 - (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)
 
 
clock = pygame.time.Clock()
done = False
Fx = randomGen(36,765)
Fy = randomGen(30,564)
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
                x_change = (segment_width + segment_margin) *- 1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) *- 1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)
        

    
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
    if Collision(snake_segments) == False:
       done = True
    if foodCol(snake_segments,Fx,Fy) == True:
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
    

    myfont = pygame.font.SysFont("monospace", 60)

    # render text
    label = myfont.render("Snake food:"+str(level),100,BLACK)
    screen.blit(label, (287,30))

    #Draw food
    pygame.draw.rect(screen,(255,0,0),(Fx,Fy,20,20))
    #Draw Snake
    allspriteslist.draw(screen)
    # Flip screen
    pygame.display.flip()
 
    # Pause
    clock.tick(9+(level))
    
  
    
pygame.quit()
