# Write a program to calculate simple interest
# input 
# enter principal:1300
# enter rate (per year ):  5
# enter time (in years) : 4

## Total Interest 
## Total amount to pay :
Principal=int(input("Your Principal amount : "))
Rate_of_interest=int(input("Enter rate [per year] : "))
Time_taken=int(input ("Enter time Span [in years]:"))

Simple_interest=(Principal*Rate_of_interest*Time_taken)/100
Total_amount=Simple_interest+Principal
print("Your Simple Intereset : ",Simple_interest)
print("Total Amount is : ",Total_amount)