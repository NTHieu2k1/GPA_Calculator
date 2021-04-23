from calculator import calc

def input_mark_data():
    subject_list = dict()

    # Input subject codes and their marks, then put to the map
    while(True):
        subject_id = input_subject_code()
        mark = input_mark()
        subject_list[subject_id] = mark
        fin = input("Finish? (Y/N) ")
        # Finish entering if user want to exit
        if fin[0] == 'Y' or fin[0] == 'y':
            break
    
    return subject_list

def input_subject_code():
    while(True):
        # Input subject code
        subject_id = input("Enter your subject ID\n(or you can just enter first 3 letters of the ID): ")
        if not calc.is_exist_subject_id(subject_id):
            # Filter subject ID if user enter first 3 letters of their subject code
            if len(subject_id) == 3:
                subject_id = subject_id.upper()
                filtered_subject_id_list = calc.filter_subject_ID(subject_id)
                size = len(filtered_subject_id_list)
                # Show hints for entering correct subject ID
                if size == 1:
                    cf = input("You mean " + filtered_subject_id_list[0] + "? (Y/N) ")
                    if cf[0] == 'Y' or cf[0] == 'y':
                        subject_id = filtered_subject_id_list[0]
                        print("You choose " + subject_id)
                    else:
                        print("Sorry, subject code you want to find is not available. Enter another one.")
                        continue
                elif size > 1:
                    count = 0
                    print("There are " + str(size) + " subject codes available")
                    for id in filtered_subject_id_list:
                        count += 1
                        print(str(count) + ". " + id)
                    try:
                        select = int(input("Select: "))
                    except:
                        print("Invalid code. Could not get your selection. Enter another one.")
                        continue
                    if select <= 0 or select > size:
                        print("Sorry, subject code you want to find is not available. Enter another one.")
                        continue
                    else:
                        subject_id = filtered_subject_id_list[select - 1]
                        print("You choose " + subject_id)
                else:
                    print("Invalid code. Enter again.")
                    continue
            else:
                print("The subject with the code is not available, or invalid code. Enter again.")
                continue
        # Ignore subjects that are not used for calculating GPA
        # Ignore English Preparation subjects
        if subject_id[0:3] == "EN0" or subject_id[0:3] == "ENT":
            print("This is an English Preparation subject, which is not used to get the GPA. Enter another one.")
            continue
        elif subject_id[0:3] == "LUK" or subject_id[0:3] == "TRS":
            print("This is an English Preparation subject, which is not used to get the GPA. Enter another one.")
            continue
        elif subject_id == "Global Citizen" or subject_id == "Global Citizen LUK5":
            print("This is an English Preparation subject, which is not used to get the GPA. Enter another one.")
            continue
        # Ignore Military Training subject
        if subject_id == "GDQP":
            print("This is the Military Training subject, which is not used to get the GPA. Enter another one.")
            continue
        # Ignore Physical Training subjects
        if subject_id[0:3] == "COV" or subject_id[0:2] == "VO":
            print("This is a Physical Training subject, which is not used to get the GPA. Enter another one.")
            continue
        # Ignore On-the-job Training subjects
        if subject_id[0:2] == "OJ":
            print("This is an On-the-job Training subject, which is not used to get the GPA. Enter another one.")
            continue
        # Ignore Musical Instrument subjects
        if subject_id == "TMI101" or subject_id[0:3] == "TRG" or subject_id[0] == "Đ":
            print("This is a Musical Instrument subject, which is not used to get the GPA. Enter another one.")
            continue
        # Ignore Extra activities
        if subject_id[0:3] == "EXO":
            print("This is an extra activity, which is not used to get the GPA. Enter another one.")
            continue
        elif subject_id[0:3] == "ORG" or subject_id[0:3] == "ORT":
            print("This is an extra activity, which is not used to get the GPA. Enter another one.")
            continue
        elif subject_id == "PCCC" or subject_id[0:3] == "PDP":
            print("This is an extra activity, which is not used to get the GPA. Enter another one.")
            continue
        # Ignore Lab subjects
        if subject_id[0:3] == "LAB":
            print("Usually, there are no marks given in the Lab subjects, so you cannot use this subject to get GPA. Enter another one.")
            continue
        break
    return subject_id

def input_mark():
    while(True):
        try:
            mark = float(input("Enter your mark: "))
        except:
            print("Please input a number. Enter again.")
            continue
        # Only accept marks are in range 0 - 10
        if mark < 0 or mark > 10:
            print("Mark input must be in range 0 - 10. Enter again.")
            continue
        break
    return mark