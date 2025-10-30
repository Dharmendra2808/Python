# Chai=20
# Coffee=30
# do you need extra sugar : amount+2
# do you need rusk:amount+5
# do you need bread : amount+5

print("---------IGT Resort---------- ")
print("---- Ek Chai, Apne Man ki  ---")
print("Menu")
print("1. Chai , \n2. Coffee ")

drink=input("What would you love to drink ?")
bill=0
if drink=="Chai" or drink=="chai":
    bill+=20
elif drink=="Coffee" or drink=="coffee":
    bill+=30
    
Sugar=input("Do you want extra sugar : ")
if Sugar=='y' or Sugar=="yes":
    bill+=2

Rusk=input("Do you want rusk : ")
if Rusk=='y' or Rusk=="yes":
    bill+=5
    
Bread=input("Do you want bread : ")
if Bread=='y' or Bread=="yes":
    bill+=5
print("Bill",bill)