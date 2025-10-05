#Group 24 

timetable = 'timetables_StudentID.txt'  #Initiate Timetable file
attendance = 'attendance_StudentID.txt' #Initiate Attendance file
assignments = 'assignments_StudentID.txt' #Initiate Assignment file


#ATTENDANCE FUNCTIONS
#Function to get the average for the attendance data
def display_N_average(attendance_data):
    total_numbers = 0
    count_ones = 0
    for attendances in attendance_data.values():
        total_numbers += len(attendances)
        count_ones += attendances.count(1)
    return total_numbers, count_ones


def extract_attendance_data():
    attendance_data = {}
    with open('attendance_StudentID.txt', 'r') as file:
        lines = file.readlines()
        current_student = None
        for line in lines:
            if line.startswith('Student'):
                current_student = line.split()[1][:-1]
                attendance_data[current_student] = {}
            elif line.startswith('Subject'):
                if current_student is not None:
                    subject, attendances = line.split(": ")
                    subject_number = subject.split()[1]
                    attendance_data[current_student][subject_number] = list(map(int, attendances.strip()[1:-1].split(',')))
                else:
                    print("Error: Subject data found before student data.")
                    print("Current line:", line)
                    print("Current student:", current_student)
        return attendance_data


#Function for the attendance code 
def icheckin():
    correct_code = '12345'
    icheckin = input("Please enter the code to enter: ")
    while icheckin != correct_code:
        print("Incorrect code. Please try again.")
        icheckin = input("Please enter the code: ")
    print("Password accepted.")
    return True


#Function to add attendance in the text file 
def add_attendance(file_path, student_choice, subject_choice):
    file_path = 'attendance_StudentID.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if line.startswith(f"Student {student_choice}:"):
            while not lines[i].startswith(f"Subject {subject_choice}"):
                i += 1
            attendances = lines[i].split(":")[1].strip().strip("[]").split(",")
            attendances = [int(x) for x in attendances if x.strip()]  # Exclude empty strings
            attendances.append(1)  # Append 1 indicating attendance
            lines[i] = f"Subject {subject_choice} attendances: {attendances}\n"
            break
    with open(file_path, 'w') as file:
        file.writelines(lines)


#Function to display the attendance text file
def display_attendance():
    f = open("attendance_StudentID.txt", 'r') 
    content = f.read()
    print("\nAttendance")
    print("-----------")
    print(content)
 

#Function for attendance action menu
def attendance_menu():
    while True:
        if not icheckin():
            return
        # Display menu
        print("\nMain Menu:")
        print("1. Display student attendance data")
        print("2. Add attendance")
        print("3. Display average attendance")
        print("4. Exit program")
        choice = input("Enter your choice: ")

        #If the user select option 1
        if choice == "1":
            student_id = input("Enter the student ID: ")
            attendance_data = extract_attendance_data()
            if student_id in attendance_data:
                print(f"Attendance data for student {student_id}:")
                for subject, attendances in attendance_data[student_id].items():
                    #finds the line for student input and displays
                    print(f"Subject {subject} attendance: {attendances}")#f string format
            else:
                print("Student ID not found.")

        #If the user select option 2        
        elif choice == "2":
            student_id = input("Enter the student ID: ")
            subject_num = input("Enter the subject number: ")
            add_attendance(file_path, student_id, subject_num)
            #executes add attendance function
            print("Done!")
            
        #If the user select option 3       
        elif choice == "3":
            # Display average attendance
            student_id = input("Enter the student ID: ")
            attendance_data = extract_attendance_data()
            if student_id in attendance_data:
                total_numbers, count_ones = display_N_average(attendance_data[student_id])
                #executes display n average
                print(f"Total classes: {total_numbers}") #variables from display n average
                print(f"Classes attended: {count_ones}")
                print(f"Average attendance: {count_ones / total_numbers:.2f}") #.2f meaning 2 decimal points
            else:
                print("Student ID not found.")

        # If the user select option 4
        elif choice == "4":
            print("Exiting program.")
            break
        else:
          print("Invalid choice. Please enter a valid option (1, 2, 3, or 4).")






#TIMETABLE FUNCTIONS
        
