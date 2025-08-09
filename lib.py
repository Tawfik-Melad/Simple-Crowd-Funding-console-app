import hashlib
import datetime

def hash_password(password) :
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def get_id():
    """Generate a unique ID for a new project."""
    ids=[]
    try:
        with open('.projects.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) > 0:
                    ids.append(int(parts[0]))
    except FileNotFoundError:
        return 1
    id=1
    for i in range(len(ids)):
        if ids[i] == id:
            id += 1
    return id

def validate_date(date_text):
    try:
        return datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        print("Incorrect date format, should be YYYY-MM-DD")
        return None


def create_project(user_email):
    title = input("Enter project title: ")
    details = input("Enter project details: ")
    try:
        target = float(input("Enter total target (e.g. 250000): "))
    except ValueError:
        print("Invalid target amount.")
        return
    start_date = None
    end_date = None
    while not start_date:
        start_date = validate_date(input("Enter start date (YYYY-MM-DD): "))
    while not end_date:
        end_date = validate_date(input("Enter end date (YYYY-MM-DD): "))
    if end_date <= start_date:
        print("End date must be after start date.")
        return
    # Count number of lines in the file to generate a unique project ID
    id = get_id()

    project = {
        "id": id,
        "owner": user_email,
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date
    }
    with open('.projects.txt', 'a') as file:
        file.write(f"{id},{user_email},{title},{details},{target},{start_date},{end_date}\n")
    print("Project created successfully.")

def view_projects(email):
    try:
        with open('.projects.txt', 'r') as file:
            projects = [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        print("No projects found.")
        return

    for idx, project in enumerate(projects, 1):
        project_id, owner, title, details, target, start_date, end_date = project
        you= " (You)" if owner == email else ""
        project_id = project_id if owner == email else "PRIVATE"
        print(f"{idx}. ID: {project_id} - {title} -{details} (Target: {target}, Start: {start_date}, End: {end_date}) Owner: {owner}{you}")

def view_owned_projects(user_email):
    try:
        with open('.projects.txt', 'r') as file:
            projects = [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        print("No projects found.")
        return []

    owned_projects = [project for project in projects if project[1] == user_email]
    if not owned_projects:
        print("You have no projects.")

    for idx, project in enumerate(owned_projects, 1):
        project_id, owner, title, details, target, start_date, end_date = project
        print(f" ID: {project_id}. {title} - {details} (Target: {target}, Start: {start_date}, End: {end_date}) Owner: {owner}")
    return 

def delete_project(user_email):
    view_owned_projects(user_email) 
    id = int(input("Enter the project id to delete: "))
    if id < 1:
        print("Invalid project number.")
        return
    try:
        with open('.projects.txt', 'r') as file:
            projects = [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        print("No projects found.")
        return
    project = next((p for p in projects if int(p[0]) == id and p[1] == user_email), None)
    if not project:
        print("Project not found or you do not own this project.")
        return
    projects.remove(project)
    with open('.projects.txt', 'w') as file:
        for p in projects:
            file.write(','.join(p) + '\n')
    print("Project deleted successfully.")
    return


def update_project(user_email):
    view_owned_projects(user_email)
    try:
        id = int(input("Enter the project id to update: "))
        if id < 1:
            print("Invalid project number.")
            return
    except ValueError:
        print("Invalid input.")
        return

    try:
        with open('.projects.txt', 'r') as file:
            projects = [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        print("No projects found.")
        return

    project = next((p for p in projects if int(p[0]) == id and p[1] == user_email), None)
    if not project:
        print("Project not found or you do not own this project.")
        return

    print("Leave field blank to keep current value.")
    new_title = input(f"Enter new title [{project[2]}]: ") or project[2]
    new_details = input(f"Enter new details [{project[3]}]: ") or project[3]
    try:
        new_target_input = input(f"Enter new target [{project[4]}]: ")
        new_target = float(new_target_input) if new_target_input else project[4]
    except ValueError:
        print("Invalid target amount.")
        return

    new_start_date = None
    while not new_start_date:
        start_input = input(f"Enter new start date [{project[5]}] (YYYY-MM-DD): ")
        if not start_input:
            new_start_date = project[5]
            break
        new_start_date_obj = validate_date(start_input)
        if new_start_date_obj:
            new_start_date = start_input

    new_end_date = None
    while not new_end_date:
        end_input = input(f"Enter new end date [{project[6]}] (YYYY-MM-DD): ")
        if not end_input:
            new_end_date = project[6]
            break
        new_end_date_obj = validate_date(end_input)
        if new_end_date_obj:
            new_end_date = end_input

    if new_end_date <= new_start_date:
        print("End date must be after start date.")
        return

    updated_project = [
        project[0], user_email, new_title, new_details, str(new_target), new_start_date, new_end_date
    ]
    idx = projects.index(project)
    projects[idx] = updated_project

    with open('.projects.txt', 'w') as file:
        for p in projects:
            file.write(','.join(p) + '\n')
    print("Project updated successfully.")


def search_in_projects():
    keyword = input("Enter keyword to search projects: ").strip().lower()
    try:
        with open('.projects.txt', 'r') as file:
            projects = [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        print("No projects found.")
        return

    found_projects = [p for p in projects if keyword in p[1] or keyword in p[2].lower() or keyword in p[3].lower() or keyword in p[4].lower()]
    if not found_projects:
        print("No projects found with that keyword.")
        return

    for idx, project in enumerate(found_projects, 1):
        project_id, owner, title, details, target, start_date, end_date = project
        print(f"{idx} - {title} -{details} (Target: {target}, Start: {start_date}, End: {end_date}) Owner: {owner}")

