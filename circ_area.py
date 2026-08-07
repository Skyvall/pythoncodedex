import math




def calculate_circle_area():
    radius_input = float(input("Enter the radius of the circle: "))
    area = (radius_input ** 2) * math.pi
    return area



print ("The area of the circle is:", calculate_circle_area())
