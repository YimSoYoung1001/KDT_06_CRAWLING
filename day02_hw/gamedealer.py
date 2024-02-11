from card import Card
import random

# [ GameDealer 클래스 ]
# 1벌의 카드(deck) 생성 기능 : 리스트로 구현
# 각 player들에게 카드를 나누어 주는 기능 (자신이 가진 deck에서 제거하여 다른 선수들에게 제공)


class GameDealer:
    def __init__(self):   #클래스에서 생성자 정의
        self.deck = list()
        self.suit_number = 13

    # 카드 1개의 deck을 생성함 (self의 deck이라는 리스트에 담았음)
    def make_deck(self):
        card_suits = ['♠', '♥', '♣', '◆']
        card_numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        for suit in card_suits:
            for num in card_numbers:
                card = Card(suit, num)
                self.deck.append(card)

    # 카드를 담은 deck 리스트에서 13개씩 print
    def print_deck(self):
        count = 1
        for d in self.deck:
            if count <= 13 :
                print(d, end = ' ')
                count += 1
            if count > 13:
                count = 1
                print()

    # 카드를 담은 deck 리스트를 랜덤으로 섞은 후 13개씩 print
    def random_print_deck(self):
        random.shuffle(self.deck)
        count = 1
        for d in self.deck:
            if count <= 13:
                print(d, end=' ')
                count += 1
            if count > 13:
                count = 1
                print()


print('[GameDealer] 초기 카드 생성')
d = GameDealer()
d.make_deck()
print('-' * 50)

print('[GameDealer] 딜러가 가진 카드 수 : 52')
d.print_deck()
print()

print('[GameDealer] 카드 랜덤하게 섞기')
print('-' * 50)
print('[GameDealer] 딜러가 가진 카드 수 : 52')
d.random_print_deck()


print()









# ======================================================================================================================
# 시행착오
# ======================================================================================================================

'''
class GameDealer:
    def __init__(self):   #클래스에서 생성자 정의
        self.deck = list() #인스턴스 변수 생성
        self.suit_number = 13

    def make_deck(self):
        card_suits = ['♠', '♥','♣','◆']
        card_numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        #deck = self.deck

        for suit in card_suits:
            for num in card_numbers:
                self.deck.append(Card(suit, num))

        print('[GameDealer] 초기 카드 생성')
        print('-'*50)
        print(f"[GameDealer] 딜러가 가진 카드 수 : {self.suit_number}")

        for d in self.deck:
            if d[0] == '♠':
                print(d, end = ' ')
            elif d[0] == '♥':
                print(d, end = ' ')
            elif d[0] == '♣':
                print(d, end = ' ')
            elif d[0] == '◆':
                print(d, end = ' ')

        print()
        print('[GameDealer] 카드 랜덤하게 섞기')
        print('-' * 50)
        print(f"[GameDealer] 딜러가 가진 카드 수 : {self.suit_number}")
        random_deck = random.shuffle(self.deck)

        for r in random_deck:
            if r[0] == '♠':
                print(d, end=' ')
            elif r[0] == '♥':
                print(d, end=' ')
            elif r[0] == '♣':
                print(d, end = ' ')
            elif r[0] == '◆':
                print(d, end = ' ')
'''