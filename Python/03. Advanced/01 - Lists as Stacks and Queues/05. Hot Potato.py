from collections import deque

kids = deque(input().split())
n = int(input())
turns = 0

while len(kids) > 1:
    for i in range(n-1):
        # Get first kid on the line
        first_kid = kids.popleft()
        # Move the kid in the end
        kids.append(first_kid)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.popleft()}")


