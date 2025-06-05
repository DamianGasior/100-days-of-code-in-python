print("Welcome to the tip calculator!\n")

bill_answer=float(input("What was the total bill? $\n"))

tip_answer=float(input("How much tip (in%) would you like to give? 10,12 or 15\n"))/100+1

split_bill_answer = int(input("How many people to split the bill ?\n"))


total_amount=(bill_answer*tip_answer)/split_bill_answer
total_amount_result=round(total_amount,2)

print(f"Each person should pay: {total_amount_result}")

