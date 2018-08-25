import csv

df_financial = ("Book1.csv")

total_months = 0
total_profit_loss = 0
average_change = 0 
month_of_change = []

with open(df_financial) as csvfile:
    reader = csv.DictReader(csvfile)
    

  
    for row in reader:
        
        total_months = total_months + 1
        print(total_months)
        
        total_profit_loss = total_profit_loss + int(row["Profit/Losses"]) 
        
        
        average = int(row["Profit/Losses"])/ 86
        print(average)
    

output =(
        f"\nFinancial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total Revenue: ${total_profit_loss}\n"
        f"Average: {average}\n"
        f"Greatest Increase in profits: Unknown\n"
        f"Greatest Decrease in Revenue: Unknown\n")

print(output)