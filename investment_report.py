print("INVESTMENT REPORT\n------------------")
princ=int(input("Enter the principle Amount:"))
time=int(input("Enter the duration in years:"))
rate=float(input("Enter the interest rate:"))
print("Year    Interest            Total\n-------------------------------------")

for i in range(1,time+1):
    interest=princ*rate/100
    princ=princ+interest
    print("%-8d%-20.3f%-20.4f" % (i,interest,princ))
print("-------------------------------------\nTotal amount accumulated: Rs %-20.3f " % princ)
