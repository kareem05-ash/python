######################################################################################################################################################
# ---------- Project Management System Program ----------
# -------------------------------------------------------  
# >> Program Features:
# [1] - Add new project (project name, head manager, project salary, team member)
# [2] - Show all project data
# [3] - Show team member data
# [4] - Generate Report                                                                                             #
######################################################################################################################################################

# ____________________________________________________________________________________________________________________________________________________
# Add new project function
def new_project():
    project_name = input("Project Name: ").strip().title()
    head_manager = input("Head Manager Name: ").strip().title()
    while True:
        project_salary = input("Total Salary: ").strip()
        try:
            project_salary = float(project_salary)
        except:
            print("Enter a valid project salary. Only digits are allowed")
        else:
            break

