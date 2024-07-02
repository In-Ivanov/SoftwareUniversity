from collections import deque

man = deque([int(x) for x in input().split()])
pie = [int(x) for x in input().split()]

count = 0

while man and pie:

    if man[0] >= pie[-1]:
        if man[0] == pie[-1]:
            man.popleft()
            pie.pop()
        else:
            man[0] = man[0] - pie[-1]
            man.append(man[0])
            man.popleft()
            pie.pop()
    else:
        pie[-1] = pie[-1] - man[0]
        man.popleft()


if not pie:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(c) for c in man)}")
elif not man:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(p) for p in pie)}")
else:
    print("We have a champion!")
