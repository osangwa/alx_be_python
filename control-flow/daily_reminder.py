task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"Note: '{task}' is a medium priority task that should be completed today.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task but has a time constraint. Try to complete it when possible.")

if time_bound != "yes":
    match priority:
        case "high":
            print(f"Reminder: '{task}' is a high priority task. Please complete it soon.")
        case "medium":
            print(f"Note: '{task}' is a medium priority task. Consider completing it this week.")
        case "low":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")