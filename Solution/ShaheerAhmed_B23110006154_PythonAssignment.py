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

# ------------------------------
# Section 2: Function Questions(In pdf for loop questions was written and the questions was more towards funtions concept thats why i changed section(2) heading by myself)
# ------------------------------

# --- Q1: Area of Rectangle --- 
def ra(length, width):
    return length * width
print(ra(2, 3))

# --- Q2: Even and Odd ---
def ev_od(n):
    if n % 2 == 0:
        return "even"
    return "odd"
 
print(ev_od(2))   
print(ev_od(5))   

# --- Q3: Reverse a String ---
def revstr(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev
 
print(revstr("shaheer")) 

# --- Q4: Sum of all Digits---
def sumdig(n):
    n = abs(n)   
    t = 0
    for d in str(n):
        t += int(d)
    return t
 
print(sumdig(154))   # 10

# --- Q5: Prime number check---
def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
 
print(prime(154))    
print(prime(7))   

# --- Q6:  Fibonacci Series prob. ---
def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    
fib(8)   

# --- Q7:  Counting the vowels prob. ---
def vow(s):
    count = 0
    for i in s.lower():
        if i in "aeiou":
            count = count + 1
    return count
 
print(vow("shaheer ahmed"))   

# --- Q8: Power without pow() or anyy operator ---
def pow(baseVal, exp):
    res = 1
    for i in range(exp):
        res = res * baseVal
    return res
 
print(pow(5, 2))   

