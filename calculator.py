#!/usr/bin/env python
# coding: utf-8

# # Calculator

# In[10]:


def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1, 2, 3, or 4): ")
if choice == '1':
    result = add(num1, num2)
    operation = "Addition"
elif choice == '2':
    result = subtract(num1, num2)
    operation = "Subtraction"
elif choice == '3':
    result = multiply(num1, num2)
    operation = "Multiplication"
elif choice == '4':
    result = divide(num1, num2)
    operation = "Division"
else:
    result = "Error: Invalid Input"
    operation = "Invalid Operation"
print(f"{operation} result: {result}")



# In[ ]:




