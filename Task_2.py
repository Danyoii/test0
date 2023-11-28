#Задание №2
from drawbot_skia.drawbot import rect, saveImage

length = 50
width = 50
distance = 100
rows = 10
cols = 10
grid_distance_x = 200 

start_x = 0
start_y = 0

for i in range(rows):
    for j in range(cols):
        rect(start_x + j * distance, start_y + i * distance, length, width)

start_x += grid_distance_x

for i in range(rows):
    for j in range(cols):
        rect(start_x + j * distance, start_y + i * distance, length, width)

saveImage("Task_2.pdf")
