import sys
import random

students = []

def input_student() :
    while True :
        temp = input("추가할 학생의 이름을 입력하세요.\n다 추가했다면 Enter 키를 누르세요.\n입력: ")
        if temp == "" :
            break
        else :
            students.append(temp)

def del_student() :
    while True :
        temp = input("삭제할 학생의 이름을 입력하세요.\n작업을 완료했다면 Enter 키를 눌러 메뉴로 돌아갑니다.\n입력: ")
        if temp == "" :
            break
        else :
            students.remove(temp)

def print_student() :
    print("학생 목록: ")
    for i in students :
        print(students)
    print("끝.")

def return_error(error) :
    print("오류가 발생했습니다. 오류 내용: \n" + error)
    sys.exit(1)

def make_team() :
    try : 
        print("옵션 선택: 1. 실력에 따라 팀 구성 / 2. 무작위로 팀 구성")
        temp = int(input("옵션을 선택하세요 :"))
        print("팀 인원 입력: ")
        temp2 = int(input("팀 인원을 입력하세요 :"))
    except ValueError as e :
        return_error(str(e))
    if temp == 1 :
        return_error("현재 개발 중인 기능입니다.")
    elif temp == 2 :
        temp3 = len(students) # 전체 학생 수
        result = students
        random.shuffle(result) # 학생 순서를 무작위로 섞기
        result = [result[result:i + temp2] for i in range(0, len(result), temp2)]
        print(result)
            

while True :
    print("메뉴 선택: 1. 학생 추가 / 2. 학생 삭제 / 3. 학생 목록 출력 / 4. 팀 짜기 / 5. 프로그램 종료")
    try : 
        temp = int(input("메뉴를 선택하세요: "))
    except ValueError as e :
        return_error(str(e))
    
    if temp == 1 :
        input_student()
    elif temp == 2 :
        del_student()
    elif temp == 3 :
        print_student()
    elif temp == 4 :
        make_team()
    elif temp == 5 :
        sys.exit(0)
    else :
        return_error("잘못된 입력입니다.")

