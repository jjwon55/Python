# 예외 정보
# as 키워드로 예외 정보를 확인 할 수 있다
''' 
    except 예외 클래스 as 변수명
    
    ex)
        except XXXError as err:
            # err.args : 예외 정보를 가진 변수
            #           -err.args[0] : 에러 번호
            #           -err.args[1] : 에러 메시지
            #           : __str__  메소드에 의해 예외정보가 출력됨

        
'''

try:
    # 예외 발생 가능성이 있는 문장
    file = open('존재하지않는파일.txt')
    line = file.readline()
    print(line)
except OSError as err:
    # OSError 예외 처리 문장
    print('예외 정보 : ', err.args)
    print('예외 정보 : ', err)
except:
    # OSError 예외 이외의 처리 문장
    print('알 수 없는 예외 발생...')
else:
    # 예외 발생하지 않았을 때 실행할 문장
    print('정상적으로 파일을 읽어왔습니다.')
finally:
    # 예외 발생과 부관하게 샐행하는 문장
    print("파일 입력을 시도하였습니다.")
