# break
# 현재 속함 반복문을 벗어나는 키워드

# 무한 반복
# : 무조건 계속 반복한는 반복문
# * 반드시, 종료조건을 넣어주어야 한다.

while True:
    academy = input('우리 학원 이름은')
    # 종료조건
    if academy == '더조은':
        print('정답입니다')
        break
    else:
        print('틀렸습니다.')