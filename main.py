from app import create_app

# 플라스크 라이브러리를 구동시켜주는 역할
# 나중에는 라이브서버(운영)과 개발용서버를 구분해서 돌려야할 필요가 있다
# 관련 세팅들을 쉽게 관리할 수 있도록 도와주는 역할이 main.py

app = create_app()

# 다른 모든 컴퓨터에서도 접속할 수 있게 허용해주자고 0.0.0.0으로 주소를 설정했다고 했는데 이게 뭔말인지 아직 잘 이해못함
app.run(host='0.0.0.0')