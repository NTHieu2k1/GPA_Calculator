from calculator import input_data, calc

# External tools for updating the database
def subject_updater():
    import sqlite3

    # Open data file
    try:
        fu_subject_dataFile = "FU_subjects.txt"
        fu_subject_data = open(fu_subject_dataFile, encoding='utf-8')
    except: # Aborting the process if required file not found
        print("Raw data file not found. Updating failed. Aborting...\n")
        return None

    # Connect to the database
    fu_subject_db = sqlite3.connect("FU All Subjects.db")
    cursor = fu_subject_db.cursor()

    # Initialize the database
    print("Resetting the database... ", end = '')
    init_db = """
    DROP TABLE IF EXISTS Subjects;

    CREATE TABLE Subjects
    (
        Subject_Code    TEXT    PRIMARY KEY UNIQUE,
        Subject_Name    TEXT,
        No_of_Credits   INTEGER
    );
    """
    cursor.executescript(init_db)
    print("Done.")

    # Read data file, and import to the database
    print("Updating...",)
    for subject in fu_subject_data:
        # Extract data
        component_list = subject.split("\t")
        subject_code = component_list[0]
        subject_name = component_list[1]
        no_of_credits = component_list[2]
        # Import extracted items into the database
        cursor.execute("""
        INSERT OR IGNORE INTO Subjects(Subject_Code, Subject_Name, No_of_Credits)
        VALUES (?, ?, ?);""", (subject_code, subject_name, no_of_credits))
        fu_subject_db.commit()

    # Finish the process and exiting
    print("Subjects updating sucessfully! Database updated!\n")
    cursor.close()

# Show menu option
def show_menu():
    print("MENU:\n1- Calculate your GPA score\n2- Updating the subject database")

# Select the option (based on the menu), and validate
def select_option():
    while True:
        try:
            option = int(input("Choose: "))
            if option != 1 and option != 2:
                print("Invalid option. Please choose again.")
                continue
            return option
        except:
            print("Invalid input. Try again!")

# Main program, all functions of the program are in here
def main():
    print("\tGPA Calculator\n")

    # Show menu option, and choose option
    show_menu()
    option = select_option()

    if option == 1: # Option 1
        # Input data (subject codes and their mark)
        subject_data = input_data.input_mark_data()

        # Get GPA score
        student = calc.Student(subject_data)
        total_marks = student.get_total_mark()
        total_credits = student.get_sum_credits()
        gpa = student.get_GPA_score(total_marks, total_credits)

        # Print GPA score
        print("Your GPA:", gpa)
    
    elif option == 2: # Option 2
        subject_updater()

    # Ask for continue, or exit
    cont = input("Do you want to continue? (Y/N) ")
    if cont[0] == 'Y' or cont[0] == 'y':
        print("\n")
        main()

main()