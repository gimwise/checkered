# 실행 방법 설명

* 영남대학교 컴퓨터공학과 21913662 김지혜

### 파이썬
* 기본적으로 해당 프로젝트는 파이썬3가 있어야 실행됩니다. 
  * 없다면 설치해주세요.
  * https://www.python.org/downloads/
  
* 가상환경을 프로젝트 내부에 추가해두었으므로 가상환경을 먼저 실행하도록 하겠습니다.
  * ```source env/bin/activate```

* 가상환경이 실행되지 않는 경우, pip install로 직접 모듈을 설치합니다.
  * ```pip install -r requirements.txt```

* 가상환경 실행 또는 모듈 설치가 완료되면 프로젝트의 DB 모델을 불러와야합니다.
  * ```python manage.py makemigrations```
  * ```python manage.py migrate```

* 장고를 실행합니다.
  * ```python manage.py runserver```

* http://127.0.0.1:8000/ 로 접속하시면 프로젝트 결과물을 보실 수 있습니다.

* 관리자 계정 
  * 아이디 : admin
  * 비밀번호 : admin1234*
* 일반 사용자 테스트 계정
  * 아이디 : test01
  * 비밀번호 : admin1234*
* 브랜드 관리자 테스트 계정
  * 아이디 : brand1
  * 비밀번호 : admin1234*