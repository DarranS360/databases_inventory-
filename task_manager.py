from datetime import datetime       # Imported datetime to use today's date for task input later

now = datetime.now()        # Get today's date
date_now = now.strftime("%d/%m/%Y")     # format the date, so it is in the format of day/month/year

# Function to register user
def reg_user():
    new_user = input("What is the username of the new user?\n").lower()
    with open("user.txt", "r") as f:
        check_user = f.read()  # Lines to ensure a user exists in user.txt to assign tasks to
        if new_user in check_user:
            print("User already exists.\n")
        else:
            new_password = input("What will their password be?\n")
            password_check = input("Please confirm the new password... \n")

            if password_check != new_password:  # Added a check to confirm password
                print("Sorry, the passwords do not match. Please try again.")
            elif password_check == new_password:
                with open("user.txt", "a") as f:
                    f.write(f"\n{new_user}, {new_password}")  # Format info and print is (username, password)
                    print(f"New user: \"{new_user}\" confirmed.\n")

# Function to add task
def add_task():
    while True:
        assigned_user = input("Which user is the task to be assigned to?\n").lower()
        with open("user.txt", "r") as f:
            check_user = f.read()  # Lines to ensure a user exists in user.txt to assign tasks to
            if assigned_user in check_user:
                task = input("What is the new task?\n").capitalize().strip()
                task_description = input("Please give a brief description of the task:\n").capitalize().strip()
                date_due = input(
                    f"When is the task \"{task}\" due? (please enter date in the format: dd/mm/yyyy)\n").strip()
                task_complete = "No"
                # Capitilse and strip before writing to file for formatting, more pleasing to the eye later on
                # File open below and info written, using today's date from string at beginning using datetime
                with open("tasks.txt", "a") as tasks:
                    tasks.write(f"\n{assigned_user}, {task}, {task_description}, {date_now}, {date_due}, {task_complete}")
                print(f"Task \"{task}\" confirmed for user \"{assigned_user}\".\n")
                break
            else:
                print("Sorry, no user exists. Please try again.\n")


# Function to allow tasks to be edited
def edit_tasks():
    line_edit = int(input("Which task would you like to edit?\n")) - 1      # -1 to compensate for count starting at 0
    which_edit = input("""Select one of the following options below:
mc - Mark task as complete
d - Edit the Due Date
u - Edit user assigned to task
""").lower()
# Open file and split lines so the individual elements can be manipulated
    with open("tasks.txt", "r") as task_read:
        list_of_lines = task_read.readlines()
        edit_lines = list_of_lines[line_edit]
        edit_lines = edit_lines.strip().split(", ")
        user = edit_lines[0]
        task = edit_lines[1]
        task_description = edit_lines[2]
        date_assigned = edit_lines[3]
        date_due = edit_lines[4]
        task_complete = edit_lines[5]

    if which_edit == "d":   # Edit due date
        with open("tasks.txt", "w") as task_edit:
            new_date = input("What would you like the new due date to be?\n")
            # Write the line anew with the original data, but with new date
            list_of_lines[line_edit] = (f"{user}, {task}, {task_description}, {date_assigned}, {new_date}, {task_complete}\n")
            task_edit.writelines(list_of_lines)
            print(f"Date changed successfully from {date_due} to {new_date}.")

    elif which_edit == "u":     # Edit user
        while True:
            with open("tasks.txt", "w") as task_edit:
                new_user = input("Who would you like the task to be reassigned to?\n")
                with open("user.txt", "r") as f:
                    check_user = f.read()  # Lines to ensure a user exists in user.txt to assign tasks to
                    if new_user not in check_user:
                        print("User does not exist, try again.\n")
                    else:
                        # Write the line anew with the original data, but with new user
                        list_of_lines[line_edit] = (f"{new_user}, {task}, {task_description}, {date_assigned}, {date_due}, {task_complete}\n")
                        task_edit.writelines(list_of_lines)
                        print(f"User changed successfully from {user} to {new_user}.")
                        break

    elif which_edit == "md":        # Edit complete element
        with open("tasks.txt", "w") as task_edit:
            task_complete_yes = "Yes"
            # Write the line anew with the original data, but with new complete marked as 'Yes'
            list_of_lines[line_edit] = (f"{user}, {task}, {task_description}, {date_assigned}, {date_due}, {task_complete_yes}\n")
            task_edit.writelines(list_of_lines)
            print("Task now marked as complete.")


