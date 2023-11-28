from drawbot_skia.drawbot import oval, rect, saveImage
#Задание №1#
length = 50
Width = 50
Distance = 150
start_horizontal = 0 
start_vertical = 0 

for i in range(10):
    rect(start_horizontal, start_vertical, length, Width)
    start_vertical = start_vertical + Distance
saveImage("Danya_1.pdf")
