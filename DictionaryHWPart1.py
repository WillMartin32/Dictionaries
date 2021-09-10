def main():
    all_courses = {"CS101":{"Room Number":"3004", "Instructor":"Haynes", "Meeting Time":"8:00 a.m."}, 
                "CS102":{"Room Number":"4501", "Instructor":"Alvarado", "Meeting Time":"9:00 a.m."},
                "CS103":{"Room Number":"6755", "Instructor":"Rich", "Meeting Time":"10:00 a.m."},
                "NT110":{"Room Number":"1244", "Instructor":"Burke", "Meeting Time":"11:00 a.m."},
                "CM241":{"Room Number":"1411", "Instructor":"Lee", "Meeting Time":"1:00 p.m."}}

    choice = 'y'
    while choice == 'y' or choice == 'Y':
        selected_course = input("\n>>>Enter a course number: ")
        course_search(selected_course, all_courses)
        choice = input("\n\n>>>Would you like to search again (Y/N)? ")


def course_search(course, list):
        
    if course in list:
        print("\n", "--For Course ", course,": Room Number is ", list[course]["Room Number"], ", Instructor is ",
        list[course]["Instructor"], ", and Meeting Time is ", list[course]["Meeting Time"], sep='')
    else:
        print("\n>>>Course Not Found!")
    
    
main()