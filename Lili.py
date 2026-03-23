# Name: Lili
# Project: Python Exercises
# Exercises 1–30

# -------------------------
# Exercise 1
# -------------------------
print("Hello, Python!")

# -------------------------
# Exercise 2
# -------------------------
name = "Lili"
age = 18
print("Name:", name, "Age:", age)

# -------------------------
# Exercise 3
# -------------------------
user_input = input("Enter something: ")
print("You entered:", user_input)

# -------------------------
# Exercise 4
# -------------------------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

# -------------------------
# Exercise 5
# -------------------------
print("Subtract:", num1 - num2)
print("Multiply:", num1 * num2)
print("Divide:", num1 / num2)

# -------------------------
# Exercise 6
# -------------------------
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# -------------------------
# Exercise 7
# -------------------------
minutes = int(input("Enter minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(hours, "hours and", remaining_minutes, "minutes")

# -------------------------
# Exercise 8
# -------------------------
n = int(input("Enter a number: "))
print("Square:", n ** 2)
print("Cube:", n ** 3)

# -------------------------
# Exercise 9
# -------------------------
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Swap using temporary variable
temp = a
a = b
b = temp
print("After swap (with temp): a =", a, ", b =", b)

# Swap without temporary variable
a, b = b, a
print("After swap (without temp): a =", a, ", b =", b)

# -------------------------
# Exercise 10
# -------------------------
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle:", area)
 
# 11. Even or odd
n = int(input("Enter number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# 12. Largest of three numbers
a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))

# 13. Print numbers 1 to n
n = int(input())
for i in range(1, n+1):
    print(i)

# 14. Print odd numbers 1–50
for i in range(1, 51):
    if i % 2 != 0:
        print(i)

# 15. Factorial
n = int(input())
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

# 16. Multiplication table
n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

# 17. Count digits
n = input()
print(len(n))

# 18. Reverse a number
n = input()
print(n[::-1])

# 19. Palindrome number
n = input()
if n == n[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# 20. Sum of digits
n = input()
total = 0
for digit in n:
    total += int(digit)
print(total)

# 21. Count vowels
s = input("Enter string: ")
count = 0
for ch in s.lower():
    if ch in "aeiou":
        count += 1
print(count)

# 22. Reverse string
s = input()
print(s[::-1])

# 23. Palindrome string
s = input()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# 24. Remove spaces
s = input()
print(s.replace(" ", ""))

# 25. Length of list without len()
lst = [1, 2, 3, 4]
count = 0
for i in lst:
    count += 1
print(count)

# 26. Largest in list
lst = [3, 7, 2, 9, 5]
largest = lst[0]
for num in lst:
    if num > largest:
        largest = num
print(largest)

# 27. Smallest in list
smallest = lst[0]
for num in lst:
    if num < smallest:
        smallest = num
print(smallest)

# 28. Remove duplicates
lst = [1, 2, 2, 3, 4, 4]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print(unique)

# 29. Manual sort (bubble sort)
lst = [5, 2, 9, 1]
for i in range(len(lst)):
    for j in range(0, len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)

# 30. Second largest number
lst = [10, 20, 4, 45, 99]
lst = list(set(lst))  # remove duplicates
lst.sort()
print(lst[-2])