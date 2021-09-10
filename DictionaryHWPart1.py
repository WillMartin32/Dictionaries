def main():
    choice = 'y'
    while choice == 'y' or choice == 'Y':
        selected_course = input("\n>>>Enter a course number: ")
        create_dict(selected_course)
        choice = input("\n\n>>>Would you like to search again (Y/N)? ")


def create_dict(course):
    all_courses = {"CS101":{"Room Number":"3004", "Instructor":"Haynes", "Meeting Time":"8:00 a.m."}, 
        "CS102":{"Room Number":"4501", "Instructor":"Alvarado", "Meeting Time":"9:00 a.m."},
        "CS103":{"Room Number":"6755", "Instructor":"Rich", "Meeting Time":"10:00 a.m."},
        "NT110":{"Room Number":"1244", "Instructor":"Burke", "Meeting Time":"11:00 a.m."},
        "CM241":{"Room Number":"1411", "Instructor":"Lee", "Meeting Time":"1:00 p.m."}}
        
    if course in all_courses:
        print("\n", "--For Course ", course,": Room Number is ", all_courses[course]["Room Number"], ", Instructor is ",
        all_courses[course]["Instructor"], ", and Meeting Time is ", all_courses[course]["Meeting Time"], sep='')
    else:
        print("\n>>>Course Not Found!")
    
    
main()