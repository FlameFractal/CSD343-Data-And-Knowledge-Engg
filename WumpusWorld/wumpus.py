import time
from random import randint

class agent:
    def __init__(self):
        self.linecurrent = 0
        self.columncurrent = 0
        self.matrix = []
        self.score = 0
        self.currentdirection = 3

    def InitializematrixMatrix(self):
        for i in range(4):
            line = []
            for k in range(4):
                line.append(None)
            self.matrix.append(line)

    def FillMatrix(self, situacaoLugar):
        self.matrix[self.linecurrent][self.columncurrent] = situacaoLugar

    def FillMatrixAtPosition(self, situacaoLugar, line, column):
        self.matrix[line][column] = situacaoLugar
        
    def GetPosition(self, line, column):
        if (line < 0 or
            line > 3 or
            column < 0 or
            column > 3):
            return None
        return self.matrix[line][column]

    def WalkUp(self):
        self.linecurrent += 1
        self.score -= 1
        self.currentdirection = 1
        print("Agent moved up.      " + str(self.linecurrent) + ", " + str(self.columncurrent))

    def WalkDown(self):
        self.linecurrent -= 1
        self.score -= 1
        self.currentdirection = 2
        print("Agent moved down.    " + str(self.linecurrent) + ", " + str(self.columncurrent))

    def WalkRight(self):
        self.columncurrent += 1
        self.score -= 1
        self.currentdirection = 3
        print("Agent moved right.   " + str(self.linecurrent) + ", " + str(self.columncurrent))

    def WalkLeft(self):
        self.columncurrent -= 1
        self.score -= 1
        self.currentdirection = 4
        print("Agent moved left.    " + str(self.linecurrent) + ", " + str(self.columncurrent))

class matrix:
    def __init__(self):
        self.matrix = []

    def InitializematrixMatrix(self):
        class PathInmatrix:
            def __init__(self):
                self.SenseMonster = False
                self.Sensepit = False
                self.Monster = False
                self.pit = False
                self.Gold = False
        for i in range(4):
            line = []
            for k in range(4):
                line.append(PathInmatrix())
            self.matrix.append(line)
        self.matrix[3][3].Gold = True
        
        self.matrix[0][3].Sensepit = True
        self.matrix[1][2].Sensepit = True
        self.matrix[0][1].Sensepit = True
        self.matrix[0][2].pit = True
        
        self.matrix[1][2].Sensepit = True
        self.matrix[3][2].Sensepit = True
        self.matrix[2][3].Sensepit = True
        self.matrix[2][1].Sensepit = True
        self.matrix[2][2].pit = True
        

    def GetPosition(self, line, column):
        if (line < 0 or
            line > 3 or
            column < 0 or
            column > 3):
            return None
        return self.matrix[line][column]

def turnright(positionright):
    if agent.columncurrent < 3:
        agent.WalkRight()
        return True
    return False
def turnup(positionup):
    if agent.linecurrent < 3:
        agent.WalkUp()
        return True
    return False
def turnleft(positionleft):
    if agent.columncurrent > 0:
        agent.WalkLeft()
        return True
    return False
def turndown(positiondown):
    if agent.linecurrent > 0:
        agent.WalkDown()
        return True
    return False

