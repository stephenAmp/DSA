"""
BINARY SEARCH - Effective with sorted arrays or continuous functions
Involves dividing input size into two if search target is in left ignore right
if in right ignore left. Saves time  Time complexity of O(logn)
STEPS
- Calculate middle index of the list: (lowest index + highest index) / 2
- if value of middle index is greater than target, ignore the  right half of the list
- if value of middle index is less than trget, ignore left half of the list
- Repeat these steps until length of search interval becomes less or equal to 1
- Check if data[left] equals target. if yes target value is acquired. Else target value does not exist in list.
"""

#BAD CODE time complexity of O n(log n)
def binary_search(target,list):
    sorted_list = sorted(list)
    middle_index = len(list)// 2
    left_part = sorted_list[:middle_index]
    right_part = sorted_list[middle_index:]
    if target == middle_index:
        return target
    elif target > middle_index:
        for item in right_part:
            if item == target:
                return target
            else:
                pass
    else:
        for item in left_part:
            if item == target:
                return target
    return 'item not in list'
list1 = [2,4,6,7,8,9,10,12]
target= 9
print(binary_search(target,list1))


# GOOD CODE No recursion no extra spaces time complexity of O(log n)


def binary_search_iterative(data, target):


    # We will search in the interval [low, high), where the right border is excluded
    low = 0
    high = len(data)

    while high - low > 1: # search until the length of the interval < 1
        mid = (low + high) // 2
        if target < data[mid]:
            high = mid # Continue our search in [low, mid)
        else:
            low = mid # Continue our search in [mid, high)
    return low if data[low] == target else None


def binary_search(list,target)->int:
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (high + low) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None 

"""Using recursion for binary search"""


def binary_search_recursive(data, target, low, high):
    if high - low <= 1:
        return low if data[low] == target else None
    mid = (low + high) // 2
    if target < data[mid]:
        return binary_search_recursive(data, target, low, mid)
    else:
        return binary_search_recursive(data, target, mid, high)
    

"""Bonus Exercise: Binary Search to Solve an Advanced Problem
With a clear understanding of binary search, we can now use it to solve a complex problem — searching for a target element in a rotated sorted list. This involves figuring out the rotation point and applying binary search accordingly.

Consider a list like this [7, 8, 9, 2, 3, 4]. This list was sorted from 2 to 9, but then it was rotated to the fourth position. Suppose we want to search for the number 3. We can see that it's in the latter half, but how does our algorithm determine this?"""

#APPLYING BINARY SEARCH
# Implementation of Binary Search on a specific use case

# List of sorted products' prices in an e-commerce company
products_price = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

def binary_search_iterative(data, target):
    low = 0
    high = len(data)
    while high - low > 1:
        mid = (low + high) // 2
        if target < data[mid]:
            high = mid 
        elif target > data[mid]:
            low = mid 
        else:  # if target is equal to data[mid]
            return mid
    return low if data[low] == target else None

def search_price(customer_query):
    result = binary_search_iterative(products_price, customer_query)
    if result is not None:
        print(f"Product of price ${customer_query} is found at position {result} in the price list.")
    else:
        print(f"No product is found with price ${customer_query}.")

# Searching for a price that exists
search_price(30)

# Searching for a price that doesn't exist
search_price(31)    


"""Binary Search involving continuous fn"""
# Define the function
def f(x):
    return x * x - 2

# Define the binary search function 
def binary_search(target, left, right, precision):
    while right - left > precision:
        mid = (left + right) / 2
        if f(mid) < target: # If the midpoint value is less than the target...
            left = mid  # ...update the left boundary to be the midpoint.
        else:
            right = mid  # Otherwise, update the right boundary.
    return left # Return the left boundary of our final, narrow interval.

epsilon = 1e-6
result = binary_search(0, 1, 2, epsilon)
print("x for which f(x) is approximately 0:", result)

# Outputs:
# x for which f(x) is approximately 0: 1.4142131805419922

"""BINARY SEARCH ON CONTINUOUS FUNCTIONS"""
# Define the function
def f(x):
    return x * x - 2

