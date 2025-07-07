import datetime #for due date and sorting as per the due date
print("\"To do list Application ✨\"")
task_counter=1
tasks=[] 
while True:
    print("\n~~~~~MENU~~~~~\n")
    print("1. Add a new task")
    print("2. View all the added tasks")
    print("3. Mark task as done")
    print("4. Delete tasks")
    print("5. Update tasks")
    print("6. Search tasks")
    print("7. Sort tasks")
    print("8. View completed tasks")
    print("9. View tasks due soon")
    print("10. Exit Application")
    choice=int(input("\nEnter the number corresponding to your choice:"))
    if choice == 1:
        print("\n~~~~~Add a new task~~~~~\n")
        while True:
            description=input("Enter your task description: ")
            if description.strip()!="":
                break
            print("You cannot leave the description box empty.")
        while True:
            date=input("Enter the due date (YYYY-MM-DD): ")
            if date.strip()=="":
                due_date = "No due date is set"
                break
            try:
                due_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
                today = datetime.date.today()
                if due_date < today:
                    answer=input("Warning: The due date you entered is past due. Do you want to change the date (y/n)? ")
                    if answer.lower()!='y':
                        break
                else:
                    break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD or leave blank.")
        task={"task_number":task_counter,"description":description, "due_date":due_date,"completed":False}
        tasks.append(task)
        print(f"Task {task_counter} is added to the list")
        task_counter+=1    
    elif choice == 2:
        print("\n~~~~~View all added tasks~~~~~")
        if not tasks:
            print("\nThere are no added tasks at the moment...")
        else:
            for task in tasks:
                status = "✓" if task["completed"] else "✗"
                due_date = task['due_date']
                if due_date != "No due date is set":
                    due_date_str = due_date.strftime('%Y-%m-%d')
                else:
                    due_date_str = due_date
                print(f"\nTask: {task['task_number']}\n Task description: {task['description']}\n Due date: {due_date_str}\n Status: {status}")
    elif choice == 3:
        while True:
            print("\n~~~~~Mark task as done~~~~~\n")
            if not tasks:
                print("No tasks are added!")
                break
            print("~~~~~Currently Incomplete Tasks~~~~~")
            for task in tasks:
                if not task["completed"]:
                    print(f"\nTask:{task['task_number']}- {task['description']}\n")
            answer=input("Enter the task number you want to mark as done (or 'q' to quit): ")
            if answer.lower() == 'q':
                break
            try:
                answer = int(answer)
                task_found=False
                for task in tasks:
                    if task["task_number"] == answer:
                        task["completed"] = True
                        print(f"Task {answer} marked as done!")
                        task_found=True
                        break
                if not task_found:
                    print("Task not found; Enter a valid task number")
            except ValueError:
                print("Please enter a number or 'q' to quit")
    elif choice == 4:
        while True:
            print("\n~~~~~Delete task~~~~~\n")
            if not tasks:
                print("No tasks are added!")
                break
            print("~~~~~Currently Added Tasks~~~~~")
            for task in tasks:
                print(f"\nTask:{task['task_number']}- {task['description']}\n")
            answer=input("Enter the task number you want to delete (or 'q' to quit): ")
            if answer.lower() == 'q':
                break
            try:
                answer = int(answer)
                task_found=False
                for i, task in enumerate(tasks):
                    if task['task_number'] == answer:
                        del tasks[i]
                        print(f"Task {answer} deleted!")
                        task_found=True
                        # Reset task numbers after deletion
                        for index, t in enumerate(tasks, 1):
                            t['task_number'] = index
                        task_counter = len(tasks) + 1
                        break
                if not task_found:
                    print("Task not found; Enter a valid task number")
            except ValueError:
                print("Please enter a number or 'q' to quit")
    elif choice == 5:
        today = datetime.date.today()
        while True:
            print("\n~~~~~Update task~~~~~\n")
            if not tasks:
                print("No tasks are added!")
                break
            print("~~~~~Currently Added Tasks~~~~~")
            for task in tasks:
                print(f"\nTask:{task['task_number']}- {task['description']}\n")
            answer=input("Enter the number of task you want to update (or 'q' to quit): ")
            if answer.lower() == 'q':
                break
            try:
                update_answer = int(answer)
                task_found = False
                for task in tasks:
                    if task['task_number'] == update_answer:
                        task_found = True
                        print("\nWhat do you want to update?")
                        print("1. Description")
                        print("2. Due Date")
                        print("3. Both")
                        print("4. Cancel")
                        update_choice=input("Enter the number corresponding to your choice: ")
                        if update_choice == '1':
                            new_desc = input(f"\nCurrent: {task['description']}\nNew description: ")
                            if new_desc.strip()!="":
                                task['description'] = new_desc
                                print("Description updated!")
                            else:
                                print("Description cannot be empty!")
                        elif update_choice == '2':
                            print(f"\nCurrent due date: {task['due_date']}")
                            while True:
                                new_date = input("New date (YYYY-MM-DD) or leave blank: ")
                                if new_date.strip()=="":
                                    task['due_date'] = "No due date is set"
                                    print("Due date removed!")
                                    break
                                try:
                                    new_due_date = datetime.datetime.strptime(new_date, "%Y-%m-%d").date()
                                    if new_due_date < today:
                                        ans=input("Warning: The due date you entered is past due. Do you want to change the date (y/n)? ")
                                        if ans.lower()!='y':
                                            task['due_date'] = new_due_date
                                            print("Due date updated!")
                                            break
                                    else:
                                        task['due_date'] = new_due_date
                                        print("Due date updated!")
                                        break
                                except ValueError:
                                    print("Invalid date format. Please use YYYY-MM-DD or leave blank.")
                        elif update_choice == '3':
                            new_desc = input(f"\nCurrent: {task['description']}\nNew description: ")
                            if new_desc.strip()!="":
                                task['description'] = new_desc
                                print("Description updated!")
                            else:
                                print("Description cannot be empty!")
                            print(f"\nCurrent due date: {task['due_date']}")
                            while True:
                                new_date = input("New date (YYYY-MM-DD) or leave blank: ")
                                if new_date.strip()=="":
                                    task['due_date'] = "No due date is set"
                                    print("Due date removed!")
                                    break
                                try:
                                    new_due_date = datetime.datetime.strptime(new_date, "%Y-%m-%d").date()
                                    if new_due_date < today:
                                        ans=input("Warning: The due date you entered is past due. Do you want to change the date (y/n)? ")
                                        if ans.lower()!='y':
                                            task['due_date'] = new_due_date
                                            print("Due date updated!")
                                            break
                                    else:
                                        task['due_date'] = new_due_date
                                        print("Due date updated!")
                                        break
                                except ValueError:
                                    print("Invalid date format. Please use YYYY-MM-DD or leave blank.")
                        elif update_choice == '4':
                            print("Update cancelled!")
                        else:
                            print("Invalid choice")
                if not task_found:
                    print("Task not found; Enter a valid task number")
            except ValueError:
                print("Please enter a number or 'q' to quit")
    elif choice == 6:
        print("\n~~~~~Search tasks~~~~~\n")
        if not tasks:
            print("No tasks are added!")
            continue
        search_term = input("Enter the search term: ").lower()
        found = False
        for task in tasks:
            if search_term in task['description'].lower():
                found = True
                status = "✓" if task["completed"] else "✗"
                due_date = task['due_date']
                if due_date != "No due date is set":
                    due_date_str = due_date.strftime('%Y-%m-%d')
                else:
                    due_date_str = due_date
                print(f"\nTask: {task['task_number']}\n Task description: {task['description']}\n Due date: {due_date_str}\n Status: {status}")
        if not found:
            print("No matching tasks found.")
    elif choice == 7:
        print("\n~~~~~Sort tasks~~~~~\n")
        if not tasks:
            print("No tasks are added!")
            continue
        print("Sort by:")
        print("1. Due Date (earliest first)")
        print("2. Description (A-Z)")
        sort_choice = input("Enter number corresponding to your choice: ")
        if sort_choice == '1':
            # Separate tasks with and without due dates
            tasks_with_dates = [t for t in tasks if t['due_date'] != "No due date is set"]
            tasks_without_dates = [t for t in tasks if t['due_date'] == "No due date is set"]
            # Sort only tasks with dates
            tasks_with_dates.sort(key=lambda x: x['due_date'])
            # Combine them (tasks with dates first)
            tasks = tasks_with_dates + tasks_without_dates
            print("Tasks sorted by due date (earliest first)")
        elif sort_choice == '2':
            tasks.sort(key=lambda x: x['description'].lower())
            print("Tasks sorted by description (A-Z)")
        else:
            print("Invalid choice")
            continue
        for task in tasks:
            status = "✓" if task["completed"] else "✗"
            due_date = task['due_date']
            if due_date != "No due date is set":
                due_date_str = due_date.strftime('%Y-%m-%d')
            else:
                due_date_str = due_date
            print(f"\nTask: {task['task_number']}\n Task description: {task['description']}\n Due date: {due_date_str}\n Status: {status}")
    elif choice == 8:
        print("\n~~~~~View completed tasks~~~~~\n")
        if not tasks:
            print("No tasks are added!")
            continue
        completed_tasks = [t for t in tasks if t["completed"]]
        if not completed_tasks:
            print("No completed tasks!")
        else:
            for task in completed_tasks:
                status = "✓"
                due_date = task['due_date']
                if due_date != "No due date is set":
                    due_date_str = due_date.strftime('%Y-%m-%d')
                else:
                    due_date_str = due_date
                print(f"\nTask: {task['task_number']}\n Task description: {task['description']}\n Due date: {due_date_str}\n Status: {status}")
    elif choice == 9:
        print("\n~~~~~View tasks due soon~~~~~\n")
        if not tasks:
            print("No tasks are added!")
            continue
        while True:
            duration=input("Specify the duration (in days) for which you would like to view your tasks: ")
            try:
                duration = int(duration)
                if duration < 0:
                    print("Invalid duration. Enter a positive number")
                    continue
                break
            except ValueError:
                print("Please enter a number")
        today = datetime.date.today()
        due_soon_tasks=[]
        for task in tasks:
            if task["due_date"]!="No due date is set" and not task["completed"]:
                days_remaining = (task["due_date"] - today).days
                if 0 <= days_remaining <= duration:
                    due_soon_tasks.append(task)
        if not due_soon_tasks:
            print("No incomplete tasks due within this time duration!")
        else:
            for task in due_soon_tasks:
                days_remaining = (task["due_date"] - today).days
                status = "✓" if task["completed"] else "✗"
                print(f"\nTask: {task['task_number']}\n Task description: {task['description']}\n Due date: {task['due_date'].strftime('%Y-%m-%d')} ({days_remaining} days remaining)\n Status: {status}")
    elif choice == 10:
        print("\nExiting the application....")
        break
    else:
        print("\nInvalid choice; Try again")