def play():
    global gameNotOver

    positioninmatrix = agent.GetPosition(agent.linecurrent, agent.columncurrent)
    positiondown = agent.GetPosition(agent.linecurrent-1, agent.columncurrent)
    positionup = agent.GetPosition(agent.linecurrent+1, agent.columncurrent)
    positionright = agent.GetPosition(agent.linecurrent, agent.columncurrent+1)
    positionleft = agent.GetPosition(agent.linecurrent, agent.columncurrent-1)
    posperpdownright = agent.GetPosition(agent.linecurrent-1, agent.columncurrent+1)
    posperpupleft = agent.GetPosition(agent.linecurrent+1, agent.columncurrent-1)
    posperpdownleft = agent.GetPosition(agent.linecurrent-1, agent.columncurrent-1)
    posperpupright   = agent.GetPosition(agent.linecurrent+1, agent.columncurrent+1)

    if (not positioninmatrix.SenseMonster and
        not positioninmatrix.Sensepit):
        if agent.currentdirection == 3:
            if positionright == None:
                if turnright(positionright):
                    return
            if positionup == None:
                if turnup(positionup):
                    return
            if positionleft == None:
                if turnleft(positionleft):
                    return
            if positiondown == None:
                if turndown(positiondown):
                    return
            if (positionright != None and
                not positionright.pit and
                not positionright.Monster):
                if turnright(positionright):
                    return
            if (positionup != None and
                not positionup.pit and
                not positionup.Monster):
                if turnup(positionup):
                    return
            if (positionleft != None and
                not positionleft.pit and
                  not positionleft.Monster):
                if turnleft(positionleft):
                    return
            if (positiondown != None and
                not positiondown.pit and
                  not positiondown.Monster):
                if turndown(positiondown):
                    return
        if agent.currentdirection == 1:
            if positionup == None:
                if turnup(positionup):
                    return
            if positionright == None:
                if turnright(positionright):
                    return
            if positionleft == None:
                if turnleft(positionleft):
                    return
            if positiondown == None:
                if turndown(positiondown):
                    return
            if (positionup != None and
                not positionup.pit and
                  not positionup.Monster):
                if turnup(positionup):
                    return
            if (positionright != None and
                not positionright.pit and
                  not positionright.Monster):
                if turnright(positionright):
                    return
            if (positionleft != None and
                not positionleft.pit and
                not positionleft.Monster):
                if turnleft(positionleft):
                    return
            if (positiondown != None and
                not positiondown.pit and
                not positiondown.Monster):
                if turndown(positiondown):
                    return
        if agent.currentdirection == 4:
            if positionleft == None:
                if turnleft(positionleft):
                    return
            if positionup == None:
                if turnup(positionup):
                    return
            if positionright == None:
                if turnright(positionright):
                    return
            if positiondown == None:
                if turndown(positiondown):
                    return
            if (positionleft != None and
                not positionleft.pit and
                not positionleft.Monster):
                if turnleft(positionleft):
                    return
            if (positionup != None and
                not positionup.pit and
                not positionup.Monster):
                if turnup(positionup):
                    return
            if (positionright != None and
                not positionright.pit and
                  not positionright.Monster):
                if turnright(positionright):
                    return
            if (positiondown != None and
                not positiondown.pit and
                  not positiondown.Monster):
                if turndown(positiondown):
                    return
        if agent.currentdirection == 2:
            if positiondown == None:
                if turndown(positiondown):
                    return
            if positionup == None:
                if turnup(positionup):
                    return
            if positionright == None:
                if turnright(positionright):
                    return
            if positionleft == None:
                if turnleft(positionleft):
                    return
            if (positiondown != None and
                not positiondown.pit and
                not positiondown.Monster):
                if turndown(positiondown):
                    return
            if (positionup != None and
                not positionup.pit and
                not positionup.Monster):
                if turnup(positionup):
                    return
            if (positionright != None and
                not positionright.pit and
                not positionright.Monster):
                if turnright(positionright):
                    return
            if (positionleft != None and
                not positionleft.pit and
                not positionleft.Monster):
                if turnleft(positionleft):
                    return
    elif positioninmatrix.SenseMonster:
        print("Smell")
         
        if (posperpupleft != None):
            if posperpupleft.SenseMonster:
                if (positionleft != None and
                    not positionleft.Monster):
                        if agent.GetPosition(agent.linecurrent+1, agent.columncurrent) == None:
                            agent.FillMatrixAtPosition(matrix.GetPosition(agent.linecurrent+1, agent.columncurrent), agent.linecurrent+1, agent.columncurrent)
                            print("Monster Found in Location (" + str(agent.linecurrent+1) + ", " + str(agent.columncurrent) )
                             
                        if agent.columncurrent < 3:
                            agent.WalkRight()
                            return
                elif (positionleft != None and
                      positionleft.Monster):
                    if agent.linecurrent < 3:
                        agent.WalkUp()
                        return
            else:
                if agent.GetPosition(agent.linecurrent-1, agent.columncurrent) == None:
                    agent.FillMatrixAtPosition(matrix.GetPosition(agent.linecurrent-1, agent.columncurrent), agent.linecurrent+1, agent.columncurrent)
                    print("Monster Found in Location (" + str(agent.linecurrent-1) + ", " + str(agent.columncurrent) )
                     
                if agent.linecurrent > 0:
                    agent.WalkDown()
                    return

        if (posperpdownright != None):
            if (posperpdownright.SenseMonster):
                if (positionright != None and
                    not positionright.Monster):
                        if agent.GetPosition(agent.linecurrent+1, agent.columncurrent) == None:
                            agent.FillMatrixAtPosition(matrix.GetPosition(agent.linecurrent+1, agent.columncurrent), agent.linecurrent, agent.columncurrent+1)
                            print("Monster Found in Location (" + str(agent.linecurrent+1) + ", " + str(agent.columncurrent) )
                             
                        if agent.columncurrent < 3:
                            agent.WalkRight()
                            return
                elif (positionright != None and
                      positionright.Monster):
                    if agent.linecurrent < 3:
                        agent.WalkUp()
                        return
            else:
                if agent.columncurrent < 3:
                    agent.WalkRight()
                    return
            
        if (posperpdownleft != None and
            posperpdownleft.SenseMonster):
            if (positionleft != None and
                not positionleft.Monster):
                if agent.GetPosition(agent.linecurrent-1, agent.columncurrent) == None:
                    agent.FillMatrixAtPosition(matrix.GetPosition(agent.linecurrent-1, agent.columncurrent), agent.linecurrent-1, agent.columncurrent-1)
                    print("Monster Found in Location (" + str(agent.linecurrent-1) + ", " + str(agent.columncurrent) )
                     
                if agent.currentdirection == 3:
                    agent.WalkRight()
                    return
                elif agent.columncurrent > 0:
                    agent.WalkLeft()
                    return
            elif (positionleft != None and
                  positionleft.Monster):
                if agent.linecurrent > 0:
                    agent.WalkDown()
                    return
        if (posperpupright != None and
            posperpupright.SenseMonster):
            if (positionright != None and
                not positionright.Monster):
                if agent.GetPosition(agent.linecurrent+1, agent.columncurrent) == None:
                    agent.FillMatrixAtPosition(matrix.GetPosition(agent.linecurrent+1, agent.columncurrent), agent.linecurrent, agent.columncurrent+1)
                    print("Monster Found in Location (" + str(agent.linecurrent+1) + ", " + str(agent.columncurrent) )
                     
                if agent.linecolumn < 3:
                    agent.WalkRight()
                    return
            elif (positionright != None and
                  positionright.Monster):
                if agent.linecurrent < 3:
                    agent.WalkUp()
                    return
            elif (positionup != None and
                  not positionup.Monster):
                if agent.GetPosition(agent.linecurrent, agent.columncurrent+1) == None:
                    agent.FillMatrixAtPosition(matrix.GetPosition(agent.linecurrent, agent.columncurrent+1), agent.linecurrent, agent.columncurrent+1)
                    print("Monster Found in Location (" + str(agent.linecurrent) + ", " + str(agent.columncurrent+1) )
                     
                if agent.linecurrent < 3:
                    agent.WalkUp()
                    return
                
        if (positionleft != None and
            not positionleft.Monster):
            agent.WalkLeft()
        elif (positionright != None and
            not positionright.Monster):
            agent.WalkRight()
        elif (positiondown != None and
            not positiondown.Monster):
            agent.WalkDown()
        elif (positionup != None and
            not positionup.Monster):
            agent.WalkUp()

    elif positioninmatrix.Sensepit:
        print("\nSensed Breeze.\n")
        if (posperpupleft != None):
            if (posperpupleft.Sensepit):
                if (positionleft != None and
                    not positionleft.pit):
                        if agent.GetPosition(agent.linecurrent+1, agent.columncurrent) == None:
                            agent.FillMatrixAtPosition(matrix.GetPosition(agent.linecurrent+1, agent.columncurrent), agent.linecurrent+1, agent.columncurrent)
                            print("Pit at " + str(agent.linecurrent+1) + ", " + str(agent.columncurrent) )
                             
                        if agent.currentdirection == 1 and \
                           agent.linecurrent < 3:
                            agent.WalkUp()
                            return
                        if agent.columncurrent < 3:
                            agent.WalkRight()
                            return
                elif (positionleft != None and
                      positionleft.pit):
                    if agent.linecurrent < 3:
                        agent.WalkUp()
                        return
                

        if (posperpdownright != None and
            posperpdownright.Sensepit):
            if (positionright != None and
                not positionright.pit):
                    if agent.GetPosition(agent.linecurrent+1, agent.columncurrent) == None:
                        agent.FillMatrixAtPosition(matrix.GetPosition(agent.linecurrent+1, agent.columncurrent), agent.linecurrent, agent.columncurrent+1)
                        print("Pit at " + str(agent.linecurrent+1) + ", " + str(agent.columncurrent) )
                         
                    if agent.columncurrent < 3:
                        agent.WalkRight()
                        return
            elif (positionright != None and
                  positionright.pit):
                if agent.linecurrent < 3:
                    agent.WalkUp()
                    return

        if (posperpdownleft != None and
            posperpdownleft.Sensepit):
            if (positionleft != None and
                not positionleft.pit):
                if agent.GetPosition(agent.linecurrent-1, agent.columncurrent) == None:
                    agent.FillMatrixAtPosition(matrix.GetPosition(agent.linecurrent-1, agent.columncurrent), agent.linecurrent-1, agent.columncurrent-1)
                    print("Pit at " + str(agent.linecurrent-1) + ", " + str(agent.columncurrent) )
                     
                if agent.currentdirection == 3:
                    agent.WalkRight()
                    return
                elif agent.columncurrent > 0:
                    agent.WalkLeft()
                    return
            elif (positionleft != None and
                  positionleft.pit):
                if agent.linecurrent > 0:
                    agent.WalkDown()
                    return
            else:
                if agent.GetPosition(agent.linecurrent, agent.columncurrent-1) == None:
                    agent.FillMatrixAtPosition(matrix.GetPosition(agent.linecurrent, agent.columncurrent-1), agent.linecurrent-1, agent.columncurrent-1)
                    print("Pit at " + str(agent.linecurrent) + ", " + str(agent.columncurrent-1) )
                     
                if agent.currentdirection == 1:
                    agent.WalkUp()
                    return
                
        if (posperpupright != None and
            posperpupright.Sensepit):
            if (positionright != None and
                not positionright.pit):
                if agent.GetPosition(agent.linecurrent+1, agent.columncurrent) == None:
                    agent.FillMatrixAtPosition(matrix.GetPosition(agent.linecurrent+1, agent.columncurrent), agent.linecurrent, agent.columncurrent+1)
                    print("Pit at " + str(agent.linecurrent+1) + ", " + str(agent.columncurrent) )
                     
                if agent.linecolumn < 3:
                    agent.WalkRight()
                    return
            elif (positionright != None and
                  positionright.pit):
                if agent.linecurrent < 3:
                    agent.WalkUp()
                    return
            elif (positionup != None and
                  not positionup.pit):
                if agent.GetPosition(agent.linecurrent, agent.columncurrent+1) == None:
                    agent.FillMatrixAtPosition(matrix.GetPosition(agent.linecurrent, agent.columncurrent+1), agent.linecurrent, agent.columncurrent+1)
                    print("Pit at " + str(agent.linecurrent) + ", " + str(agent.columncurrent+1) )
                     
                if agent.linecurrent < 3:
                    agent.WalkUp()
                    return
            
        if (positionleft != None and
            not positionleft.pit):
            agent.WalkLeft()
        elif (positionright != None and
            not positionright.pit):
            agent.WalkRight()
        elif (positiondown != None and
            not positiondown.pit):
            agent.WalkDown()
        elif (positionup != None and
            not positionup.pit):
            agent.WalkUp()

gameNotOver = True
agent = agent()
matrix = matrix()
matrix.InitializematrixMatrix()
agent.InitializematrixMatrix()