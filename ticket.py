def create_ticket():
    print("===== HELPDESK TICKET SYSTEM =====")

    student_name = input("Enter Student Name: ")
    student_id = input("Enter Student ID: ")
    issue = input("Enter Issue: ")
    location = input("Enter Location: ")
    priority = input("Enter Priority (High/Medium/Low): ")

    # Assign technician based on priority
    if priority.lower() == "high":
        technician = "Ahmad"
    elif priority.lower() == "medium":
        technician = "Siti"
    elif priority.lower() == "low":
        technician = "Ali"
    else:
        technician = "Not Assigned"

    status = "Pending"

    ticket = {
        "student_name": student_name,
        "student_id": student_id,
        "issue": issue,
        "location": location,
        "priority": priority,
        "technician": technician,
        "status": status
    }

    return ticket