# 각 캐릭터는 주어진 생명력, 데미지를 가짐
# 4개의 캐릭터 중 하나를 자신의 캐릭터로 선택
# 사용자 포함 네 캐릭터들은 돌아가며 게임을 진행
    # 게임 진행 1라운드는 이름순, 2,3,4라운드는 생명순으로 진행
# 컴퓨터가 랜덤의 알파벳 대문자 10글자로 단어를 만들어 냄

# 게임은 3라운드 동안 진행됨
# 4명의 캐릭터들은 돌아가며 알파벳을 맞추어 나감
    # 이전의 나온 알파벳은 나올 수 없음
# 틀릴 때마다 생명력에서 데미지만큼 생명력이 감소
    # 생명력이 0이하가 되면 캐릭터는 사망
# 매 알파벳 선택 마다, 
    # 알파벳을 맞췄을 시, 현재까지의 단어 상태를 출력해준다.
    # 알파벳을 틀렸을 시, 감소된 HP를 출력
        # HP의 값이 0 이하가 될 경우 그대로 출력 - 게임 종료 후 "이승아 (사망)"으로 표시된다.

# 3라운드 동안 진행되며, 3라운드 종료 후 결과 출력화면으로 넘어감
    # 결과는 생명력 순, 알파벳 맞춘 순 두 가지 형태로 출력한다.
    # 내가 선택한 캐릭터는 이름 앞뒤에 * 를 출력해준다.
    # 사망자는 HP 대신 사망으로 출력한다.
    # 남은 생명력이 같은 경우 이름 순으로 출력


import string
import random

class Player:
    def __init__(self, name, hp, damage, correct_alp):
        self.name=name      # 이름
        self.hp=hp          # 생명력
        self.damage=damage  # 데미지
        self.correct_alp=0  # 알파벳 맞춘 횟수

