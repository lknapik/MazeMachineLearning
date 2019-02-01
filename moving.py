import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((20,20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def move(self, action, xPos, yPos,ver,hor,moves):
        #action is any number 0-3
        def checkWalls(side, x,y,ver,hor):
                s = False
                if(side == "west" and ver[y][x] == 1):
                    s = True
                if(side == "east" and ver[y][x+1] == 1):
                    s = True
                if(side == "north" and hor[y][x] == 1):
                    s = True
                if(side == "south" and hor[y+1][x] == 1):
                    s = True
                return s

        
        terminal = False
        if(action == 0):
            if(checkWalls("east", xPos, yPos, ver, hor) == True):
                reward = 0
            else:
                xPos += 1
                reward  = 1
        elif(action == 1):
            if(checkWalls("south", xPos, yPos, ver, hor) == True):
                reward = 0
            else:
                yPos += 1
                reward  = 1
        elif(action == 2):
            if(checkWalls("west", xPos, yPos, ver, hor) == True):
                reward = 0
            else:    
                xPos -= 1
                reward  = 1
        elif(action == 3):
            if(checkWalls("north", xPos, yPos, ver, hor) == True):
                reward = 0
            else:
                yPos -=1
                reward  = 1

        if(moves > 300):
            terminal = True
            reward = 0
        if(xPos == 19 & yPos == 19):
            terminal = True
            reward = 10
        return xPos, yPos, reward, terminal

