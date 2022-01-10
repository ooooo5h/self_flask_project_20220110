from flask import Flask
from flask.templating import render_template

def create_app():
    # 플라스크 서버를 변수에 담았음
    app = Flask(__name__)
    
    # 서버에 대한 세팅 진행하는 부분
    @app.route("/")
    def home():
        return "<h1>나혼자 도전</h1>"
    
    
    @app.route("/test")
    def test():
        return "여긴 테스트"
    
    
    @app.route("/web")
    def web_test():
        return render_template('web_test.html')   # templates폴더 내부의 파일을 불러내는 코드
    
    
    @app.route("/json")
    def json_test():
        
        # JSON양식 => "이름표" : 실제값 의 조합(딕셔너리를 이용하면 작업이 편함)
        test_dict = {}
        test_dict['menu'] = '빵',
        test_dict['price'] = 3500,
        test_dict['store_name'] = '맛있는 빵집',
        test_dict['is_open'] = True
    
    # 이 서버를 사용하도록 결과로 리턴하는 부분
    return app