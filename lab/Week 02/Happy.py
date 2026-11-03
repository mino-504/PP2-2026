#
# 생일 축하 함수
#
def say_happy_birthday(name:str) -> None:
    print("안녕하세요")
    print(name + "님의 생일을 축하합니다")
    return None

def test_happy_birthday() :
    say_happy_birthday("민호")
    say_happy_birthday("태현")
    say_happy_birthday("기범")
    say_happy_birthday("재균")
    
def test_happy_birthday2() :
    names = ["민호", "태현", "기범", "재균"]
    for name in names:
        say_happy_birthday(name)
        
def test_happy_birthday3() :
    say_happy_birthday(3.141592)
    say_happy_birthday(100)
    say_happy_birthday([1,2,3])    

if __name__ == "__main__": #메인에서 
#    test_happy_birthday()
#    test_happy_birthday2()
    test_happy_birthday3()
