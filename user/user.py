# 사용자 정보에 관련된 기능들을 모아두는 모듈
# app.py에서 이 함수들을 끌어다 사용


def user_test():
    return{
        'name' : '전은형',
        'birth_year' : 1991,
    }
    
    
def login_test(id, pw):
    
    if id == 'admin' and pw =='qwer':
        return{
            'code' : 200,
            'message' : 'login OK',
        }
    else :
        return {
            'code' : 400,
            'message' : 'fail',
        }