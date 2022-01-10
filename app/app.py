from flask import Flask

def create_app():
    # 플라스크 서버를 변수에 담았음
    app = Flask(__name__)
    
    # 서버에 대한 세팅 진행하는 부분
    @app.route("/")
    def test():
        return "<h1>나혼자 도전</h1>"
    
    # 이 서버를 사용하도록 결과로 리턴하는 부분
    return app