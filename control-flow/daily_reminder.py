def main():
    # Prompt for a single task
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound_input = input("Is it time-bound? (yes/no): ").strip().lower()
    
    # Convert time-bound input to boolean
    is_time_bound = time_bound_input == "yes"
    
    # Process the task based on priority and time sensitivity
    match priority:
        case "high":
            if is_time_bound:
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Please complete it soon.")
        
        case "medium":
            if is_time_bound:
                print(f"Note: '{task}' is a medium priority task that should be completed today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Consider completing it this week.")
        
        case "low":
            if is_time_bound:
                print(f"Note: '{task}' is a low priority task but has a time constraint. Try to complete it when possible.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")

if __name__ == "__main__":
    main()