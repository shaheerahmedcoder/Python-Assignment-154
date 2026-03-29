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



