from cs50 import get_string

text = get_string("Text: ")
letters = words = sentences = 0

for character in text:
   if character.isalpha():
       letters += 1
   elif character.isspace():
       words += 1
   elif character in ['.', '!', '?']:
       sentences += 1

L = letters / words * 100
S = sentences / words * 100

index = 0.0588 * L - 0.296 * S - 15.8
grade = round(index)

if grade >= 16:
   print("Grade 16+")
elif grade < 1:
   print("Before Grade 1")
else:
   print(f"Grade {grade}")