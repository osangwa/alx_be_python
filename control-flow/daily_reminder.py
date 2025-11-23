def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")
    
    # Use Match Case statement to react differently based on priority
    match priority.lower():
        case "high":
            # Use if statement to modify the reminder if the task is time-bound
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Please complete it soon.")
        
        case "medium":
            # Use if statement to modify the reminder if the task is time-bound
            if time_bound == "yes":
                print(f"Note: '{task}' is a medium priority task that should be completed today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Consider completing it this week.")
        
        case "low":
            # Use if statement to modify the reminder if the task is time-bound
            if time_bound == "yes":
                print(f"Note: '{task}' is a low priority task but has a time constraint. Try to complete it when possible.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")

if __name__ == "__main__":
    main()