import json
import random
import threading
import os


class Quiz:
    def __init__(self, question, choices, answer, difficulty):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.difficulty = difficulty


class QuizGame:
    def __init__(self):
        self.quizzes = self.load_quizzes()
        self.score = 0
        self.time_limit = 10
        self.best_score = self.load_best_score()
        self.state = self.load_state()          # ✅ state 추가

    def load_best_score(self):
        try:
            with open("best_score.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                return data["best_score"]
        except:
            return 0

    def save_best_score(self):
        with open("best_score.json", "w", encoding="utf-8") as f:
            json.dump({"best_score": self.best_score}, f, ensure_ascii=False, indent=4)

    # ✅ state.json 읽기 - 프로그램 시작 시 호출
    def load_state(self):
        default = {
            "last_difficulty": "전체",
            "last_score": 0,
            "play_count": 0
        }
        try:
            with open("state.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            required = ["last_difficulty", "last_score", "play_count"]
            for key in required:
                if key not in data:
                    raise KeyError(f"필드 누락: {key}")

            return data

        except FileNotFoundError:
            self.save_state(default)
            return default

        except (json.JSONDecodeError, KeyError) as e:
            print(f"⚠️  state.json 손상 감지: {e}")
            self._backup_and_reset_state(default)
            return default

    # ✅ state.json 쓰기 - 게임 종료 시 호출
    def save_state(self, data=None):
        if data is None:
            data = self.state
        with open("state.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # ✅ 손상 시 백업 + 초기화
    def _backup_and_reset_state(self, default):
        if os.path.exists("state.json"):
            os.rename("state.json", "state_backup.json")
            print("📦 손상된 파일을 state_backup.json으로 백업했습니다.")
        self.save_state(default)
        print("🔄 state.json을 초기화했습니다.")

    # ✅ #15 수정 - 예외처리 추가
    def load_quizzes(self):
        try:
            with open("quizzes.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            quizzes = []
            for item in data:
                quiz = Quiz(
                    item["question"],
                    item["choices"],
                    item["answer"],
                    item["difficulty"]
                )
                quizzes.append(quiz)

            return quizzes

        except FileNotFoundError:
            print("⚠️  quizzes.json 파일이 없습니다. 빈 목록으로 시작합니다.")
            return []
        except json.JSONDecodeError:
            print("⚠️  quizzes.json 형식이 올바르지 않습니다. 빈 목록으로 시작합니다.")
            return []
        except KeyError as e:
            print(f"⚠️  퀴즈 데이터에 필드가 없습니다: {e}")
            return []

    def save_quizzes(self):
        data = []
        for quiz in self.quizzes:
            item = {
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer,
                "difficulty": quiz.difficulty
            }
            data.append(item)

        with open("quizzes.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # ✅ #2 수정 - 입력값 검증 추가
    def add_quiz(self):
        print("\n=== 퀴즈 추가 ===")

        question = input("문제를 입력하세요: ").strip()
        if not question:
            print("❌ 문제를 입력해주세요!")
            return

        choices = []
        for i in range(1, 5):
            choice = input(f"{i}번 보기를 입력하세요: ").strip()
            if not choice:
                print(f"❌ {i}번 보기를 입력해주세요!")
                return
            choices.append(f"{i}. {choice}")

        answer = input("정답 번호를 입력하세요 (1~4): ").strip()
        if answer not in ["1", "2", "3", "4"]:
            print("❌ 정답 번호는 1~4 사이 숫자여야 합니다!")
            return

        print("난이도를 선택하세요: 쉬움 / 보통 / 어려움")
        difficulty = input("난이도: ").strip()
        if difficulty not in ["쉬움", "보통", "어려움"]:
            print("❌ 올바른 난이도를 입력해주세요! (쉬움/보통/어려움)")
            return

        new_quiz = Quiz(question, choices, answer, difficulty)
        self.quizzes.append(new_quiz)
        self.save_quizzes()
        print("✅ 퀴즈가 추가되었습니다!")

    def delete_quiz(self):
        print("\n=== 퀴즈 삭제 ===")

        for i, quiz in enumerate(self.quizzes):
            print(f"{i + 1}. [{quiz.difficulty}] {quiz.question}")

        number = input("\n삭제할 퀴즈 번호를 입력하세요: ")

        if not number.isdigit():
            print("❌ 숫자를 입력해주세요!")
            return

        index = int(number) - 1

        if index < 0 or index >= len(self.quizzes):
            print("❌ 없는 번호입니다!")
            return

        deleted = self.quizzes[index].question
        del self.quizzes[index]
        self.save_quizzes()
        print(f"✅ '{deleted}' 퀴즈가 삭제되었습니다!")

    def select_difficulty(self):
        print("\n=== 난이도 선택 ===")
        print("1. 쉬움")
        print("2. 보통")
        print("3. 어려움")
        print("4. 전체")

        choice = input("난이도를 선택하세요: ")

        if choice == "1":
            return "쉬움"
        elif choice == "2":
            return "보통"
        elif choice == "3":
            return "어려움"
        elif choice == "4":
            return "전체"
        else:
            print("❌ 잘못된 입력! 전체 난이도로 진행합니다.")
            return "전체"

    def show_menu(self):
        print("\n=== 파이썬 퀴즈 게임 ===")
        print(f"🏆 현재 최고 점수: {self.best_score}점")
        print(f"📈 총 플레이 횟수: {self.state['play_count']}회")      # ✅ 추가
        print(f"🎯 마지막 점수: {self.state['last_score']}점")         # ✅ 추가
        print("1. 퀴즈 시작")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 삭제")
        print("4. 종료")
        return input("번호를 선택하세요: ")

    def input_with_timer(self):
        answer = [None]

        def get_input():
            answer[0] = input("정답 번호를 입력하세요: ")

        thread = threading.Thread(target=get_input)
        thread.daemon = True
        thread.start()
        thread.join(timeout=self.time_limit)

        return answer[0]

    def update_best_score(self, total):
        current_score = int((self.score / total) * 100)

        print(f"\n📊 이번 점수: {current_score}점")
        print(f"🏆 최고 점수: {self.best_score}점")

        if current_score > self.best_score:
            self.best_score = current_score
            self.save_best_score()
            print("🎉 새로운 최고 점수 달성!")
        else:
            print("💪 최고 점수에 도전해보세요!")

    def run(self):
        self.score = 0

        difficulty = self.select_difficulty()

        if difficulty == "전체":
            filtered = self.quizzes
        else:
            filtered = [q for q in self.quizzes if q.difficulty == difficulty]

        if len(filtered) == 0:
            print(f"❌ '{difficulty}' 난이도 퀴즈가 없습니다!")
            return

        random_quizzes = random.sample(filtered, len(filtered))

        for i, quiz in enumerate(random_quizzes):
            print(f"\nQ{i + 1}. [{quiz.difficulty}] {quiz.question}")
            for choice in quiz.choices:
                print(choice)
            print(f"⏱️  제한 시간: {self.time_limit}초")

            answer = self.input_with_timer()

            if answer is None:
                print(f"\n⏰ 시간 초과! 정답은 {quiz.answer}번이었습니다.")
            elif answer == quiz.answer:
                print("✅ 정답입니다!")
                self.score += 1
            else:
                print(f"❌ 틀렸습니다! 정답은 {quiz.answer}번입니다.")

        total = len(filtered)
        print(f"\n=== 결과 ===")
        print(f"총 {total}문제 중 {self.score}개 정답!")

        if self.score == total:
            print("🏆 완벽해요! 천재인가요?")
        elif self.score >= total * 0.8:
            print("🥇 훌륭해요! 거의 다 맞혔어요!")
        elif self.score >= total * 0.6:
            print("🥈 잘 했어요! 조금만 더 공부해봐요!")
        else:
            print("🥉 아쉬워요! 다시 도전해봐요!")

        self.update_best_score(total)

        # ✅ 게임 종료 시 state.json 저장
        self.state["last_difficulty"] = difficulty
        self.state["last_score"] = int((self.score / total) * 100)
        self.state["play_count"] = self.state.get("play_count", 0) + 1
        self.save_state()

    # ✅ #11 수정 - Ctrl+C / EOFError 예외처리 추가
    def start(self):
        try:
            while True:
                choice = self.show_menu()

                if choice == "1":
                    self.run()
                elif choice == "2":
                    self.add_quiz()
                elif choice == "3":
                    self.delete_quiz()
                elif choice == "4":
                    print("게임을 종료합니다. 안녕히 가세요! 👋")
                    break
                else:
                    print("1, 2, 3, 4 중에 입력해주세요!")

        except KeyboardInterrupt:
            print("\n\n게임을 종료합니다. 안녕히 가세요! 👋")
        except EOFError:
            print("\n\n입력이 종료되었습니다. 게임을 끝냅니다. 👋")


game = QuizGame()
game.start()