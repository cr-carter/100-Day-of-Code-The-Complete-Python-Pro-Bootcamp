#There was no project this day as part of the course.
#It was simply exercises finding bugs inside of short snippets of code.

#For example, I had to find a bug in this code, which was fairly easy to find:
# Which number do you want to check?
number = int(input())

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#The issue of course is that a single equal sign (=) should not be used in the if statement,
#it should be a double equal sign (==)

#Another example is this code, whose bug was revealed as soon as I ran the code:
year = input() # Which year do you want to check?

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

#The issue is clearly that the variable "year" is stored as a string, and therefore
#cannot have mathematical operations performed on it in the if statements.
