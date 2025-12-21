from domains import student as s
from domains import course as c
from input import courseList, studentList, inputStudent, inputCourse, inputMark
import input
from output import listCourse, listCourseAlt, listStudent, listStudentAlt, calcGPA, showStudentMarks, showStudentMarksAlt, sortByGPA, sortByGPAAlt
import zipfile
import os


def extracter():
    if os.path.exists("students.dat.zip") == True:
        with zipfile.ZipFile("students.dat.zip", "r") as zipper:
            zipper.extractall()
        if os.path.exists("students.txt") == True:
            with open("students.txt", "r") as file:
                linesList = file.readlines()
                index = -1
                nameIndex = 0
                idIndex = 0
                dobIndex = 0
                while index <= len(linesList) - 5:
                    nameIndex = index + 1
                    idIndex = index + 2
                    dobIndex = index + 3
                    inputStudent(linesList[nameIndex].strip(), linesList[idIndex].strip(), linesList[dobIndex].strip(), False)
                    index += 4
        if os.path.exists("courses.txt") == True:
            with open("courses.txt", "r") as file:
                linesList = file.readlines()
                index = -1
                nameIndex = 0
                idIndex = 0
                creditIndex = 0
                while index <= len(linesList) - 5:
                    nameIndex = index + 1
                    idIndex = index + 2
                    creditIndex = index + 3
                    inputCourse(linesList[nameIndex].strip(), linesList[idIndex].strip(), int(linesList[creditIndex].strip()), False)
                    index += 4
        if os.path.exists("marks.txt") == True:
            with open("marks.txt", "r") as file:
                linesList = file.readlines()
                index = -1
                theCourseIndex = 0
                theStudentIndex = 0
                markIndex = 0
                while index <= len(linesList) - 5:
                    theCourseIndex = index + 1
                    for i in range(len(courseList)):
                        if linesList[theCourseIndex].strip() == courseList[i].getCourseName():
                            theCourseIndex = i
                    theStudentIndex= index + 2
                    for i in range(len(studentList)):
                        if linesList[theStudentIndex].strip() == studentList[i].getID():
                            theStudentIndex = i
                    markIndex = index + 3
                    inputMark(courseList[theCourseIndex], studentList[theStudentIndex], float(linesList[markIndex].strip()), False)
                    index += 4
        os.remove("students.dat.zip")

def zipper():
    with zipfile.ZipFile("students.dat.zip", mode="a", compression=zipfile.ZIP_DEFLATED) as zipper:
        try: 
            zipper.write("students.txt")
            os.remove("students.txt")
        except FileNotFoundError: pass
        try: 
            zipper.write("courses.txt")
            os.remove("courses.txt")
        except FileNotFoundError: pass
        try: 
            zipper.write("marks.txt")
            os.remove("marks.txt")
        except FileNotFoundError: pass
        try: 
            zipper.write("marks2.txt")
            os.remove("marks2.txt")
        except FileNotFoundError: pass

