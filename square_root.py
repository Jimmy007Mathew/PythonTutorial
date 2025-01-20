num=int(input("Enter the number:"))

guess= num/2
while(abs(guess*guess - num) >= 0.00000001):
    guess=guess -(guess **2 -num)/(2*guess)


print(round(guess,5))