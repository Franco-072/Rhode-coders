# List of scores for a student
scores = [90,100,80]

total = 0

# loop to add up all the scores
for grade in scores:
    total += grade

# Calculate the average (final score)
average = total / len(scores)

grade = ()

# Determine the grade based on the average score
# This is according to Colloge Simply

if 96 <= average <= 100:
    grade = "A+"
elif 92 <= average < 96:   
    grade = "A"
elif 90 <= average < 92:
    grade = "A-"
elif 86 <= average < 90:
    grade = "B+"
elif 82 <= average < 86:
    grade = "B"
elif 80 <= average < 82:
    grade = "B-"
elif 76 <= average < 80:   
    grade = "C+"
elif 72 <= average < 76:
    grade = "C"
elif 70 <= average < 72:
    grade = "C-"
elif 66 <= average < 70:
    grade = "D+"
elif 62 <= average < 66:
    grade = "D"
elif 60 <= average < 62:
    grade = "D-"
else:
    grade = "F" 

# print
print("Scores:", scores)
print("Final Score:", average)
print("Grade:", grade)
