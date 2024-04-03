creds = [
    "CSE3 Act1",
    "by: Andrew Oloroso",
    "repo: https://github.com/ChugxScript/CSE3-Python-Act1"
]

def evenOddNumber():
    print()
    number_str = input("enter number: ")

    if number_str.isdigit():
        number = int(number_str)
        if number % 2 == 0:
            print(f"number [{number}] is EVEN.")
        else:
            print(f"number [{number}] is ODD.")
    else:
        print(f"number [{number}] is INVALID. It must be integer.")

# evenOddNumber()

def ageCheck():
    print()
    age_str = input("enter age: ")   
    
    if age_str.isdigit():
        age = int(age_str)
        if age < 0:
            print(f"Age [{age}] is INVALID.")
        elif age < 3:
            print(f"Age [{age}] is an INFANT not a TEENAGER.")
        elif age < 13:
            print(f"Age [{age}] is a CHILD not a TEENAGER.")
        elif age < 20:
            print(f"Age [{age}] is a TEENAGER.")
        elif age < 60:
            print(f"Age [{age}] is an ADULT not a TEENAGER.")
        else:
            print(f"Age [{age}] is a SENIOR not a TEENAGER.")
    else:
        print(f"age [{age_str}] is INVALID. It must be integer.")

# ageCheck()

def monthlyCommission():
    print()
    monthlySale_str = input("input monthly sale: ")
    
    if monthlySale_str.isdigit():
        monthlySale = int(monthlySale_str)
        if monthlySale > 500000:
            commission = monthlySale * 0.1
            print(f"Commission is 10% = {commission}")
        else:
            commission = monthlySale * 0.05
            print(f"Commission is 5% = {commission}")
    else:
        print(f"Monthly Sale [{monthlySale_str}] is INVALID. It must be integer.")

# monthlyCommission()

def yearCheck():
    print()
    year_str = input("enter year: ")

    if year_str.isdigit():
        year = int(year_str)
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    # Divisible by 400, so leap year
                    print(f"year [{year}] is a LEAP YEAR.")  
                else:
                    # Divisible by 100 but not by 400, so not a leap year
                    print(f"year [{year}] is NOT a LEAP YEAR.")   
            else:
                # Divisible by 4 but not by 100, so leap year
                print(f"year [{year}] is a LEAP YEAR.")  
        else:
            # Not divisible by 4, so not a leap year
            print(f"year [{year}] is NOT a LEAP YEAR.")   
    else:
        print(f"year [{year_str}] is INVALID. It must be integer.")

# yearCheck()

def absoluteValue():
    print()
    number_str = input("enter number: ")

    number = int(number_str)
    if number < 0:
        # absoluteNumber = number * -1  OR...
        absoluteNumber = abs(number)
        print(f"absolute value of [{number}] is [{absoluteNumber}]")
    else:
        print(f"number [{number}] is already an absolute value")

# absoluteValue()

def positiveNegativeNumber():
    print()
    number_str = input("enter number: ")

    number = int(number_str)
    if number < 0:
        print(f"number [{number}] is NEGATIVE.")
    elif number > 0:
        print(f"number [{number}] is POSITIVE.")
    else:
        print(f"number [{number}] is 0.")

# positiveNegativeNumber()

if __name__ == "__main__":
    while True:
        print("--- MENU ---")
        print("[1] Enter any number and check it is even or odd.")
        print("[2] Enter any age and check it is teenager or not.")
        print("[3] Enter monthly sale of Salesman and give him commission  e.r. if the monthly sale is more than 500,000 the coommision will be 10% of monthly sale otherwise 5%.")
        print("[4] Input any year and check it is Leap Year or Not.")
        print("[5] Input any number and print Absolute value of that number.")
        print("[6] Input any number and check it is positive or negative.")
        userNum = int(input("\n>>> "))

        if userNum == 1:
            evenOddNumber()
        elif userNum == 2:
            ageCheck()
        elif userNum == 3:
            monthlyCommission()
        elif userNum == 4:
            yearCheck()
        elif userNum == 5:
            absoluteValue()
        elif userNum == 6:
            positiveNegativeNumber()
        else:
            print(f"[{userNum}] is invalid. Try again.")
        
        print()
        for cred in creds:
            print(cred)
        print()