# Define the binary search function 
def binary_search(target, left, right, precision):
    while right - left > precision:
        mid = (left + right) / 2
        if f(mid) < target: # If the midpoint value is less than the target...
            left = mid  # ...update the left boundary to be the midpoint.
        else:
            right = mid  # Otherwise, update the right boundary.
    return left # Return the left boundary of our final, narrow interval.

epsilon = 1e-6
result = binary_search(0, 1, 2, epsilon)
print("x for which f(x) is approximately 0:", result)

# Outputs:
# x for which f(x) is approximately 0: 1.4142131805419922


"""Applying the Technique to a Complex Problem"""
# With this newly acquired knowledge, we open up a vast range of possibilities to solve complex problems. For example, suppose we need to solve a problem in physics where we need to determine at which time (t), the velocity function V(t) = 9.81*t -0.65*t^2


# Python program to calculate the point at which a ball dropped from a height h reaches the ground 
# using Binary Search on the continuous function h(t) = h - (1/2) * g * t^2.

import math

# Define the continuous function for the height of the ball at time t 
def h(t, initial_height, g):
    return initial_height - (0.5) * g * t**2

# Define the binary search function
def binary_search(func, initial_height, g, target, left, right, precision):
    while right - left > precision:
        mid = (left + right) / 2
        if func(mid, initial_height, g) < target:
            right = mid
        else:
            left = mid
    return (left + right) / 2

# Requested precision
epsilon = 1e-6
# Constants
initial_height = 100  # Initial height in meters
g = 9.81  # acceleration due to gravity

# Time range 
time_range = [0, 10]

# Call binary_search for h with the target being 0, indicating the hit of the ground
result = binary_search(h, initial_height, g, 0, time_range[0], time_range[1], epsilon)

print("Time when the ball hits the ground (seconds): ", result)


# Python program to find the root of a given function using Binary Search
import math
import numpy as np

# Define a continuous function 'f' where f(x) = x^4 - x^2 - 10
def f(x):
    return x**4 - x**2 - 10

# Define the binary search function 
def binary_search(func, target, left, right, precision):
    while np.abs(func(left)) > precision and np.abs(func(right)) > precision:
        middle = (left + right) / 2
        if func(middle) < target:
            left = middle
        else:
            right = middle
            
    return middle

epsilon = 1e-6  # to make sure the solution is within an acceptable range
target = 0  # target value for root of function 'f'
start = -5  # starting point of the interval
end = 5  # ending point of the interval

result = binary_search(f, target, start, end, epsilon)
print("The value of x for which f(x) is approximately 0 within the interval [" + str(start) + ", " + str(end) + "] is: ", result)






# Python program to find the root of a given function using Binary Search
import math
import numpy as np

# Define a continuous function 'f' where f(x) = x^4 - x^2 - 10
def f(x):
    return x**4 - x**2 - 10

# Define the binary search function 
def binary_search(func, target, left, right, precision):
    while np.abs(func(left)) > precision and np.abs(func(right)) > precision:
        middle = (left + right) / 2
        if func(middle) < target:
            left = middle
        else:
            right = middle
            
    return middle

epsilon = 1e-6  # to make sure the solution is within an acceptable range
target = 50  # target value for root of function 'f'
start = -5  # starting point of the interval
end = 5  # ending point of the interval

result = binary_search(f, target, start, end, epsilon)
print("The value of x for which f(x) is approximately 0 within the interval [" + str(start) + ", " + str(end) + "] is: ", result)







# Python program to find the value of 'x' when f(x) = 0 using Binary Search on Continuous Space
import math

# Define a continuous function 'f'
def f(x):
    return x**3 - 5 * x**2 + 5

# TODO: Write the Binary Search Function that performs the search on the continuous function in the interval [2, 5]


def perform_binary_search(func, target, right, left, precision):
    while right - left > precision:
        middle = (right + left) / 2
        if func(middle) > target:
            right = middle
        else:
            left = middle
    return (right + left) / 2
# TODO: Define precision, target value, and interval bounds
precision = 1e-6
target = 0 
interval = [2,5]
left = interval[0]
right = interval[1]

print(perform_binary_search(f,target,right,left,precision))
