from gpiozero import LEDCharDisplay
from time import sleep

display = LEDCharDisplay (26, 19, 13, 6, 5, 21, 20, active_high = True) #display tens
display2 = LEDCharDisplay (2, 3, 24, 17, 14, 15, 18, active_high = True) #display ones

num = 22

for i in range(num,0,-1):
    if i >= 10:
    
        display.value = str(i)[0]
        display2.value = str(i)[1]
        print(str(i))
        sleep(1)
    elif i < 10:
        display.off()
        print(str(i)[0])
        
        display2.value = str(i)[0]
        sleep(1)

display.off()
display2.off()
        
# while True:
#     for char in '0123456789':
#         display2.value = char
#         sleep(1)