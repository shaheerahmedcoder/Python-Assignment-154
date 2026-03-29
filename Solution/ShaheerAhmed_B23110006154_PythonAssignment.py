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




# --- Q1: Numbers divisible by 7 and multiple of 5, between 1500 and 2700 ---

# --- Q1: Numbers divisible by 7 and multiple of 5, between 1500 and 2700 ---

# --- Q1: Numbers divisible by 7 and multiple of 5, between 1500 and 2700 ---

# --- Q1: Numbers divisible by 7 and multiple of 5, between 1500 and 2700 ---

# --- Q1: Numbers divisible by 7 and multiple of 5, between 1500 and 2700 ---