def controller():
    import datetime
    import time
    extracter()
    option = 1e-10
    while option != 0:
        print("Choose:")
        print("     1.Input student")
        print("     2.Input course")
        print("     3.Input mark")
        print("     4.List students")
        print("     5.List courses")
        print("     6.Show students' marks for a course")
        print("     7.Calculate GPA of a student")
        print("     8.Sort the student list by GPA in descending order")
        print("     0.Exit")
        try:
            option = int(input("You choose?> "))
        except ValueError:
            print("Error 233: Invalid input")
            print()
            time.sleep(1)
            continue
        if option not in range(0,9):
            print("Error 238: Invalid option. Try again")
            print()
            time.sleep(1)
            continue
        else:
            if option == 1:
                print()
                name = input("Enter the student's name> ")
                id = input("Enter the student's ID> ")
                check = False
                while check == False:
                    try:
                        predob = input("Enter the student's DOB (DD/MM/YYYY)> ")
                        middob = datetime.datetime.strptime(predob, "%d/%m/%Y")
                        check = True
                    except ValueError:
                        print("Error 254: Invalid format")
                        continue
                dob = middob.strftime("%d/%m/%Y")
                input.inputStudent(name, id, dob, True)
            elif option == 2:
                print()
                name = input("Input course's name> ")
                id = input("Input course's ID> ")
                try: credit = int(input("Input course's credit> "))
                except ValueError: 
                    print("Error 264: Invalid input")
                    option = 2
                    continue
                input.inputCourse(name, id, credit, True)
            elif option == 3:
                global studentList
                global courseList
                print()
                choice = -1
                choice2 = -1
                mark = None
                print("Select course: ")
                listCourse()
                try:
                    choice = int(input("You choose?> "))
                except ValueError: 
                    print("Error 280: Invalid input")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                if choice not in range(len(courseList)):
                    print("Error 286: Option not exist. Try again")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                print("Select student: ")
                listStudent()
                try: 
                    choice2 = int(input("You choose?> "))
                except ValueError: 
                    print("Error 296: Invalid input")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                if choice2 not in range(len(studentList)):
                    print("Error 302: Option not exist. Try again")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                try:
                    mark = int(input("Input mark for the selected student> "))
                except ValueError:
                    print("Error 310: Invalid input")
                    continue
                input.inputMark(courseList[choice], studentList[choice2], mark, True)
            elif option == 4:
                print()
                listStudent()
                time.sleep(3)
            elif option == 5:
                print()
                listCourse()
                time.sleep(3)
            elif option == 6:
                print()
                choice = -1
                print("Select course: ")
                listCourse()
                try: choice = int(input("You choose?> "))
                except ValueError: 
                    print("Error 328: Invalid input")
                    option = 6
                    print()
                    time.sleep(1)
                    continue
                if choice not in range(len(courseList)):
                    print("Error 334: Course not exist. Try again")
                    option = 3
                    print()
                    time.sleep(1)
                    continue
                print(showStudentMarks(courseList[choice]))
            elif option == 7:
                choice = -1
                print()
                print("Select student: ")
                listStudent()
                try: 
                    choice = int(input("You choose?> "))
                except ValueError: 
                    print("Error 348: Invalid input")
                    option = 7
                    print()
                    time.sleep(1)
                    continue
                if choice not in range(len(studentList)):
                    print("Error 354: Option not exist. Try again")
                    option = 7
                    print()
                    time.sleep(1)
                    continue
                print(f"GPA (All unassigned grade = 0) = {calcGPA(studentList[choice])}")
                time.sleep(3)
            elif option == 8:
                print()
                print(sortByGPA())
                time.sleep(3)
            elif option == 0:
                option = 0
                zipper()
                pass
            else:
                print("How did you get here? Go back!")
                continue
            time.sleep(0.5)

#controller()

