def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")
    
    # Process the task based on priority
    if time_bound == "yes":
        # Time-bound tasks
        if priority.lower() == "high":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif priority.lower() == "medium":
            print(f"Note: '{task}' is a medium priority task that should be completed today.")
        elif priority.lower() == "low":
            print(f"Note: '{task}' is a low priority task but has a time constraint. Try to complete it when possible.")
        else:
            print("Invalid priority level.")
    else:
        # Non-time-bound tasks
        if priority.lower() == "high":
            print(f"Reminder: '{task}' is a high priority task. Please complete it soon.")
        elif priority.lower() == "medium":
            print(f"Note: '{task}' is a medium priority task. Consider completing it this week.")
        elif priority.lower() == "low":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("Invalid priority level.")

if __name__ == "__main__":
    main()