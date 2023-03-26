# Name: Yunhee Cho 
# SBUID: 115935503

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius (fahrenheit): #user input function
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
#No else statement

def what_to_wear(celsius):

    if celsius < -10:
        return "Wear a puffy jacket"
    elif -10 <= celsius <= 0:
        return "Wear a scarf"
    elif 0 <= celsius <= 10:
        return "Wear a sweater"
    elif 10 <= celsius <= 20:
        return "Wear a light Jacket"
    elif celsius > 20:
        return "Wear a T-shirt"
    
    #This function is fruitful because it returns a value, which is the type of clothing in this case.
    
fahrenheit = float(input("Enter the temperature in fahrenheit: "))
celsius = fahrenheit2celsius(fahrenheit)
print("The temperature in celsius is: ", + float(celsius))
clothing = what_to_wear(celsius)
print(clothing)
    



# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

'''def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    ...

def euclidean_distance(x1, y1, x2, y2):
    ...

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    ...


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


def deg2rad(deg):
    ...

def apothem(number_sides, length_side):
   ...

def polygon_area(number_sides, length_side):'''


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

'''# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))'''