import curses
def main(stdscr):
    import time
    import datetime
    extracter()
    option = -1
    curses.curs_set(1)
    curses.echo()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.clear()
    while option != 0:
        stdscr.addstr(0,40,"Welcome to buttered version of the program", curses.color_pair(3))
        stdscr.addstr(1,50, "Let's get started", curses.color_pair(4))
        stdscr.addstr(3,0,"Choose:", curses.color_pair(3))
        stdscr.addstr(4,6,"1.Input student", curses.color_pair(1))
        stdscr.addstr(5,6,"2.Input course", curses.color_pair(1))
        stdscr.addstr(6,6,"3.Input mark", curses.color_pair(1))
        stdscr.addstr(7,6,"4.List students", curses.color_pair(1))
        stdscr.addstr(8,6,"5.List courses", curses.color_pair(1))
        stdscr.addstr(9,6,"6.Show students' marks for a course", curses.color_pair(1))
        stdscr.addstr(10,6,"7.Calculate GPA of a student", curses.color_pair(1))
        stdscr.addstr(11,6,"8.Sort the student list by GPA in descending order", curses.color_pair(1))
        stdscr.addstr(12,6,"0.Exit",curses.color_pair(1))

        stdscr.refresh()

        while option not in range(9):
            stdscr.addstr(14,0,"You choose?> ", curses.color_pair(5))
            stdscr.refresh()
            window = curses.newwin(1,50, 14, 13)
            option = window.getstr(0,0,3)
            option = option.decode('utf-8')
            try: option = int(option)
            except ValueError: 
                window = curses.newwin(1, 50, 15, 0)
                window.addstr(0,0,"Error 415: Invalid option", curses.color_pair(2))
                window.refresh()
                time.sleep(0.5)
                window.clear()
                window.refresh()
                option = -1
                continue
            if option not in range(9):
                window = curses.newwin(1, 50, 15, 0)
                window.addstr(0,0,"Error 424: Invalid option", curses.color_pair(2))
                window.refresh()
                time.sleep(0.5)
                window.clear()
                window.refresh()
                option = -1
                continue
            time.sleep(0.5)


        stdscr.clear()
        stdscr.refresh()
        if option == 1:
            stdscr.addstr(0,0,"Enter the student's name> ", curses.color_pair(5))
            stdscr.refresh()
            name = stdscr.getstr(0,26,50)
            name = name.decode('utf-8')
            stdscr.addstr(1,0,"Enter the student's ID> ", curses.color_pair(5))
            stdscr.refresh()
            id = stdscr.getstr(1,24, 50)
            id = id.decode('utf-8')
            window = curses.newwin(2, 100, 2, 0)
            check = False
            while check == False:
                try:
                    window.addstr(0,0, "Enter the student's DOB (DD/MM/YYYY)> ", curses.color_pair(5))
                    window.refresh()
                    predob = window.getstr(0,38, 16)
                    predob = predob.decode('utf-8')
                    middob = datetime.datetime.strptime(predob, "%d/%m/%Y")
                    check = True
                except ValueError:
                    window.addstr(1,0, "Error 447: Invalid format", curses.color_pair(2))
                    window.refresh()
                    time.sleep(0.5)
                    option = -1
                    window.clear()
                    window.refresh()
                    continue
            dob = middob.strftime("%d/%m/%Y")
            input.inputStudent(name, id, dob, True)
            option = -1
            window.clear()
            window.refresh()
            stdscr.clear()
            stdscr.refresh()
        elif option == 2:
            stdscr.addstr(0,0, "Input course's name> ", curses.color_pair(5))
            stdscr.refresh()
            name = stdscr.getstr(0, 21, 50)
            name = name.decode('utf-8')
            stdscr.addstr(1,0, "Input course's ID> ", curses.color_pair(5))
            stdscr.refresh()
            id = stdscr.getstr(1, 19, 50)
            id = id.decode('utf-8')
            try: 
                stdscr.addstr(2, 0, "Input course's credit> ", curses.color_pair(5))
                stdscr.refresh()
                credit = stdscr.getstr(2, 23, 5)
                credit = credit.decode('utf-8')
                credit = int(credit)
            except ValueError:
                stdscr.addstr(3,0,"Error 477: Invalid input", curses.color_pair(2))
                stdscr.refresh()
                option = 2
                stdscr.clear()
                stdscr.refresh()
                option = -1
                continue
            input.inputCourse(name, id, credit, True)
            option = -1
            stdscr.clear()
            stdscr.refresh()
        elif option == 3:
            global studentList
            global courseList
            choice = -1
            choice2 = -1
            mark = None
            position = 0
            maxIndex = 0
            stdscr.addstr(position,0,"Select course: ", curses.color_pair(3))
            stdscr.refresh()
            position += 1
            if len(listCourseAlt()) <= 0:
                stdscr.addstr(position, 0, "Warning 500: No courses", curses.color_pair(4))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            else:
                for index in range(len(listCourseAlt())):
                    stdscr.addstr(position + index, 0, listCourseAlt()[index], curses.color_pair(1))
                    maxIndex += 1
                position += maxIndex
                maxIndex = 0
                stdscr.refresh()
            try:
                stdscr.addstr(position, 0, "You choose?> ", curses.color_pair(5))
                stdscr.refresh()
                choice = stdscr.getstr(position, 13, 5)
                choice = choice.decode('utf-8')
                choice = int(choice)
                position += 1
            except ValueError:
                position += 1
                stdscr.addstr(position, 0, "Error 524: Invalid input", curses.color_pair(2))
                stdscr.refresh()
                position += 1
                option = -1
                time.sleep(1)
                stdscr.clear()
                stdscr.refresh()
                continue
            if choice not in range(len(courseList)):
                stdscr.addstr(position, 0, "Error 533: Option not exist. Try again", curses.color_pair(2))
                stdscr.refresh()
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                time.sleep(1)
                continue
            stdscr.addstr(position, 0, "Select student: ", curses.color_pair(3))
            position += 1
            stdscr.refresh()
            if len(listStudentAlt()) <= 0:
                stdscr.addstr(position, 0, "Warning 545: No students", curses.color_pair(4))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            else:
                for index in range(len(listStudentAlt())):
                    stdscr.addstr(position+index, 0, listStudentAlt()[index], curses.color_pair(1))
                    maxIndex += 1
                position += maxIndex
                maxIndex = 0
                stdscr.refresh()
            try: 
                stdscr.addstr(position, 0, "You choose?> ", curses.color_pair(5))
                stdscr.refresh()
                choice2 = stdscr.getstr(position, 13, 5)
                choice2 = choice2.decode('utf-8')
                choice2 = int(choice2)
                position += 1
            except ValueError:
                position += 1
                stdscr.addstr(position, 0, "Error 569: Invalid input", curses.color_pair(2))
                stdscr.refresh()
                option = -1
                time.sleep(1)
                position += 1
                stdscr.clear()
                stdscr.refresh()
                continue
            if choice2 not in range(len(studentList)):
                stdscr.addstr(position, 0, "Error 578: Option not exist. Try again", curses.color_pair(2))
                stdscr.refresh()
                option = -1
                time.sleep(1)
                position += 1
                stdscr.clear()
                stdscr.refresh()
                continue
            try:
                stdscr.addstr(position, 0, "Input mark for the selected student> ", curses.color_pair(5))
                stdscr.refresh()
                mark = stdscr.getstr(position, 37, 5)
                mark = mark.decode('utf-8')
                mark = int(mark)
                position += 1
            except ValueError:
                position += 1
                stdscr.addstr(position, 0, "Error 595: Invalid input", curses.color_pair(2))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            input.inputMark(courseList[choice], studentList[choice2], mark, True)
            option = -1
            time.sleep(1)
            stdscr.clear()
            stdscr.refresh()
        elif option == 4:
            position = 0
            maxIndex = 0
            if len(listStudentAlt()) <= 0:
                stdscr.addstr(position, 0, "(empty)", curses.color_pair(6))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            else:
                for index in range(len(listStudentAlt())):
                    stdscr.addstr(position+index, 0, listStudentAlt()[index], curses.color_pair(1))
                    maxIndex += 1
                position += maxIndex
                maxIndex = 0
                stdscr.refresh()
            time.sleep(3)
            option = -1
            stdscr.clear()
            stdscr.refresh()
        elif option == 5:
            position = 0
            maxIndex = 0
            if len(listCourseAlt()) <= 0:
                stdscr.addstr(position, 0, "(empty)", curses.color_pair(6))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            else:
                for index in range(len(listCourseAlt())):
                    stdscr.addstr(position + index, 0, listCourseAlt()[index], curses.color_pair(1))
                    maxIndex += 1
                position += maxIndex
                maxIndex = 0
                stdscr.refresh()
            time.sleep(3)
            option = -1
            stdscr.clear()
            stdscr.refresh()
        elif option == 6:
            choice = -1
            position = 0
            maxIndex = 0
            stdscr.addstr(0,0,"Select course: ", curses.color_pair(3))
            position += 1
            stdscr.refresh()
            if len(listCourseAlt()) <= 0:
                stdscr.addstr(position, 0, "(empty)", curses.color_pair(6))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            else:
                for index in range(len(listCourseAlt())):
                    stdscr.addstr(position + index, 0, listCourseAlt()[index], curses.color_pair(1))
                    maxIndex += 1
                position += maxIndex
                maxIndex = 0
                stdscr.refresh()
            try:
                stdscr.addstr(position, 0, "You choose?> ", curses.color_pair(5))
                stdscr.refresh()
                choice = stdscr.getstr(position, 13, 5)
                choice = choice.decode('utf-8')
                choice = int(choice)
                position += 1
            except ValueError: 
                position += 1
                stdscr.addstr(position, 0, "Error 685: Invalid input", curses.color_pair(2))
                stdscr.refresh()
                position += 1
                time.sleep(1)
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            if choice not in range(len(courseList)):
                stdscr.addstr(position, 0, "Error 694: Course not exist. Try again", curses.color_pair(2))
                stdscr.refresh()
                position += 1
                time.sleep(1)
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            stdscr.clear()
            stdscr.refresh()
            maxIndex = 0
            if type(showStudentMarksAlt(courseList[choice])) == str:
                if showStudentMarksAlt(courseList[choice])[0:8] == "Warning ":
                    stdscr.addstr(0,0, showStudentMarksAlt(courseList[choice]), curses.color_pair(4))
                else:
                    stdscr.addstr(0,0, showStudentMarksAlt(courseList[choice]), curses.color_pair(2))
                stdscr.refresh()
                time.sleep(1)
                stdscr.clear()
                stdscr.refresh()
                option = -1
                continue
            else:
                tempList = list(showStudentMarksAlt(courseList[choice]).keys())
                for index in range(len(showStudentMarks(courseList[choice]))):
                    stdscr.addstr(maxIndex + index, 0, f"{tempList[index]}: {showStudentMarks(courseList[choice])[tempList[index]]}", curses.color_pair(1))
                    maxIndex += 1
                maxIndex = 0
                stdscr.refresh()
                time.sleep(3)
                option = -1
                stdscr.clear()
                stdscr.refresh()
        elif option == 7:
            choice = -1
            position = 0
            maxIndex = 0
            stdscr.addstr(0,0,"Select student: ", curses.color_pair(3))
            position += 1
            stdscr.refresh()
            if len(listStudentAlt()) <= 0:
                stdscr.addstr(position, 0, "(empty)", curses.color_pair(6))
                stdscr.refresh()
                time.sleep(1)
                position += 1
                option = -1
                stdscr.clear()
                stdscr.refresh()
                continue
            else:
                for index in range(len(listStudentAlt())):
                    stdscr.addstr(position+index, 0, listStudentAlt()[index], curses.color_pair(1))
                    maxIndex += 1
                position += maxIndex
                maxIndex = 0
                stdscr.refresh()
                try: 
                    stdscr.addstr(position, 0, "You choose?> ", curses.color_pair(5))
                    stdscr.refresh()
                    choice = stdscr.getstr(position, 13, 5)
                    choice = choice.decode('utf-8')
                    choice = int(choice)
                    position += 1
                except ValueError: 
                    position += 1
                    stdscr.addstr(position, 0, "Error 758: Invalid input", curses.color_pair(2))
                    stdscr.refresh()
                    time.sleep(1)
                    option = -1
                    stdscr.clear()
                    stdscr.refresh()
                    continue
                if choice not in range(len(studentList)):
                    stdscr.addstr(position, 0, "Error 766: Option not exist. Try again", curses.color_pair(2))
                    stdscr.refresh()
                    time.sleep(1)
                    option = -1
                    stdscr.clear()
                    stdscr.refresh()
                    continue
                stdscr.addstr(position, 0, f"GPA (All unassigned grade = 0) = {calcGPA(studentList[choice])}", curses.color_pair(1))
                stdscr.refresh()
                time.sleep(3)
                option = -1
                stdscr.clear()
                stdscr.refresh()
        elif option == 8:
            maxIndex = 0
            if type(sortByGPAAlt()) == str:
                stdscr.addstr(0,0, sortByGPAAlt(), curses.color_pair(2))
                stdscr.refresh()
                time.sleep(1)
                stdscr.clear()
                stdscr.refresh()
                option = -1
                continue
            else:
                if len(sortByGPAAlt()) <= 0:
                    stdscr.addstr(0,0, "(Empty)", curses.color_pair(6))
                else:
                    tempList = list(sortByGPAAlt().keys())
                    for index in range(len(sortByGPAAlt())):
                        stdscr.addstr(maxIndex + index, 0, f"{tempList[index]}: {sortByGPAAlt()[tempList[index]]}", curses.color_pair(1))
                        maxIndex += 1
                    maxIndex = 0
                stdscr.refresh()
                time.sleep(3)
                option = -1
                stdscr.clear()
                stdscr.refresh()
        elif option == 0:
            option = 0
            zipper()
            pass
        else:
            stdscr.addstr(0,0,"How did you get here? Go back!", curses.color_pair(3))
            stdscr.refresh()
            time.sleep(0.5)
            continue
    stdscr.refresh()

curses.wrapper(main)

