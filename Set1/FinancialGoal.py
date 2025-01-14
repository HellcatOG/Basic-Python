#Input

target_amount = float(input("Enter the target saving amount: "))
current_saving = float(input("Enter your current saving: "))
total_months = float(input("Enter the total months: "))

#Calculations

remaining_amount = target_amount - current_saving
monthly_savings = remaining_amount / total_months

#output

print(f"The remaianing Amount is {remaining_amount:.1f} \n Monthly Savings required is {monthly_savings:.1f}")
