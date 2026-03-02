# I was supposed to put a comment here
# My Last Name


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod1 = float(input('Enter grade for Module 1: '))
mod2 = float(input('Enter grade for Module 2: '))
mod3 = float(input('Enter grade for Module 3: '))
mod4 = float(input('Enter grade for Module 4: '))
mod5 = float(input('Enter grade for Module 5: '))
mod6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod1, mod2, mod3, mod4, mod5]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = total / len(grades)

# determine letter grade for average


if avg >= 90:
    letter_grade ='A'
elif avg >= 80:
    letter_grade ='B'
elif avg >= 70:
    letter_grade ='c'
elif avg >= 60:
    letter_grade ='D'

else:
    letter_grade ='F'

# Display results
print("\n------------Results------------")
print(f"Lowest Grade: {low:.1f}")
print(f"Highest Grade: {high:.1f}")
print(f"Sum of Grades: {sum:.1f}")
print(f"Average: {avg:.2f}")
print("----------------------------------------------")

print(f"Your grade is: {letter_grade} ")




