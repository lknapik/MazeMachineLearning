from random import randrange,shuffle
import pygame
class maze:    
    def makeMaze(self, w, h):
        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
        hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
    
        def walk(x, y):
            vis[y][x] = 1
    
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]: continue
                if xx == x: hor[max(y, yy)][x] = "+  "
                if yy == y: ver[y][max(x, xx)] = "   "
                walk(xx, yy)
            
        def translateMaze(hor,ver):
            k = 0
            l = 0
            for a in hor:
                l = 0
                for i in a:
                    if(i == '+--'):
                        hor[k][l] = 1
                    if(i == '+  '):
                        hor[k][l] = 0
                    l = l+1
                k = k+1
                a.pop()
        
            k = 0
            l = 0
            for b in ver:
                l=0
                for j in b:
                    if(j == '|  ' or j == '|'):
                        ver[k][l] = 1
                    if(j == '   '):
                        ver[k][l] = 0
                    l = l+1
                k = k+1  
            return hor,ver
        
        walk(randrange(w), randrange(h))
        hor, ver = translateMaze(hor,ver)
        return hor, ver
    
    def drawMaze(self,hor,ver):
        windowSurface = pygame.Surface((800,800))
        WHITE = (255,255,255)
        xCount = 0
        yCount = 0
        for i in hor:
            xCount = 0
            for j in i:
                if(j == 1):
                    pygame.draw.line(windowSurface, WHITE, (40*xCount,40*yCount),(40*xCount+40,40*yCount),2)
                xCount += 1
            yCount += 1
        xCount = 0
        yCount = 0
        for i in ver:
            xCount = 0
            for j in i:
                if(j == 1):
                    pygame.draw.line(windowSurface, WHITE, (40*xCount,40*yCount),(40*xCount,40*yCount+40),2)
                xCount += 1
            yCount += 1
        return windowSurface

            
