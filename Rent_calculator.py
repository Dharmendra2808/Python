# user input 
# total rent
# Room rent
# Electricity units used
# Electricity per unit used
# No. of roommates
# Each one should pay :    

rent=int(input("Enter room rent : "))
Electricity_bill=int(input("Electricity unit used :"))
Charge_per_unit=int(input("Electric charge per unit : "))
Roomate=int(input("No. of roommates : "))

Total_bill=Electricity_bill*Charge_per_unit
Each_tenants_should_pay=(rent+Total_bill)//Roomate 
print(f"Each one should pay : {Each_tenants_should_pay}")