class Game:
    def __init__(self):
        self.player=[]              # 캐릭터의 목록, start_game()에서 생성
        self.user_character=""      # 사용자가 선택한 캐릭터
        self.remain_alp=list(string.ascii_uppercase)# 남은 알파벳
        self.cur_string=["_"]*10    # 현재까지의 글자상태를 저장
        self.answer_string=""       # 랜덤 10글자 단어

    def start_game(self):
        """
        [게임 시작 전] 부분을 담당하는 함수
        캐릭터들을 초기화하고, 사용자가 플레이할 캐릭터를 선택
        랜덤 알파벳 10글자로 이루어진 answer_string을 생성
        동일 클래스의 game()에서 호출됨
        """
        self.player.append(Player("김용빈",50,20,0))
        self.player.append(Player("김규리",70,25,0))
        self.player.append(Player("이승아",80,30,0))
        self.player.append(Player("윤석현",90,35,0))
        # TODO 1-(1): 사용자로부터 캐릭터를 입력받아 user_character에 저장해주세요.
        print("당신의 캐릭터 번호를 선택해주세요 (1,2,3,4): ", end="")
        character_num=int(input())
        self.user_character=self.player[character_num-1].name
        print(f"당신의 캐릭터는 '{self.user_character}' 입니다.")
        ##### END OF TODO 1-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####

        # TODO 1-(2) : 랜덤 알파벳 10글자로 이루어진 단어를 만들어 answer_string에 저장해주세요.
        word=""
        for i in range(10):
            word+=random.choice(string.ascii_uppercase)
        self.answer_string=word
        print(self.answer_string)
        print("랜덤으로 생성된 답입니다. 플레이어는 알 수 없습니다.")
        ##### END OF TODO 1-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    def sort_data(self,i):
        """
        [게임 진행] 부분에서 게임 진행 순서를 담당하는 함수
        동일 클래스 game()에서 호출
        """

        # TODO 2 : 게임진행을 위한 data 를 재정렬해주세요.(ROUND 1 : 이름순, ROUND 2,3 : HP 높은 순)
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        if i==1:
            for i in range(4):
                self.player=sorted(self.player, key=lambda x: x.name) # 이름 순으로 정렬
        else:
            for i in range(4):
                self.player=sorted(self.player, key=lambda x: x.hp, reverse=True)
        ##### END OF TODO 2 (문제와 본 라인 사이에 코드를 작성하세요.) #####

    def play_game(self):
        """
        [게임 진행] 부분을 담당하는 함수
        동일 클래스 game()에서 호출
        """

        print(
          f"게임은 {self.player[0].name},{self.player[1].name},{self.player[2].name},{self.player[3].name} 순으로 진행됩니다.\n")

        List_answer_string=list(self.answer_string) # 랜덤 10글자 단어
        for i in range(4):

            if self.player[i].name== self.user_character:
                print("***** 내 캐릭터 *****")
            else:
                print(f"***** {i+1} 캐릭터 *****")

            print(f"이름: {self.player[i].name} (HP: {self.player[i].hp})")

            # TODO 3-(1) : 플레이어와 컴퓨터의 차례에서는 랜덤의 알파벳 한글자를 선택하게 해주세요. 
            # 단 앞에 나왔던 알파벳과 중복되면 안됩니다.
            print("선택 알파벳 : ", end="")
            if self.player[i].name==self.user_character:
                enter_Alphabet=input()
                print(enter_Alphabet)
            else:
                enter_Alphabet=random.choice(self.remain_alp) # 전체 알파벳들 중에서 랜덤으로 선택
                print(enter_Alphabet)
            ##### END OF TODO 3-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####

            # TODO 3-(2) : 정답 시, 현재까지 맞춘 단어의 상태를 출력해주세요.
			# 이 단계에서 플레이어 별 점수 집계도 처리해주셔야 합니다.
            #  print("***** 맞았습니다 ᵔεᵔ  *****")
            if enter_Alphabet in List_answer_string:
                print("***** 맞았습니다 ᵔεᵔ  *****")
                self.player[i].correct_alp+=1 # 맞춘 횟수 1 증가
                self.cur_string[List_answer_string.index(enter_Alphabet)]=enter_Alphabet
                # self.cur_string[List_answer_string에서 enter_Alphabet의 인덱스 값]=enter_Alphabet 할당
                List_answer_string[List_answer_string.index(enter_Alphabet)]="0" # List_answer_string의 원소를 "0"으로 바꿈
                self.answer_string="".join(List_answer_string) # self.answer_string 갱신
                print(" ".join(self.cur_string))
            ##### END OF TODO 3-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####

            # TODO 3-(3) : 오답 시, 생명력을 데미지만큼 감소시켜주고 이를 출력해주세요.
            #  print("***** 틀렸습니다 (ﾟ⊿ﾟ)  ******")
            else:
                print("***** 틀렸습니다 (ﾟ⊿ﾟ)  ******")
                self.player[i].hp-=self.player[i].damage # 생명력 감소
                print(f"{self.player[i].name}님은 틀렸기 때문에 HP가 {self.player[i].hp} 남았습니다.")
            print()
            ##### END OF TODO 3-(3)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    def game_result(self):
        """
        [게임 종료 후] 부분을 담당하는 함수
        게임의 결과를 생명력순, 알파벳 맞춘 횟수 순 두가지의 경우로 출력
        동일 클래스 game()에서 호출
        """

        print("\n\n******************* 게임이 끝났습니다 *******************")

        # TODO 4-(1) : 생명력 순으로 결과값을 출력해주세요.
        # 내가 선택한 캐릭터 이름 앞뒤에는 *을 붙여주세요.
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        print("=============================")
        print("     게임 순위 - 생명력")
        print("=============================")
        
        for i in range(4):
            self.player=sorted(self.player, key=lambda x: x.hp, reverse=True) # 생명력 순으로 정렬
        
        for i in range(4):
            if self.player[i].name==self.user_character:
                if self.player[i].hp<=0:
                    print(f"{i+1}등: *{self.player[i].name}* (사망)")
                else:
                    print(f"{i+1}등: *{self.player[i].name}* (HP: {self.player[i].hp})")
            else:
                if self.player[i].hp<=0:
                    print(f"{i+1}등: {self.player[i].name} (사망)")
                else:
                    print(f"{i+1}등: {self.player[i].name} (HP: {self.player[i].hp})")
        ##### END OF TODO 4-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####

        # TODO 4-(2) : 알파벳 맞춘 횟수 순으로 결과값을 출력해주세요.
        # 내가 선택한 캐릭터 이름 앞뒤에는 *을 붙여주세요.
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        print("=============================")
        print(" 게임 순위 - 알파벳 맞춘 횟수")
        print("=============================")
        
        for i in range(4):
            self.player=sorted(self.player, key=lambda x: x.correct_alp, reverse=True)

        for i in range(4):
            if self.player[i].name==self.user_character:
                print(f"{i+1}등: *{self.player[i].name}* {self.player[i].correct_alp}회")
            else:
                print(f"{i+1}등: {self.player[i].name} {self.player[i].correct_alp}회")
        ##### END OF TODO 4-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    def game(self):
        """
        게임 운영을 위한 함수
        별도 코드 작성 필요 없음
        """

        self.start_game()

        print("******************* 게임 시작 *******************\n")

        for i in range(1,4):
            print("===========================")
            print(f"     ROUND {i} - START")
            print("===========================")

            self.sort_data(i)
            self.play_game()

            print("===========================")
            print(f"     ROUND {i} - END")
            print("===========================")

        self.game_result()

if __name__=='__main__':
    game=Game()
    game.game()
