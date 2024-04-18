import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

with open(csv_path, 'r') as file:
    csv_read = csv.reader(file, delimiter=',')
    
    next(csv_read)
    
    for row in csv_read:
        total_months += 1
        
        months.append(row[0])
        
        profit_loss = int(row[1])
        
        total_profit_losses += profit_loss
        
        if total_months > 1:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
        
        previous_profit_loss = profit_loss

average_change = sum(profit_loss_changes) / len(profit_loss_changes)

greatest_increase = max(profit_loss_changes)
greatest_decrease = min(profit_loss_changes)

greatest_increase_index = profit_loss_changes.index(greatest_increase)
greatest_decrease_index = profit_loss_changes.index(greatest_decrease)

greatest_increase_month = months[greatest_increase_index + 1]
greatest_decrease_month = months[greatest_decrease_index + 1]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

output_folder = os.path.join("..", "analysis")
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "bank_results.txt")

with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
