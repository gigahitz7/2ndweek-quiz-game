# 🐍 파이썬 퀴즈 게임

파이썬 기초 지식을 테스트하는 퀴즈 게임입니다!  
타이머, 난이도 선택, 최고 점수 기록 기능을 포함합니다.

---

## 📸 실행 화면
=== 파이썬 퀴즈 게임 ===
🏆 현재 최고 점수: 100점
📈 총 플레이 횟수: 1회
🎯 마지막 점수: 100점

퀴즈 시작
퀴즈 추가
퀴즈 삭제
종료
code
📋 복사

---

## ✨ 주요 기능

| 기능 | 설명 |
|------|------|
| 🎯 퀴즈 풀기 | 랜덤 순서로 퀴즈 출제 |
| ⏱️ 타이머 | 문제당 10초 제한 |
| 🎚️ 난이도 선택 | 쉬움 / 보통 / 어려움 / 전체 |
| ➕ 퀴즈 추가 | 나만의 퀴즈 추가 가능 |
| 🗑️ 퀴즈 삭제 | 원하는 퀴즈 삭제 가능 |
| 🏆 최고 점수 | 최고 점수 자동 저장 및 갱신 |
| 📊 게임 통계 | 총 플레이 횟수 & 마지막 점수 자동 저장 |

---

## 📁 파일 구조
2ndweek-quiz-game/
│
├── main.py # 메인 실행 파일
├── quizzes.json # 퀴즈 데이터 저장
├── best_score.json # 최고 점수 저장
├── state.json # 플레이 횟수 & 마지막 점수 저장
└── README.md # 프로젝트 설명서

code
📋 복사

---

## ⚙️ 설치 및 실행 방법

### 1️⃣ 저장소 클론

