N = int(input())

stacks = []
for i in range(N):
    line = input()
    if line.startswith('pu'):
        stacks.append(line[1])
    elif line.startswith('po'):
        if len(stacks) !=0:
            print(stacks.pop(0))
        else:
            print(-1)
    elif line.startswith('s'):
        print(len(stacks))
    elif line[0].startswith('f'):
        if len(stacks) !=0:
            print(stacks[0])
        else:
            print(-1)
    elif line[0].startswith('b'):
        if len(stacks) !=0:
            print(stacks[-1])
        else:
            print(-1)
    elif line[0].startswith('e'):
        if len(stacks) !=0:
            print(0)
        else:
            print(1)
    
    