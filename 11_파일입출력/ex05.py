# 파일 복사
''' 
    * 파일 복사 과정
    원본 파일 -> 객체 -> 복사본
    (읽기,rb)          (쓰기,wb)
    
    * with
    : 파일 입출력 시, 자동으로 close()함수를 호출한다.
    
    with open(파일경로, 모드) as 파일객체:
        처리코드
        처리코드
        처리코드
'''

import os

path = os.path.dirname(__file__) + os.path.sep + 'file'
origin = path + os.path.sep + input('원본 파일명 : ')
copy = path + os.path.sep + input('사본 파일명 : ')

buffer_size = 1024      # 버퍼 용량 : 1024Byte(1KB)

with open(origin, 'rb') as source:
    with open(copy, 'wb') as copyfile:
        while True:
            # 원본 파일을 버퍼용량(1025 = 1KB)만큼 읽어와서 buffer에 저장
            buffer = source.read(buffer_size)
            if not buffer:
                break
            # 1KB 씩 파일 데이터 출력
            copyfile.write(buffer)

print(copy)
print('파일이 복사되었습니다.')