```bash
git clone https://github.com/gigahitz7/2ndweek-quiz-game.git
cd 2ndweek-quiz-game
2️⃣ 실행
bash
📋 복사
python main.py
✅ 별도 라이브러리 설치 없이 바로 실행 가능합니다!

🎮 게임 방법
code
📋 복사
1. 게임 실행
        ↓
2. 난이도 선택 (쉬움 / 보통 / 어려움 / 전체)
        ↓
3. 문제 풀기 (10초 안에 번호 입력!)
        ↓
4. 결과 확인 & 최고 점수 갱신
🏅 점수 기준
점수	결과 메시지
100점	🏆 완벽해요! 천재인가요?
80점 이상	🥇 훌륭해요! 거의 다 맞혔어요!
60점 이상	🥈 잘 했어요! 조금만 더 공부해봐요!
60점 미만	🥉 아쉬워요! 다시 도전해봐요!
🏗️ 클래스 구조
클래스	주요 책임
Quiz	퀴즈 1개의 데이터(문제·보기·정답·난이도)를 저장하고 관리
QuizGame	메뉴 출력, 퀴즈 실행, 파일 저장/로드, 점수 계산 등 게임 전체 흐름 제어
Quiz 클래스
퀴즈 1개를 객체로 표현
속성: question(문제), options(보기), answer(정답), difficulty(난이도)
QuizGame 클래스
게임 전체를 관리하는 컨트롤러 역할
주요 메서드:
메서드	역할
run()	메인 메뉴 루프 실행
start_quiz()	퀴즈 출제 및 채점
add_quiz()	새 퀴즈 추가
delete_quiz()	퀴즈 삭제
save_quizzes()	quizzes.json 저장
load_quizzes()	quizzes.json 로드
save_best_score()	best_score.json 저장
save_state()	플레이 횟수 & 마지막 점수를 state.json 저장
load_state()	state.json 로드하여 게임 시작 시 통계 복원
🔀 로직 분리 기준
이 프로젝트는 역할에 따라 코드를 3가지로 분리했습니다.

역할	담당	설명
입력 검증	QuizGame 메서드 내부	사용자 입력이 숫자인지, 유효 범위인지 확인
데이터 입출력	save_quizzes() load_quizzes() save_best_score() save_state() load_state()	JSON 파일 읽기/쓰기만 담당
게임 로직	start_quiz() add_quiz() delete_quiz()	퀴즈 진행·채점·추가·삭제 처리
분리한 이유
입력 검증과 데이터 저장을 분리하면 → 저장 방식이 바뀌어도 검증 코드를 수정할 필요 없음
게임 로직을 별도 메서드로 분리하면 → 기능 추가 시 다른 기능에 영향 없이 수정 가능
🛠️ 사용 기술
Python 3

모듈	용도
json	퀴즈·점수·게임 통계 데이터 저장
random	퀴즈 랜덤 출제
threading	타이머 기능 구현
💾 데이터 저장 구조
게임 데이터는 3개의 JSON 파일로 분리하여 저장합니다.

파일	저장 내용	예시
quizzes.json	전체 퀴즈 목록	[{"question": "...", "options": [...], "answer": 1, "difficulty": "쉬움"}]
best_score.json	최고 점수	{"best_score": 100}
state.json	플레이 횟수 & 마지막 점수	{"play_count": 3, "last_score": 80}
💡 배운 점
클래스(class)를 활용한 객체지향 프로그래밍
JSON 파일로 데이터 저장 및 불러오기
threading을 활용한 타이머 구현
random.sample로 랜덤 출제 구현
게임 상태(플레이 횟수·마지막 점수)를 파일로 영속 저장하는 방법
🤔 객체지향 프로그래밍을 선택한 이유
절차형 vs 객체지향 비교
구분	절차형 방식	객체지향 방식 (채택)
퀴즈 데이터 관리	딕셔너리·리스트로 관리	Quiz 클래스 객체로 관리
기능 추가 시	전체 코드 영향 가능성 있음	해당 메서드만 수정
코드 가독성	기능이 늘수록 복잡해짐	역할별로 묶여 있어 읽기 쉬움
선택 이유
퀴즈 1개를 Quiz 객체로 표현하면 → 문제·보기·정답·난이도를 하나로 묶어 관리 가능
QuizGame 클래스로 게임 전체를 묶으면 → 기능이 늘어나도 역할별로 정리되어 유지보수 쉬움
나중에 퀴즈 종류가 늘어날 경우 → Quiz 클래스를 상속해서 확장 가능
🔧 트러블슈팅
한글이 깨져서 출력되는 문제
증상

code
📋 복사
?????? ???? 출력됨
원인

Python 파일의 인코딩이 UTF-8이 아닌 경우
Windows 터미널의 기본 인코딩이 CP949(EUC-KR)로 설정된 경우
해결 방법

방법 1 - main.py 상단에 인코딩 선언 추가

python
📋 복사
# -*- coding: utf-8 -*-
방법 2 - 터미널에서 인코딩 변경

bash
📋 복사
chcp 65001
방법 3 - VSCode 우측 하단 인코딩을 UTF-8로 변경

code
📋 복사
VSCode 우측 하단 → UTF-8 클릭 → Save with Encoding → UTF-8 선택
📝 커밋 메시지 규칙
이 프로젝트에서 사용한 커밋 메시지 형식입니다.

태그	의미	예시
feat	새 기능 추가	feat: 타이머 기능 추가
fix	버그 수정	fix: 한글 깨짐 문제 수정
docs	문서 수정	docs: README 클래스 설명 추가
refactor	코드 구조 개선	refactor: Quiz 클래스 분리
chore	기타 작업	chore: .gitignore 추가
작성 예시

code
📋 복사
feat: 난이도 선택 기능 추가
fix: 타이머 종료 후 입력 오류 수정
docs: README 트러블슈팅 섹션 추가
👨‍💻 개발자
이름: 진호영
GitHub: https://github.com/gigahitz7/2ndweek-quiz-game
개발 기간: 2025년 11월
⭐ 재미있었다면 Star를 눌러주세요! ⭐