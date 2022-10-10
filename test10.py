#핸드폰 번호 가리기
#input 번호 받아서 010-2222-2222
#뒷 4자리만 살리고 ***-****-2222
#02-8888-8888 -> **-****-8888

def solution(phone_number):
    answer = ''
    for i in range(0, len(phone_number)):
        if i < len(phone_number)-4 :
            if phone_number[i] == "-":
                answer += "-"
            else: 
                answer += "*"
        else :
            answer += phone_number[i]
    return answer

print(solution("01033334444"))
print(solution("0277778888"))


# 파일 입출력
# 상대 경로 (내 위치에서 가고픈 곳으로 가고 싶음)
# . : 현재위치 c/test
# .. c
# . 현재위치 c/test/test1
# ../test12.py

#절대 경로
#C:\test\test-python

# f = open("./test.txt", 'w')
# f.write("hi1")
# f.write("\n")
# f.write("\n")
# f.write("\tbye1")
# f.close()

# f = open("./test.txt", 'r')
# lines = f. readlines()
# for line in lines :
#     print(line)
# f.close()

# f = open("./test.txt", 'a')
# f.write("""
#         asdfasdfasdf""")
# f.close()


#git add.
#git commit

#내일 업데이트, class
# def open(filename, type) :
        #filename 존재 유무
        #if write : "w" ; 쓰기모드
        #elif read : "r" ; 읽기모드

# fr = open("./12345.txt", 'r')
# lines = fr.readlines()  #["빅데이터", ]
# for line in lines :
#         print(lines)
# fr.close()

# fw = open("./12345.txt", 'w')
# for line in lines :
#         if line == "AI" :
#                 fw.write("ML")
#         elif line == "py" :
#                 fw.write("python")
#         else :
#                 fw.write(line)
# fw.close()


# fr = open("./8888.txt", 'r', encoding="UTF-8")
# lines = fr.readlines()  #["빅데이터", ]
# for line in lines :
#         print(lines)
# fr.close()

# fw = open("./8888.txt", 'w', encoding="UTF-8")
# for line in lines :
#         line = line.strip()
#         if line == "한글" :
#                 fw.write("ML")
#         elif line == "쓰기" :
#                 fw.write("글쓰기")
#         else :
#                 fw.write(f"{line}")
#         fw.write("\n")

# fw.close()



#문제
# fr = open('./8888.txt', 'r', encoding= "UTF-8")
# lines = fr.readlines()
# fr.close()


# fw = open('./8888.txt', 'w', encoding="UTF-8")
# for line in lines : 
#         text_update = input(f"바꿀 문장(취소는 c):c\n 전 문장: {line}")
#         if text_update == "c" :
#                 fw.write(line.strip())
#         else: 
#                 fw.write(text_update)
#         fw.write("\n")
# fw.close()

# a=input("hi")
# print(a)

# ft = open('./8888.txt', 'r', encoding="UTF-8")
# lines = ft.readlines()
# ft.close()

# fw = open('./8888.txt', 'w',encoding= "UTF-8")
# for line in lines:
#         update_text = input(f"전 문장 : {line}\n 바꿀 문장(취소는 c): \t")
#         if update_text == 'c' :
#                 fw.write(line.strip())
#         else :
#                 fw.write(update_text)
#         fw.write("\n")
# fw.close()