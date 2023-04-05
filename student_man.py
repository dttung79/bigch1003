# Viết chương trình quản lý sinh viên có các chức năng sau:
# 1. Thêm sinh viên (mã sinh viên, họ tên, điểm trung bình)
# 2. Sửa thông tin sinh viên (nhập mã, tìm theo mã và sửa thông tin)
# 3. Xóa sinh viên (nhập mã, tìm theo mã và xóa)
# 4. Tìm kiếm sinh viên theo tên (2 lựa chọn là tìm gần đúng hoặc tìm chính xác)
# 5. Hiển thị danh sách sinh viên (2 lựa chọn là sắp xếp theo tên hoặc theo điểm)

students = {}
EXACT = 1
IN_NAME = 2
ADD = 1
EDIT = 2
DELETE = 3
SEARCH = 4
DISPLAY = 5
EXIT = 6

def main():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == ADD:
            add_student()
        elif choice == EDIT:
            edit_student()
        elif choice == DELETE:
            delete_student()
        elif choice == SEARCH:
            search()
        elif choice == DISPLAY:
            display()
        elif choice == EXIT:    
            running = False
        else:
            print('Invalid choice') 
def print_menu():
    # TODO: print menu
    pass

def add_student():
    stid = input("Enter student id: ")
    if stid in students:
        print(f'Student id {stid} already exists')
        return
    name = input("Enter student name: ")
    gpa = float(input("Enter student gpa: "))
    students[stid] = [name, gpa]
    print(f'Student {name} added')

def edit_student():
    stid = input("Enter student id: ")
    if stid not in students:
        print(f'Student id {stid} does not exist')
        return
    name = input("Enter student name: ")
    gpa = float(input("Enter student gpa: "))
    students[stid] = [name, gpa]
    print(f'Student {name} edited')

def delete_student():
    stid = input("Enter student id: ")
    if stid not in students:
        print(f'Student id {stid} does not exist')
    else:
        del students[stid]
        print(f'Student id {stid} deleted')

def search_name(exact=True):
    name = input("Enter student name: ")
    if exact:
        found_students = [id for id in students.items() if students[id][0] == name]
    else:
        found_students = [id for id in students.items() if name in students[id][0]]
    
    if len(found_students) == 0:
        print(f'No student found')  
        return
    
    for st in found_students:
        print(f'{st[0]} {st[1][0]} {st[1][1]}')

def search():
    print('1. Search by exact name')
    print('2. Search in name')
    choice = int(input('Enter your choice: '))
    search_name(choice == EXACT)

def display():
    # TODO: display students 2 options
    pass
# Run program
main()