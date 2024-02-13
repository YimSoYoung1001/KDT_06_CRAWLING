# [ Player 클래스 ]
# 자신이 가지고 있는 카드 관리 (2개의 리스트 가짐 : holding_card_list, open_card_list)
# 두 장의 동일한 카드를 제거하는 기능 (번호가 동일한 경우, holding_card_list에서 open_card_list로 이동 => 테이블에 공개하는 기능)


class Player:
    def __init__(self, name):
        self.name = name
        self.holding_card_list = list()
        self.open_card_list = list()

    def add_card_list(self, card_list):
        self.holding_card_list = card_list

    def display_two_card_lists(self):
        print('=' * 50)
        print(f"[{self.name}] Open card list: {len(self.open_card_list)}")
        for card in self.open_card_list:
            print(card, end=' ')
        print()
        print(f"[{self.name}] Holding card list: {len(self.holding_card_list)}")
        for card in self.holding_card_list:
            print(card, end=' ')
        print()
        print()

    def check_one_pair_card(self):
        print('='*50)
        print(f"[{self.name}: 숫자가 같은 한쌍의 카드 검사]")
        length = len(self.holding_card_list)

        for i in range(length-1):
            one_card = self.holding_card_list[i]
            for k in range(i+1, length):
                second_card = self.holding_card_list[k]

                #중복카드라고 판단되면 open_card_list에 들어감
                if one_card.number == second_card.number:
                    if one_card not in self.open_card_list:
                        self.open_card_list.append(one_card)
                    if second_card not in self.open_card_list:
                        self.open_card_list.append(second_card)

        #중복카드가 모두 open_card_list에 들어갔으니 그 카드들을 holding_card_list에서 제거해야함
        for i in range(10):           #이렇게 여러번 돌리니 open + holding의 개수가 맞음 (이유는 모르겠음)
            for card in self.holding_card_list:
                if card in self.open_card_list:
                    #print('중복카드 존재 =', card)
                    self.holding_card_list.remove(card)









# ----------------------------------------------------------------------------------------------------------------
# ETC (시행착오)
# ----------------------------------------------------------------------------------------------------------------

    """
    # out of range 에러 발생
    
    def check_one_pair_card(self):
        print('='*50)
        print(f"[{self.name}: 숫자가 같은 한쌍의 카드 검사]")
        length = len(self.holding_card_list)

        for i in range(length-1):
            one_card = self.holding_card_list[i]

            for k in range(i+1, length):
                second_card = self.holding_card_list[k]

                if one_card.number == second_card.number:
                    if one_card not in self.open_card_list:
                        self.open_card_list.append(one_card)
                        self.holding_card_list.remove(one_card)
                        length = length - 1

                    if second_card not in self.open_card_list:
                        self.open_card_list.append(second_card)
                        self.holding_card_list.remove(second_card)
                        length = length - 1
    """
