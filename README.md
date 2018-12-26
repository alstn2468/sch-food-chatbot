SCH Food Chatbot
========================
순천향대학교 학식알리미<br/>
----------------------


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Generic badge](https://img.shields.io/badge/No-Update-red.svg)](https://shields.io/)

### 이 프로젝트는 더 이상 업데이트 되지 않습니다.<br/>
### 곧 다른 레파지토리가 업데이트 될 예정입니다.


##  [김민수](https://github.com/alstn2468)
## [ [Facebook](https://www.facebook.com/profile.php?id=100003769223078) ] [ [Github](https://github.com/alstn2468) ] [ [LinkedIn](https://www.linkedin.com/in/minsu-kim-336289160/) ] [ [Blog](https://alstn2468.github.io/) ]<br/>


## 개요
Python과 Django 웹 프레임워크를 사용하여 제작한 자동 응답형 카카오톡 챗봇입니다.<br/>
[(순천향대학교 학식알리미)](http://pf.kakao.com/_xggCxixl)에서 친구 추가가 가능합니다.<br/>
순천향대학교 학식알리미는 다음 [문서](https://github.com/plusfriend/auto_reply)를 기반으로 제작되었습니다.<br/>


## 기술


### 언어
- Python(3.6.5)


### 프레임워크
- Django(2.0.5)


### 모듈
- certifi(2018.1.18)<br/>
- chardet(3.0.4)<br/>
- dj-database-url(0.5.0)<br/>
- dj-static(0.0.6)<br/>
- Django(2.0.5)<br/>
- gunicorn(19.8.1)<br/>
- idna(2.6)<br/>
- lxml(4.2.1)<br/>
- psycopg2(2.7.4)<br/>
- pytz(2018.4)<br/>
- requests(2.18.4)<br/>
- static3(0.7.0)<br/>
- urllib3(1.22)<br/>
- virtualenv(15.2.0)<br/>
- whitenoise(3.3.1)<br/>
- beautifulsoup4(4.6.0)<br/>
- bs4(0.0.1)<br/>
- html-sanitizer(1.4.0)

### 서버
- heroku


## 기능

### 향설1 생활관
- 월 ~ 토 요일별 `당일` 학식 메뉴 확인 가능<br/>
- 조식, 중식, 석식 학번에 확인 가능<br/>
- 학식이 없는 경우도 표시<br/>


### 향설2 생활관
- 향설2 생활관 학식 `메뉴` 확인 가능<br/>
- 일주일 동안 같은 메뉴


### 향설3 생활관
- 요일별 `당일` 학식 메뉴 확인 가능<br/>
- 컵밥, 도시락, 덮밥, 스페셜메뉴, 돈까스, 라면, 부대라면 세부 메뉴 한번에 확인 가능<br/>
- 학식이 없는 경우도 표시<br/>


### 학생 회관
- 월 ~ 금 요일별 `당일` 학식 메뉴 확인 가능<br/>
- 조식 메뉴 확인 가능<br/>
- 중식/석식 메뉴는 동일<br/>
- 중식/석식 세부 메뉴 확인 가능<br/>
- 샐러드바 메뉴 확인 가능<br/>
- 학식이 없는 경우도 표시<br/>


### 교직원 식당
- 월 ~ 금 요일별 `당일` 학식 메뉴 확인 가능<br/>
- 중식 메뉴 확인 가능<br/>
- 한정 메뉴 확인 가능<br/>


### 식당 별 이용 가능 시간 확인 가능
- 식당별 조식, 중식, 석식 `이용 가능 시간` 확인 가능<br/>


### 종강일 확인 가능
- `오늘` 날짜 확인 가능<br/>
- `종강일` 확인 가능<br/>
- 오늘로부터 `종강`까지 며칠이 남았는지 확인 가능<br/>
- 종강일은 사람마다 `다를 수` 있습니다.<br/>
- 순천향대학교 학식 알리미에서는 시험이 끝나고 `다음 주`를 기준으로 합니다.<br/>

### 학사일정 확인 가능
- `이번 달` 학사 일정 확인 가능<br/>
- 학사 일정 요일, 세부 내용 확인 가능<br/>


### 개발자 정보 확인
- 개발자의 정보 확인 가능<br/>
- 문제가 생길시 연락할 수 있는 카카오톡 아이디 명시<br/>
- 학과, 학번, 이름 확인 가능<br/>


## 버전
2018/05/12<br/>
- Version [(1.0.0)](https://github.com/alstn2468/SCH_Food_ChatBot/commit/a90e974c8cbcb5274cc9d3174393c5dadf446160) Released<br/>

2018/05/14<br/>
- Version [(2.0.0)](https://github.com/alstn2468/SCH_Food_ChatBot/commit/0345f08a672d499816ca8cf03f60ab140992656c)<br/>
- 학사 일정 확인 기능 추가 완료

2018/05/14<br/>
- Version [(2.1.0)](https://github.com/alstn2468/SCH_Food_ChatBot/commit/ce419d7c03e235c8cc61a78d2b26d75e1f364079)<br/>
- 버튼 메뉴 세분화 완료

2018/05/14<br/>
- Version [(2.2.0)](https://github.com/alstn2468/SCH_Food_ChatBot/commit/22a2d0cd5613c5398dfb8c6656467389f1acbfbb)<br/>
- 학교 Wi-Fi 기능 추가 완료
- 소스 코드 모듈화 완료

2018/05/16<br/>
- Version [(2.3.0)](https://github.com/alstn2468/SCH_Food_ChatBot/commit/a6428acc74a6561d29b65ae4e5cea82a41aee978)<br/>
- 식당 이용 시간 확인 기능 추가 완료
- 소스 코드 모듈화 완료

2018/05/20<br/>
- Version [(2.3.1)](https://github.com/alstn2468/SCH_Food_ChatBot/commit/a924f4cb603ecaa1378fb286e7c7ab1b95852a2b)<br/>
- 학식 메뉴 띄어쓰기 적용
