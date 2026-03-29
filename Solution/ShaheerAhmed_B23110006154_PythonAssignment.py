# ==============================================
# Name          : Shaheer Ahmed
# Roll No       : B23110006154
# Class         : BSCS - Section A
# Assignment    : Python Practice Assignment
# Semester/Year : 5th / 3rd
# ==============================================

# ------------------------------
# Section 1: For Loop Questions
# ------------------------------

# --- Q1: Numbers divisible by 7 and multiple of 5, between 1500 and 2700 ---
ans = []
for s in range(1500, 2701):
    if s % 7 == 0 and s % 5 == 0:
        ans.append(s)
print(ans)

# --- Q2: Factorial without math.factorial() function --- 
n = int(input("enter number: "))
f = 1
for i in range(1, n+1):
    f *= i
print(f)

# --- Q3: Print each item and its type from a list  ---
datalist = [154, 11.23, 1+2j, True, 'shaheer ahmed', (3, 2), [4, 5], {"class": 'BSCS', "section": 'A'}]
for item in datalist:
    print(f"Value: {item} | Type: {type(item).__name__}")

# --- Q4: Numbers between 100-400 where every digit is even---
evens = []
for n in range(100, 401):
    digits = str(n)
    all_even = True
    for d in digits:
        if int(d) % 2 != 0:
            all_even = False
            break
    if all_even:
        evens.append(str(n))
print(",".join(evens))

# --- Q5: Print all divisors of a number ---
n = int(input("enter number: "))
divs = []
for i in range(1, n + 1):
    if n % i == 0:
        divs.append(i)
print(f"Divisors: {divs}")

# --- Q6: Common divisors of two numbers ---
a = int(input("enter first num: "))
b = int(input("enter second num: "))
 
common = []
small = min(a, b)
for i in range(1, small + 1):
    if a % i == 0 and b % i == 0:
        common.append(i)
print(f"Common divisors: {common}")

# --- Q7: HCF of two numbers ---
a = int(input("enter first num: "))
b = int(input("enter second num: "))
 
hcf = 1
small = min(a, b)
for i in range(1, small+ 1):
    if a % i == 0 and b % i == 0:
        hcf = i 
print(f"HCF = {hcf}")

# --- Q1: Numbers divisible by 7 and multiple of 5, between 1500 and 2700 ---
