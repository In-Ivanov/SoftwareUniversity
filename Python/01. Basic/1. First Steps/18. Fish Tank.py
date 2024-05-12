lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_aqua = lenght * width * height
volume_litres = volume_aqua * 0.001
space = percent / 100
litres = volume_litres * (1 - space)

print(litres)
