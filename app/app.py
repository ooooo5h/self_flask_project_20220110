from flask import Flask, request
from flask.templating import render_template

from user.user import user_test, login_test

def create_app():
    # 플라스크 서버를 변수에 담았음
    app = Flask(__name__)
    
    # 서버에 대한 세팅 진행하는 부분
    @app.route("/")
    def home():
        return "<h1>나혼자 도전</h1>"
    
    
    @app.route('/module_test')
    def module_test():
        return user_test()
        # 다른 모듈의 함수 실행결과를 내보내자
        # 로직은 다른 모듈에서만 작성하고
        # main.py에서는 불러내기만 실행할 예정
        
        
    @app.route('/login_test')
    def login_01():
        
        # 외부에서 보내주는 파라미터를 받아서 확인해보자
        params = request.args.to_dict()
        print(f'전달받은 파라미터 : {params}')
        
        id = params['login_id']
        pw = params['pw']
        
        return login_test(id, pw)

    # 이 서버를 사용하도록 결과로 리턴하는 부분
    return app