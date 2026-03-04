# create a dictionary
print("\n \nWelcome to my Algorithem")
bank_customer = [
    {"customer id": "R101", "name": "John", "age": 35, "salary": 5000, "balance": 11000, "account type": "Current Account", "branch": "Main Street", "account manager": "Mark", "branch manager": "James"},
    {"customer id": "R102", "name": "Mona", "age": 28, "salary": 6000, "balance": 14000, "account type": "Current Account", "branch": "Downtown", "account manager": "Yusuf", "branch manager": "Fatima"},
    {"customer id": "R103", "name": "Khalid", "age": 40, "salary": 7500, "balance": 28000, "account type": "Current Account", "branch": "Riverside", "account manager": "Aisha", "branch manager": "Ali"},
    {"customer id": "R104", "name": "Hannah", "age": 33, "salary": 8000, "balance": 32000, "account type": "Current Account", "branch": "Westside", "account manager": "Layla", "branch manager": "Mohamed"},
    {"customer id": "R105", "name": "Omar", "age": 45, "salary": 9000, "balance": 42000, "account type": "Current Account", "branch": "Eastview", "account manager": "Kareem", "branch manager": "Nour"},
    {"customer id": "R106", "name": "Amira", "age": 29, "salary": 11000, "balance": 70000, "account type": "Current Account", "branch": "Main Street", "account manager": "Omar", "branch manager": "Hassan"},
    {"customer id": "R107", "name": "Sarah", "age": 38, "salary": 11500, "balance": 77000, "account type": "Current Account", "branch": "Downtown", "account manager": "Yusuf", "branch manager": "Fatima"},
    {"customer id": "R108", "name": "Tariq", "age": 41, "salary": 12000, "balance": 99000, "account type": "Current Account", "branch": "Riverside", "account manager": "Aisha", "branch manager": "Ali"},
    {"customer id": "R109", "name": "Nadia", "age": 36, "salary": 13000, "balance": 102000, "account type": "Current Account", "branch": "Westside", "account manager": "Layla", "branch manager": "Mohamed"},
    {"customer id": "R111", "name": "Zaid", "age": 42, "salary": 14000, "balance": 130000, "account type": "Current Account", "branch": "Eastview", "account manager": "Kareem", "branch manager": "Nour"},
    {"customer id": "R112", "name": "Hassan", "age": 50, "salary": 15500, "balance": 580000, "account type": "Current Account", "branch": "Main Street", "account manager": "Omar", "branch manager": "Hassan"},
    {"customer id": "R113", "name": "Rania", "age": 31, "salary": 16500, "balance": 800000, "account type": "Current Account", "branch": "Downtown", "account manager": "Yusuf", "branch manager": "Fatima"},
    {"customer id": "R114", "name": "Bill", "age": 48, "salary": 17500, "balance": 1020000, "account type": "Business Account", "branch": "Riverside", "account manager": "Aisha", "branch manager": "Ali"},
    {"customer id": "R115", "name": "Dina", "age": 39, "salary": 18500, "balance": 1300000, "account type": "Business Account", "branch": "Westside", "account manager": "Layla", "branch manager": "Mohamed"},
    {"customer id": "R116", "name": "Samir", "age": 46, "salary": 19000, "balance": 1700000, "account type": "Business Account", "branch": "Eastview", "account manager": "Kareem", "branch manager": "Nour"},
    {"customer id": "R117", "name": "Nasir", "age": 47, "salary": 200000, "balance": 1830000, "account type": "Business Account", "branch": "Main Street", "account manager": "Omar", "branch manager": "Hassan"},
    {"customer id": "R118", "name": "Ibrahim", "age": 49, "salary": 220000, "balance": 2560000, "account type": "Business Account", "branch": "Downtown", "account manager": "Yusuf", "branch manager": "Fatima"},
    {"customer id": "R119", "name": "Abdulrahman", "age": 50, "salary": 250000, "balance": 3800000, "account type": "Business Account", "branch": "Riverside", "account manager": "Aisha", "branch manager": "Ali"},
    {"customer id": "R121", "name": "Bassam", "age": 55, "salary": 300000, "balance": 5870000, "account type": "Business Account", "branch": "Westside", "account manager": "Layla", "branch manager": "Mohamed"},
    {"customer id": "R122", "name": "Abdulfatah", "age": 20, "salary": 350000, "balance": 11980000, "account type": "Business Account", "branch": "Eastview", "account manager": "Kareem", "branch manager": "Nour"},
    {"customer id": "R123", "name": "Farhad", "age": 20, "salary": 400000, "balance": 24000000, "account type": "Business Account", "branch": "Main Street", "account manager": "Omar", "branch manager": "Hassan"}
]

#1 How to filter from a list

#define a function to filter a list based on a key and value
def filter_list(lst,key,value):
    filtered = []
    for item in lst:
        if item[key] == value:
            filtered.append(item)
    return filtered

#show available keys to choose from
print("\nCan you please choose a key to filter it? ")
print("\n \ncustomer id")
print("name")
print("age")
print("salary")
print("balance")
print("account type")
print("branch")
print("account manager")
print("branch manager\n")

#ask the user to enter the key and value they want to filter by and exit if exit is entered 
key = input("").strip().lower()

if key == "exit":
    print("Thank you to use my Algorithm")

value = input("Please write the value you want to filter by: \n")

#check if the key is in the dictionary and convert value to an integer if needed
valid_keys = ["customer id", "name", "age", "salary", "balance", "account type", "branch", "account manager", "branch manager"]
if key in valid_keys:
#call the filter function and print the filtered results
    filtered_list = filter_list(bank_customer, key, value)
    if filtered_list:
        for item in filtered_list:
            print(item) 
    else:
        print("incorrect value entered. Please choose a correct value")
else:
    print("incorrect key entered. Please choose a correct key from the menu")
        

#-----------------------------------------------------------------------------
#2 How to sort from list

#continue asking for a valid key until the user enters one
while True:  

#ask the user to write a key to sort by
    print("\n \ncustomer id")
    print("name")
    print("age")
    print("salary")
    print("balance")
    print("account type")
    print("branch")
    print("account manager")
    print("branch manager\n")
    key = input("Which key do you want to sort by from th list: ").strip().lower()

#check if the key exists in the customer dictionary
    if key in bank_customer[0]:

#calculate the number of elements in the list
        num = len(bank_customer)

#bubble Sort: compare two adjacent elements
        for i in range(num):
            for j in range(0, num - i - 1):
                if bank_customer[j][key] > bank_customer[j + 1][key]:
                    bank_customer[j], bank_customer[j + 1] = bank_customer[j + 1], bank_customer[j]
                    
#print the sorted list
        print("\nSorted Bank Customers:")
        for item in bank_customer:
            print(item)
        break 
    else:
        print("wrong key! Please enter a valid key from the list")


#-----------------------------------------------------------------------------
#3 an aggregating algorithm to calculate the average from a list

def aggregate_customer(lst, key):
    total = 0
    customer_count = 0 

#loop through all customers in the list
    for item in bank_customer:
        if key in item:
            total += item[key]
            customer_count += 1 

#if there are no matching customers, return 0 to avoid division by zero
    if customer_count == 0:
        return 0
    return total // customer_count

while True:
    key = input("\nCan you please choose a key to get an average from: ").lower().strip()

#check if the key exists in the bank_customer data and exit the loop if the key is correct
    if key in bank_customer[0]:
        result = aggregate_customer(bank_customer, key)
        print("\nThe average for", key, "is:", result)
        break
#show an error message and ask again
    else:
        print("incorrcet key. Try again")
    