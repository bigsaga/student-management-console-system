from console_color import*
from student import Student

#creating database
student_database = []

# Welcome screen menu
def welcome_screen():
    print(YELLOW, '***** Welcome To NIIT Student Management System*****')
    user_input = int(input(WHITE + '1. Add Student\n'
                                   '2. Add all student details\n'
                                   '3. Search for student datails\n'
                                   '4. Delete student info\n'
                                   '5. Update student info\n'
                                   '6. about system\n'
                                   '7. Exit Application\n\n'
                                   'Please Provide Your Request : '))
    user_option(user_input)

#user option
def user_option(user_input):
    if user_input == 1:
        response = 'yes'
        while response == 'yes':
            student_info = add_student_info()
            user_answer = input(BLUE + 'Do you want to save info?(y/n) : ').lower()
            if user_answer == 'y':
                student_database.append(student_info)
                print(GREEN, f'{student_info.get_first_name()}'' ' 
                             f'{student_info.get_middle_name()}'' '
                             f'{student_info.get_last_name()} '' '
                             f' has been save successfully,')
            elif user_answer == 'n':
                user_answer = input('are you sure?(y/n) : ').lower()
                if user_answer == 'y':
                    welcome_screen()
            else:
                student_database.append(student_info)
        else:
            welcome_screen()
        response = input('is there another student? (y/n) : ').lower()
        welcome_screen()

    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        pass
    elif user_input == 5:
        pass
    elif user_input == 6:
        about_us()
    elif user_input == 7:
        close_program()
    else:
        invalid_request()

def about_us():
    print(BLUE, '***** This System Keep Track Of Student Details *****')
    welcome_screen()

def close_program():
    print(BLUE, '***** Thanks You For Using NIIT SMS, Hope To See You Again *****')
    exit(1)

def invalid_request():
    print(RED, 'Request Invalid, Please Try Again. Thank You')
    welcome_screen()

def add_student_info():
    print(YELLOW, '***** Fill Details Below To Add Student *****', WHITE)
    id = input('Provide student ID : ')
    first_name = input('Provide First Name : ')
    middle_name = input('Provide Middle Name : ')
    last_name = input('Provide Last Name : ')
    dob = input('Provide DOF e.g(dd-mm-yyyy) : ')
    course = input('Provide Course : ')
    period = input('Provide Period : ')

#   creating student objet
    student_info = Student(id, first_name, middle_name, last_name, dob, course, period)
    return student_info


# calling function
welcome_screen()