#Timetable function to get the time
def getValidTime():
    while True:
        # It asks the user to input the start and end times of the course.
        startTime = input("Enter the course's start time (e.g. 12:30 in 24 hour format) :  ")
        endTime   = input("Enter the course's end time (e.g. 14:30 in 24 hour format)   :  ")
        try: # Ensure user does not input invalid input
            
            # To split the input string into hour and minute using the split(':') method
            startHour , startMinute = startTime.split(':') 
            endHour , endMinute = endTime.split(':')
            
            # Make sure the input hours and minutes are both within valid time range 
            if 1 <= int(startHour) <= 24 and 1 <= int(endHour) <= 24 and 0 <= int(startMinute) <= 60 and 0 <= int(endMinute) <= 60:
                
                # If input is valid, it will check if the end time is greater than start time
                if int(endHour) > int(startHour):
                    
                    # If everything is valid, it will format the start and end time with "AM" or "PM" based on the hours and then return them
                    if int(startHour) >= 12:
                        startTime = startTime + " PM"
                        
                    else:
                        startTime = startTime + " AM"
                        
                    if int(endHour) >= 12:
                        endTime = endTime + " PM"
                        
                    else: 
                        endTime = endTime + " AM"
                        
                    return startTime, endTime
                
                # Display error message if any input is invalid 
                else:
                     print("Error: Start time cannot be greater than end time")
                     
            else:
                print("Error: Hour cannot be below 0 and above 24, and minute cannot be below 0 or above 60")
                
        except:
             print("Invalid format: must be HH:MM (e.g. 10:30)")


#Timetable function to add a new course
def addCourse(course):
    f = open('timetables_StudentID.txt', 'a') # Open the file in append mode
    f.write(f"\nCourse Code : {course[0]}\n")
    f.write(f"Course Name : {course[1]}\n")
    f.write(f"Instructor  : {course[2]}\n")
    f.write(f"Room Number : Room {course[3]}\n")
    f.write(f"Time Slot   : {course[4]} - {course[5]}\n") 
    print("Successfully created a new course") 
    f.close()


#Timetable function to delete a course
def deleteCourse(code):
    f = open('timetables_StudentID.txt','r') # Open the file in read mode
    lines = f.readlines()
    codeToRemove = None
    i = 0
    while i < len(lines):
        if f"Course Code : {code}" in lines[i]:
            codeToRemove = i
            f.close()
            break
        i += 1
    if codeToRemove is not None:
        del lines[codeToRemove : codeToRemove+6] 
        # Deleting course details (6 lines) from the list
        f = open('timetables_StudentID.txt','w')
        f.writelines(lines) # Write modified lines to the file
        f.close()
        print("Successfully deleted a course")
    else:
        print("Error: Invalid course code")


#Timetable function to modify the timetable
def modifyTimetable(code, startTime, endTime):	
    f = open('timetables_StudentID.txt','r')
    
    # It reads all the lines in the file and stores them in lines
    lines = f.readlines()
    codeToChange = None
    i = 0
    # This will go through each lines and find the course code
    while i < len(lines):
        
        # If course code is found, it will stores the index of the line containing the course code in 'codeToChange' and close the file
        if f"Course Code : {code}" in lines[i]:
            codeToChange = i
            f.close()
            break
        i += 1
        
    # This check if 'codeToChange' is not none, indicating the course code is found
    if codeToChange is not None:
        
        # Open the file with write mode, overwriting and update the times to a new start and end times
        lines[codeToChange+4] = f"Time Slot   : {startTime} - {endTime}\n"
        
        # Update time slot for the course
        f = open('timetables_StudentID.txt','w')
        
        # Writes the updated lines back to the file and closes the file
        f.writelines(lines)
        
        f.close()
        print("Successfully change a course's timetable")
    else:
        
        # Print error message if course code is not found
        print("Error: Invalid course code")


#Timetable function
def displayTimetable(): 
    f = open('timetables_StudentID.txt', 'r') 
    content = f.read()
    print("\nTimetable")
    print("-----------")
    print(content)
    f.close()


#ASSIGNMENT FUNCTIONS    
#Function to load assignment data from file
def load_assignment_data():
    
    # Initialize an empty list to store assignment data
    assignments = []
    try:
        with open('assignments_StudentID', "r") as file:
            data = file.read().strip().split("\n\n")
            for entry in data:
                
                # Split the entry into lines and extract course code, assignment name, and status
                assignment_info = entry.strip().split("\n")
                course_code = assignment_info[0].split(": ")[1]
                assignment_name = assignment_info[1].split(": ")[1]
                status = assignment_info[2].split(": ")[1]
                
                # Append assignment details to the list of assignments
                assignments.append({"course_code": course_code, "assignment_name": assignment_name, "status": status})
        return assignments
    except FileNotFoundError:
        print("Assignment file not found.")
        return assignments


