# INPUTS

owner_age = int(input("Age: "))
monthly_revenue = float(input("Monthly Revenue: "))
credit_score = int(print("Credit Score: "))
years_in_business = float(input("Years in Business: "))
has_defaults = bool(input("Has Defaults? ---> "))
collateral_name = input("Collateral Name: ")
collateral_value = float(input("Collateral Value: "))

base_fee = 0
max_loan = 0

# BASELINE
if owner_age >= 21 and has_defaults == False and years_in_business >= 2.0:
    print("BASELINE PASSED.")
    if credit_score >= 720:  # TIER 1
        print("CREDIT SCORE CONSIDERED HIGH.")
        max_loan = monthly_revenue * 3
        if monthly_revenue >= 50000:
            print("ABOVE 50k REVENUE.")
            base_fee = max_loan * 0.015
            print("BASE FEE IS SET TO", base_fee)
        else:
            print("REVENUE BELOW 50k.")
            base_fee = max_loan * 0.025
            print("BASE FEE IS SET TO", base_fee)
    elif credit_score >= 620 and credit_score < 720: # TIER 2
        print("Credit Score within range of 620 and 720.")
        max_loan =  monthly_revenue * 1.5
        if years_in_business >= 5.0:
            base_fee = max_loan * 0.02
            print("Years in Business is greater than 5 years, base is", base_fee)
        else:
            base_fee = max_loan * 0.035
            print("Years in Business is lower than 5 years, base fee is", base_fee)
    elif credit_score < 620:
        print("CREDIT SCORE TOO LOW.")
    else: 
        print("INVALID.")
else:
    print("BASELINE FAILED.")