# Function to view all tasks
def view_all():
    with open("tasks.txt", "r") as f:
        for line in f.readlines():  # Read line by line to gather info
            temp_view = line.strip().split(", ")  # Split lines at the "," to sep out user, task, etc. into list
            user = temp_view[0]
            task = temp_view[1]
            task_description = temp_view[2]
            date_assigned = temp_view[3]
            date_due = temp_view[4]
            task_complete = temp_view[5]
            # Above gets place in list of each type of info (user, task, etc.)
            view_all = "----------------------------------------------------------------------------------\n" \
                       f"Task: \t \t \t \t {task}\n" \
                       f"Assigned to: \t \t {user}\n" \
                       f"Date assigned: \t \t {date_assigned}\n" \
                       f"Due date: \t \t \t {date_due}\n" \
                       f"Task complete? \t \t {task_complete}\n" \
                       f"Task description: \t {task_description}\n" \
                       f"------------------------------------------------------------------------------------\n"
            # Above is format of output, \ stops the error message that would otherwise occur
            print(view_all)


# Function to view user tasks
def view_mine():
    n = 0
    with open("tasks.txt", "r") as f:
        check_user = f.read()       # Check user is in file and has tasks to display
        if username not in check_user:
            print("You have no tasks to display.\n")
        else:
            with open("tasks.txt", "r") as file:
                for line in file.readlines():       # Read line by line to gather info
                    n += 1
                    if username in line:
                        temp_view = line.strip().split(", ")     # Split lines at the "," to sep out into list
                        user = temp_view[0]
                        task = temp_view[1]
                        task_description = temp_view[2]
                        date_assigned = temp_view[3]
                        date_due = temp_view[4]
                        task_complete = temp_view[5]
                        # Above gets place in list of each type of info (user, task, etc.)
                        view_all = "------------------------------------------------------------------------------\n" \
                                   f"Task number:         {n}\n" \
                                   f"Task: \t \t \t \t {task}\n" \
                                   f"Assigned to: \t \t {user}\n" \
                                   f"Date assigned: \t \t {date_assigned}\n" \
                                   f"Due date: \t \t \t {date_due}\n" \
                                   f"Task complete? \t \t {task_complete}\n" \
                                   f"Task description: \t {task_description}\n" \
                                   f"--------------------------------------------------------------------------------\n"

                        print(view_all)

    alt_option = input("Would you like to edit a task? (\"y\" for yes or \"-1\" to return to the main menu)\n")
    if alt_option == "y":
        edit_tasks()        # Calls on the function to edit tasks once a user views their tasks


# Function for admin to view total user and task numbers
def display_stats():
    # Below calls on newly created file, splits it into lists, calls on a search for total users and prints at index 1
    with open("user_overview.txt", "r") as users_all:
        for line in users_all.readlines():
            if "Total number of users" in line:
                temp_view = line.strip().split(": ")
                user_count = temp_view[1]
    # Below calls on newly created file, splits it into lists, calls on a search for total tasks and prints at index 1
    with open("task_overview.txt", "r") as tasks_all:
        for line in tasks_all.readlines():
            if "Total number of tasks" in line:
                temp_view = line.strip().split(": ")
                tasks_count = temp_view[1]
        ds_print = "--------------------------------------\n" \
                   f"Number of Users: \t {user_count}\n" \
                   f"Number of Tasks: \t {tasks_count}\n" \
                   f"--------------------------------------\n"
        print(ds_print)