# Function to save assignment data to file
def save_assignment_data(course_code, assignment_name, status):
    
    #Construct the assignment information in string
    assignment_info = f"Course Code: {course_code}\nAssignment Name: {assignment_name}\nStatus: {status}"
    try:
        
        # Open the assignment file in append mode and write the assignment info
        with open('assignments_StudentID', 'a') as file:
            file.write('\n\n' + assignment_info)
        print("Assignment data saved successfully.")
    except FileNotFoundError: # Handle the case where the assignment file is not found
        print("Assignment file not found. Data not saved.")


#Assignment function to submit an assignment
def submit_assignment(course_code, assignment_name):
    file_path = 'assignments_StudentID.txt'
    try:
        with open(file_path, 'r') as file:
            data = file.readlines() # Read all lines in text file
        for i, line in enumerate(data):
            if f"Course Code: {course_code}" in line and f"Assignment Name: {assignment_name}" in data[i + 1]:
                # Update the status from "Pending" to "Submitted"
                data[i + 2] = "Status: Submitted\n"
                with open(file_path, 'w') as file:
                    file.writelines(data)
                print("Assignment submitted successfully.")
                return
        print("Assignment not found. Please double-check your course code and assignment name.")
    except FileNotFoundError:
        print("Assignment file not found.")

"""
#Function to check position using course code
def check_pos(course_code):
    try:
        with open('assignments_StudentID.txt', 'r') as f:
            data = f.read().split("\n\n")
            # Iterate over each assignment entry and find the position of the course code
            for pos, assignment_info in enumerate(data):
                assignment_lines = assignment_info.split("\n")
                for line in assignment_lines:
                    if f"Course Code: {course_code}" in line:
                        return pos
        print("ERROR: Course code not found!") # Handle the case where the course code is not found
        return -1
    except FileNotFoundError: # Handle the case where the assignment file is not found
        print("ERROR: Assignment file not found!")
        return -1
"""

# Function to check position using course code
def check_pos(course_code):
    try:
        with open('assignments_StudentID.txt', 'r') as f:
            data = f.read().split("\n\n")
            for pos, assignment_info in enumerate(data):
                if f"Course Code: {course_code}" in assignment_info:
                    return pos
        print("ERROR: Course code not found!")
        return -1
    except FileNotFoundError:
        print("ERROR: Assignment file not found!")
        return -1

#Assignment function to submit an assignment
def submit_assignment(course_code, assignment_name):
    file_path = 'assignments_StudentID.txt'
    try:
        
        with open(file_path, 'r') as file:
            data = file.readlines() # Read all lines in text file
            
        for i, line in enumerate(data):
            if f"Course Code: {course_code}" in line and f"Assignment Name: {assignment_name}" in data[i + 1]:
                # Update the status from "Pending" to "Submitted"
                data[i + 2] = "Status: Submitted\n"
                with open(file_path, 'w') as file:
                    file.writelines(data)
                print("Assignment submitted successfully.")
                return
            
        print("Assignment not found. Please double-check your course code and assignment name.")
        
    except FileNotFoundError:
        print("Assignment file not found.")


#Assignment function to check assignment status (for assignment menu)
def check_assignment_status(course_code, assignment_name):
    file_path = 'assignments_StudentID.txt'
    with open(file_path, 'r') as file:
        data = file.read()

    assignment_info = f"Course Code: {course_code}\nAssignment Name: {assignment_name}\nStatus: "
    pos = data.find(assignment_info)
    
    if pos != -1:
        status = data[pos + len(assignment_info):].split('\n')[0]
        print(f"Assignment Status: {status}")
    else:
        print("Assignment not found. Please double-check your course code and assignment name.")



#Function to display assignment data
def display_assignments():
    print("\nAssignments")
    print("-----------")
    f = open('assignments_StudentID.txt','r')
    print(f.read())



#Assignment function main menu options for student
def assignment_menu_students():
    print("\nAssignment Management Menu:")
    print("[1] Submit Assignment")
    print("[2] Check Assignment Status")
    print("[3] Back to Main Menu")


#Assignment function to manage assignment actions for students
def manage_assignment_actions_students():
    while True:
        assignment_menu_students()
        choice = input("Enter your choice: ")
        if choice == "1":
            course_code = input("Enter course code: ")
            assignment_name = input("Enter assignment name: ")
            submit_assignment(course_code, assignment_name)
        elif choice == "2":
            course_code = input("Enter course code: ")
            assignment_name = input("Enter assignment name: ")
            check_assignment_status(course_code, assignment_name)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


#Assignment function main menu options for faculty
def assignment_menu_faculty():
    print("[1] Display assignments")
    print("[2] Edit assignment status")
    print("[3] Exit")


