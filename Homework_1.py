# Name: Yunhee Cho 
# SBUID: 115935503

##################### SCORE ######################
####### Score:  6/10
#################################################

# Remove the ellipses (...) when writing your solutions.
# your output:
# (base) D:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27>D:/anaconda/python.exe "d:/CSE 101 Ass1/Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27/yunheecho7/Homework_1.py"
# Enter the temperature in fahrenheit: 44
# The temperature in celsius is:  6.666666666666667
# You need to wear a:  Sweater--> correct
# x1: -4
# x2: -4
# x3: -5
# y1: 5
# y2: 3
# y3: -3
# The perimeter of a triangle is:  16 --> wrong
# The area of a triangle is:  1
# Enter the side: 5
# Enter the length side 4
# The area of the regular polygon is:  27.527638409423474 --> correct
# The area of the triangle is : 32 , its perimeter is : 16--> wrong
# The area of the polygon is : 32--> wrong
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius (fahrenheit): #user input function
    celsius = (fahrenheit - 32) * (5 / 9) #The formula used in converting from fahrenheit to celsius
    return celsius


def what_to_wear(celsius):

    if celsius < -10: #if the given celsius is less than -10 degrees, then the user needs to wear a puffy jacket
        return "Puffy jacket"
    elif -10 <= celsius <= 0: #...less than or equal to 0 degrees,...a scarf
        return "Scarf"
    elif 0 <= celsius <= 10: #...less than or equal to 10 degrees,...a sweater
        return "Sweater"
    elif 10 <= celsius <= 20: #...less than or equal to 20 degrees,...a light jacket
        return "Light Jacket"
    elif celsius > 20: #...greater than 20 degrees,...a t-shirt
        return "T-shirt"
    


fahrenheit = float(input("Enter the temperature in fahrenheit: "))

#Calling functions fahrenheit2celsius and what_to_wear (this is where I got stuck the most for this exercise because I didn't know how to call them)
celsius = fahrenheit2celsius(fahrenheit)
clothing = what_to_wear(celsius)

print("The temperature in celsius is: ", str(celsius)) #prints out the temperature after converting from fahrenheit
print("You need to wear a: ", clothing) #prints out the clothing the user needs to wear given the temperature in celsius 

#This function is fruitful because it returns a value, which is the type of clothing in this case.


# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    A = abs((x1 * y2 + x2 * y3 + x3 * y1) - (x1 * y3 + x2 * y1 + x3 * y2)) / 2 #Formula for solving area of a triangle
    return int(A)


def euclidean_distance(x1, y1, x2, y2):
    d = (((x1 - x2)) ** 2 + (y1 - y2) ** 2) ** 0.5 #Formula for the euclidean distance
    return d
    

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    P = s1 + s2 + s3 #The formula for the perimeter of a triangle ## from where do you get s????
    return int(P)

x1 = int(input("x1: "))
x2 = int(input("x2: "))
x3 = int(input("x3: "))
y1 = int(input("y1: "))
y2 = int(input("y2: "))
y3 = int(input("y3: "))

s1 = euclidean_distance(x1, y1, x2, y2) #The distance obtained from x1, y1, x2, y2 using the euclidean distance formula
s2 = euclidean_distance(x2, y2, x3, y3) #...from x2, y2, x3, y3 ...
s3 = euclidean_distance(x3, y3, x1, y1) #...from x3, y3, x1, y1 ...

#Calling functions compute_triangle_perimeter and shoelace_triangle_area 
P = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
A = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)

print("The perimeter of a triangle is: ", str(P)) #prints out the perimeter of a triangle
print("The area of a triangle is: " , str(A)) #prints out the area of a triangle

# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

#import math module for tan and pi
from math import tan, pi

def deg2rad(deg):
    return deg * (pi / 180) #conversion from degrees to radians

def apothem(number_sides, length_side): 
    return a 

def polygon_area(number_sides, length_side):
    return area

number_sides = int(input("Enter the side: ")) #user inputs the value for the side
length_side = int(input("Enter the length side ")) #user inputs the value for the side of a length
a = length_side / (2 * tan(pi / number_sides)) # formula for the apothem, a,  defined in def polygon area
area = (number_sides * length_side * a) / 2 #formula for the area of a regular polygon,defined in the function def polygon_area
print("The area of the regular polygon is: ", str(area)) #prints out the area of a polygon after inputing side length and side

# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.'''

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter))

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

