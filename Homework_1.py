# Name: Yunhee Cho 
# SBUID: 115935503

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius (fahrenheit): #user input function
    celsius = (fahrenheit - 32) * (5 / 9) #The formula used in converting from fahrenheit to celsius
    return celsius


def what_to_wear(celsius):

    if celsius < -10:
        return "Puffy jacket"
    elif -10 <= celsius <= 0:
        return "Scarf"
    elif 0 <= celsius <= 10:
        return "Sweater"
    elif 10 <= celsius <= 20:
        return "Light Jacket"
    elif celsius > 20:
        return "T-shirt"
    
#Calling functions fahrenheit2celsius and what_to_wear (this is where I got stuck the most for this exercise because I didn't know how to call them)

fahrenheit = float(input("Enter the temperature in fahrenheit: "))
celsius = fahrenheit2celsius(fahrenheit)
clothing = what_to_wear(celsius)
print("The temperature in celsius is: ", str(celsius))
print("You need to wear a: ", clothing)

#This function is fruitful because it returns a value, which is the type of clothing in this case.


# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):

    area = abs((x1 * y2 + x2 * y3 + x3 * y1) - (x1 * y3 + x2 * y1 + x3 * y2)) / 2 #Formula for solving area of a triangle
    return area 


def euclidean_distance(x1, y1, x2, y2):
   
    euclidean_distance = (((x1 - x2)) ** 2 + (y1 - y2) ** 2) ** 0.5 #Formula for the euclidean distance
    return euclidean_distance

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    s1 = euclidean_distance(x1, y1, x2, y2) #The distance obtained from x1, y1, x2, y2 after using the euclidean distance formula
    s2 = euclidean_distance(x2, y2, x3, y3) #...from x2, y2, x3, y3 ...
    s3 = euclidean_distance(x3, y3, x1, y1) #...from x3, y3, x1, y1 ...

    P = s1 + s2 + s3 #The formula for the perimeter of a triangle
    return P

x1 = int(input("x1: "))
x2 = int(input("x2: "))
x3 = int(input("x3: "))
y1 = int(input("y1: "))
y2 = int(input("y2: "))
y3 = int(input("y3: "))

s1 = euclidean_distance(x1, y1, x2, y2) 
s2 = euclidean_distance(x2, y2, x3, y3) 
s3 = euclidean_distance(x3, y3, x1, y1)

P = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
print("The perimeter of a triangle is: ", str(P))
print("The area of a triangle is: " , str(area))

# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

from math import tan, pi

def deg2rad(deg):
    return deg * (pi / 180)

def apothem(number_sides, length_side):
   
    return a

def polygon_area(number_sides, length_side):
    
    return area

number_sides = int(input("Enter the side: "))
length_side = int(input("Enter the length side "))
a = length_side / (2 * tan(pi / number_sides))
area = (number_sides * length_side * a) / 2
print("The area of the regular polygon is: ", str(area))

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

