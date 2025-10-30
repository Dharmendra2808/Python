'''year=int(input("Enter year : "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("it's a leap year ")
        else:
            print("it is not a leap year ")
    else:
        print("it is not a leap year ")
else:
    print("it is not a leap year") '''
# The above code has nested loops if there is a code for same logic then we have to use some thing called elif

year = int(input("Enter year : "))
if year%400==0 and year%100==0:
    print(f"Hence the year {year} is a leap year ")
elif year%4==0 and year%100!=0:
    print(f"Hence this year {year} is a leap year")
else:
    print(f"The above year {year} is not a leap year ")