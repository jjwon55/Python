# 데코레이터를 이용한 getter, setter, 정의

class Person:
    
    # @property : 해당 변수를 데코레이터 기능을 사용할 수 있도록 지정
    #           - getter, setter 로 사용가능
    #           - @property 로 지정한 변수는 _변수 와 같은 형태로 사용

    @property
    def name(self):
        return self.__name


    # @변수.setter : 해당 메소드를 setter 메소드로 지정
    @name.setter
    def name(self, value):
        self.__name = value
        print('setter 메소드 호출..')

    # @변수.getter : 해당 메소드를 getter 메소드로 지정
    #               - (객체, 변수) 실행 시, 지정한 getter 메소드가 시행
    @name.getter
    def name(self):
        print('getter 메소드 호출')
        return self.__name
    
    
p = Person()

# setter 메소드를 통해 값이 지정됨(호출됨)
p.name = '김조은'       
# getter 메소드를 통해 값이 접근함(호출됨)
print('p - name : {}'.format(p.name))