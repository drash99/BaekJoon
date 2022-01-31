isinloop = True
gamenumber = 0
while isinloop:
    inplen = int(input().split(' ')[0])
    if inplen == 0:
        isinloop = False
        break
    gamenumber += 1
    targetchar = ['+', 'B', 'W']

    mapinput = []
    maptarget = []
    currentpos = [0,0]

    for i in range(inplen):
        mapinput.append(list(input().strip()))
        for j in range(len(mapinput[-1])):
            if mapinput[i][j] in targetchar:
                maptarget.append((i,j))
            if mapinput[i][j] in ['w', 'W']:
                currentpos = [i,j]


    commands = list(input().strip())

    def movebox(mapstatus, boxpos, direction):
        if direction == 'U':
            if mapstatus[boxpos[0]-1][boxpos[1]] in ['#', 'B', 'b']:
                return -1
            else:
                mapstatus[boxpos[0]-1][boxpos[1]] = 'b'
                mapstatus[boxpos[0]][boxpos[1]] = '.'
                return 0
            
        elif direction == 'D':
            if mapstatus[boxpos[0]+1][boxpos[1]] in ['#', 'B', 'b']:
                return -1
            else:
                mapstatus[boxpos[0]+1][boxpos[1]] = 'b'
                mapstatus[boxpos[0]][boxpos[1]] = '.'
                return 0
            
        elif direction == 'L':
            if mapstatus[boxpos[0]][boxpos[1]-1] in ['#', 'B', 'b']:
                return -1
            else:
                mapstatus[boxpos[0]][boxpos[1]-1] = 'b'
                mapstatus[boxpos[0]][boxpos[1]] = '.'
                return 0
            
        elif direction == 'R':
            if mapstatus[boxpos[0]][boxpos[1]+1] in ['#', 'B', 'b']:
                return -1
            else:
                mapstatus[boxpos[0]][boxpos[1]+1] = 'b'
                mapstatus[boxpos[0]][boxpos[1]] = '.'
                return 0

        
    def movechar(mapstatus, currentpos, direction):
        if direction == 'U':
            if mapstatus[currentpos[0]-1][currentpos[1]] == '#':
                return currentpos
            
            elif mapstatus[currentpos[0]-1][currentpos[1]] in  ['B','b']:
                if movebox(mapstatus, [currentpos[0]-1, currentpos[1]], 'U') != 0:    
                    return currentpos
            mapstatus[currentpos[0]-1][currentpos[1]] = 'w'
            mapstatus[currentpos[0]][currentpos[1]] = '.'
            currentpos[0] -= 1
            return currentpos
        
        elif direction == 'D':
            if mapstatus[currentpos[0]+1][currentpos[1]] == '#':
                return currentpos
            
            elif mapstatus[currentpos[0]+1][currentpos[1]] in  ['B','b']:
                if movebox(mapstatus, [currentpos[0]+1, currentpos[1]], 'D') != 0:    
                    return currentpos
            mapstatus[currentpos[0]+1][currentpos[1]] = 'w'
            mapstatus[currentpos[0]][currentpos[1]] = '.'
            currentpos[0] += 1
            return currentpos

        elif direction == 'L':
            if mapstatus[currentpos[0]][currentpos[1]-1] == '#':
                return currentpos
            
            elif mapstatus[currentpos[0]][currentpos[1]-1] in  ['B','b']:
                if movebox(mapstatus, [currentpos[0], currentpos[1]-1], 'L') != 0:    
                    return currentpos
            mapstatus[currentpos[0]][currentpos[1]-1] = 'w'
            mapstatus[currentpos[0]][currentpos[1]] = '.'
            currentpos[1] -= 1
            return currentpos

        elif direction == 'R':
            if mapstatus[currentpos[0]][currentpos[1]+1] == '#':
                return currentpos
            
            elif mapstatus[currentpos[0]][currentpos[1]+1] in  ['B','b']:
                if movebox(mapstatus, [currentpos[0], currentpos[1]+1], 'R') != 0:    
                    return currentpos
            mapstatus[currentpos[0]][currentpos[1]+1] = 'w'
            mapstatus[currentpos[0]][currentpos[1]] = '.'
            currentpos[1] += 1
            return currentpos
        else:
            return currentpos

    def checkcomplete(mapstatus):  
        iscomplete = True
        for target in maptarget:
            if mapstatus[target[0]][target[1]] == 'w':
                mapstatus[target[0]][target[1]] = 'W'
                iscomplete = False
            elif mapstatus[target[0]][target[1]] == 'b':
                mapstatus[target[0]][target[1]] = 'B'
            elif mapstatus[target[0]][target[1]] in ['+','.']:
                mapstatus[target[0]][target[1]] = '+'
                iscomplete = False
        return iscomplete

    completed = False
    for command in commands:
        movechar(mapinput,currentpos, command)
        if checkcomplete(mapinput):
            completed = True
            break

    if completed:
        print("Game "+str(gamenumber)+": complete")
    else:
        print("Game "+str(gamenumber)+": incomplete")
    for i in mapinput:
        print(''.join(i))
          


