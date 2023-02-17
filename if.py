x=1
marks=67
grades=89
#if statement
if x>=0:
    print("the number is positive")
    print(4+10)

#if...else statement
if marks>=60:
    print("you have passed")
else:
    print("you have failed")

#if...elif...else statement
if grades>=80 and grades<=100:
    print("grade A")
elif grades>=70 and grades<=79:
    print("grade B")
elif grades>=60 and grades<=69:
    print("grade C+")
elif grades>=50 and grades<=59:
    print("grade C")
elif grades>=40 and grades<=49:
    print("grade D+")
else:
    print("failed")