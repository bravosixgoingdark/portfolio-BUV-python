
month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'] # List of months
monthRain = [] # List of rainfall
count = 0 # Counter
while count < 12: # Loop 12 times
    try:
        num = int(input(f'Enter the amount of rainfall of {month[count]}: ')) # Get the amount of rainfall
        monthRain.append(num)
        count += 1
    except:
        print("Input not accepted.")
highNum = max(monthRain) # Get the highest number of rainfall
blank = "   "
star = " * " # The symbol for the graph
for x in range(highNum): # Loop the highest number of rainfall times
    for y in range(len(monthRain)):
        if y == 11:
            if (monthRain[y] - highNum) < 0:
                print(blank)
                highNum = highNum - 1
            else:
                print(star)
                highNum = highNum - 1
        else:
            if (monthRain[y] - highNum) < 0:
                print(f'{blank} ', end="")
            else:
                print(f'{star} ', end="")
print(" ".join(month))


