import math # Importing math built in module 

radius = float(input("Please input the radius: ")) # assign radius to user input value, must be bracked by float because input value can be float or int not string. 

diameter = radius*2   # assign variable diameter with radius times two 

purple_area = diameter*radius/2 # get the area of purple with triangle formula with diameter as base and radius as height of triangle. Formula is: base*radius/2

yellow_area = math.pi*radius**2 # get the area of yellow with circle formula with math.pi(called from math module) --> the mathematical constant π = 3.141592, phi*radius**2 

red_area = diameter**2 # get the area of red with square formula with diameter as rectangle side. Formulas is side**2 

print('\n================================\n')

print(f'Area of red area: {(red_area - yellow_area):.2f}') # print the only red area two decimal format using python formatted string(source: w3schools.com), we still need to subtract with yellow area
print(f'Area of yellow area: {(yellow_area - purple_area):.2f}') # print the only yellow area two decimal format using python formatted string(source: w3schools.com), we still need to subtract with purple area
print(f'Area of purple area: {purple_area:.2f}') # print the purple area with two decimal format using python formatted string(source: w3schools.com).

print('\n================================')