#Assignment function to manage assignment actions for faculty
def manage_assignment_actions_faculty():
    while True:
        assignment_menu_faculty()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_assignments()
            
        elif choice == "2":
            course_code = input("Enter course code: ")
            assignment_name = input("Enter assignment name: ")
            new_status = input("Enter new status: ")
            update_assignment_status(course_code, assignment_name, new_status)
            
        elif choice == "3":
            break
        
        else:
            print("Invalid choice. Please try again.")


# Assignment function to update assignment status (for faculty)
def update_assignment_status(course_code, assignment_name, new_status):
    # Get the position of the assignment in the file
    pos = check_pos(course_code)
    if pos == -1:
        # Handle the case where the course code is not found
        print("Error: Course code not found.")
        return
    # Open the assignment file in read mode
    with open('assignments_StudentID.txt', 'r') as file:
        data = file.read()
        # Check if the assignment exists in the file
        if f"Course Code: {course_code}\nAssignment Name: {assignment_name}" in data:
            # Replace the old status with the new status
            updated_data = data.replace(f"Status: {assignment_name}\n", f"Status: {new_status}\n")
            # Write the updated data back to the file
            with open('assignments_StudentID.txt', 'w') as file:
                file.write(updated_data)
            print("Assignment status updated successfully.")
        else:
            # Handle the case where the assignment is not found
            print("Assignment not found. Please double-check your course code and assignment name.")



#Main Program
exit = False
while exit == False:
    print("\nWelcome to EduHub University's Classroom Management System!")
    print("Are you a student or a faculty member?")
    print("[1] Student")
    print("[2] Faculty")
    num = int(input("Enter 1 or 2: "))
    
    if num == 1:
        print("Main Menu")
        print("[1] Attendance")
        print("[2] Timetable")  
        print("[3] Assignment")
        print("[4] Display")
        print("[5] Exit")
        num = int(input("Enter 1, 2, 3, 4, or 5: "))

        if num == 1: #Attendance
            attendance_menu()
          
        elif num == 2: #Timetable (Students)
            displayTimetable() 
        
        elif num == 3: #Assignment (Students)
            display_attendance()
            display_assignments()#Display assignments
            manage_assignment_actions_students()

        elif num == 4: #Display everything
            display_attendance()
            displayTimetable()
            display_assignments()
            
        elif num == 5: #Exit
            print("Thank you for using our program! :)")
            exit = True #Exiting the program
        
        else:
            print("ERROR: Wrong input!")

    elif num == 2:
        password = input("What is the password: ") 
        
        if password == "password":
            print("[1] Edit Timetable")
            print("[2] Update Assignment status")
            print("[3] Exit")
            num = int(input("Enter option: "))
                    
            if num == 1: #Timetable(Faculty)
                 while True:
                        print("[1] Create a new course for the timetable")
                        print("[2] Update existing course timetable")
                        print("[3] Delete a course from the timetable")
                        print("[4] Display the current timetable")
                        print("[5] Exit ")
                        option = int(input("Enter option :  "))
                        
                        if option == 1: #Create a new course for the timetable
                            courseCode = input("Enter the course code: ")
                            courseName = input("Enter the course name: ")
                            instructor = input("Enter the instructor's name: ")
                            while True:
                                try:
                                    roomNum = int(input("Enter the room number: "))
                                    break
                                except:
                                    print("Error: Enter valid room number")
                            startTime, endTime = getValidTime()
                            newCourse = course = [courseCode, courseName, instructor, roomNum, startTime, endTime]
                            addCourse(newCourse)
                            
                        elif option == 2: #Update existing course for the timetable
                            displayTimetable()
                            courseCode = input("Which course's timetable do you want to change?\nEnter the course code you want to change :   ")
                            startTime, endTime = getValidTime()
                            modifyTimetable(courseCode, startTime, endTime)
                            
                        elif option == 3: #Delete a course from the timetable
                            displayTimetable()
                            code = input("Enter the course code you want to delete :   ")
                            deleteCourse(code)
                            
                        elif option == 4: #Display the current timetable
                            displayTimetable()
                            
                        elif option == 5: #Exit
                            print("Thank you for using our program! :)")
                            break #Exiting the program
                        
                        else:
                            print("Invalid Option!")   
                        
            elif num == 2: #Assignments (Faculty)
                manage_assignment_actions_faculty()

            elif num == 3: #Exit
                print("Thank you for using our program! :)")
                exit = True #Exiting the program
                    
            else:
                    print("ERROR: Wrong input!")
                    
        else:
            print("Wrong Password!")

    else:
        print("ERROR: Wrong input!")