# Function to generate reports of tasks into a new file that will be created
def generate_report():
    with open("tasks.txt", "r") as tasks_all:
        # Counters to add to keep track of complete/overdue/incomplete tasks
        complete_count = 0
        incomplete_count = 0
        overdue = 0

        for line in tasks_all.readlines():  # Read line by line to gather info
            temp_view = line.strip().split(", ")  # Split lines at the "," to sep out user, task, etc. into list
            date_due = temp_view[4]
            task_complete = temp_view[5]

            # Checking for overdue by comparing dates to today and ensuring it is marked as 'No' for completeness
            if date_due <= date_now and task_complete == "No":
                overdue += 1

            if task_complete == "Yes":
                complete_count += 1
            elif task_complete == "No":
                incomplete_count += 1

    # Counts the number of lines which will give the number of tasks
    with open("tasks.txt", "r") as tasks_all:
        tasks_count = sum(1 for line in tasks_all if line.rstrip())
        percentage_incomplete = (incomplete_count / tasks_count) * 100
        percentage_overdue = (overdue / tasks_count) * 100

    # Creating new file/opening it, and writing in the information gathered above
    with open("task_overview.txt", "w+") as f:
        f.write(f"""Total number of tasks: {tasks_count}
Total completed tasks: {complete_count}
Total incomplete tasks: {incomplete_count}
Total tasks overdue: {overdue}
Percentage incomplete: {percentage_incomplete:.2f}%     
Percentage overdue: {percentage_overdue:.2f}%""")
# .2f above in f string "rounds" up, by printing only 2 spaces after decimal


# Function to generate reports of user tasks into a new file that will be created
# Methods used above are again implemented below
def generate_report_user():
    complete_count = 0
    incomplete_count = 0
    overdue = 0
    task_user = 0

    with open("tasks.txt", "r") as file:
        for line in file.readlines():
            if username in line:
                task_user += 1
                temp_view = line.strip().split(", ")
                date_due = temp_view[4]
                task_complete = temp_view[5]

                if date_due <= date_now and task_complete == "No":
                    overdue += 1
                if task_complete == "Yes":
                    complete_count += 1
                elif task_complete == "No":
                    incomplete_count += 1

    with open("tasks.txt", "r") as tasks_all:
        tasks_count = sum(1 for line in tasks_all if line.rstrip())
        percentage_incomplete = (incomplete_count / task_user) * 100
        percentage_overdue = (overdue / task_user) * 100
        percentage_total = (task_user / tasks_count) * 100
        percentage_complete = (complete_count / task_user) * 100

    with open("user.txt", "r") as f:
        user_count = sum(1 for line in f if line.rstrip())

    with open("user_overview.txt", "w+") as f:
        f.write(f"""Total number of users: {user_count}
Total tasks for {username}: {task_user}
Percentage of total tasked assigned to you: {percentage_total:.2f}%
Percentage of tasks completed: {percentage_complete:.2f}%
Percentage of tasks incomplete: {percentage_incomplete:.2f}%
Percentage of tasks overdue: {percentage_overdue:.2f}%""")


# Login section
while True:
    username = input("Please enter your username: \n").lower()
    password = input("Please enter your password: \n")
    user_pass = f"{username}, {password}"       # Combine username and password to match format in txt file

    with open("user.txt", "r") as user:
        for line in user:
            if user_pass in line:       # Checking if combined username password is in user.txt
                access = True
                break
            else:
                access = False

    if access:      # If access is true, welcome message printed and use allowed into programme menu
        print("\nWelcome")
        break
    elif not access:        # If access false, error message printed
        print("\nIncorrect Username or Password. Please try again.\n")

# Operation section
while True:
    if username != "admin":     # While loop for regular user
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
e - Exit
''').lower()

    elif username == "admin":       # While loop for admin with extra option ds (display stats)
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display stats
e - Exit
''').lower()

    # register user section
    if menu == 'r' and username == "admin":     # Access only if admin
        reg_user()
    elif menu == 'r' and username != "admin":    # Error message if user is not admin
        print("You are not authorised to add a new user. Please select another option.\n")

    # add task section
    elif menu == 'a':
        add_task()

    # view all tasks section
    elif menu == 'va':
        view_all()

    # View my tasks section
    elif menu == 'vm':
        view_mine()

    # Admin menu display stats section
    elif menu == "ds" and username == "admin":      # Line states will only show info if user is admin
        display_stats()

    elif menu == 'e':
        print('\nGoodbye!!!')
        exit()

    elif menu == 'gr':
        generate_report()
        generate_report_user()
        print("Reports generated successfully.\n")

    else:
        print("You have made a wrong choice, please try again.\n")

# Line 202-205, opening the file again was the only way it would work to count the lines
# When included in the code above it threw everything off
# Any idea as to why? Any tips would be greatly appreciated :-)
