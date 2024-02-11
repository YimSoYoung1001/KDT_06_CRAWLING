# 각 클래스의 객체 생성 및 게임 진행

from card import Card
from player import Player
from gamedealer import GameDealer

def play_game():
    #두 명의 player 객체 생성
    player1 = Player('흥부')
    player2 = Player('놀부')

    dealer = GameDealer() #dealer라는 객체 생성
    dealer.make_deck()    #카드 deck 1개를 만듦
    dealer.random_print_deck()  #랜덤하게 섞어서 인출
    print(' \n\n\n')

    # [카드게임 : 1단계]
    print('='*50)
    share_num = 10
    print(f'카드 나누어 주기: {share_num}장')
    print('-'*50)
    print(f'[GameDealer] 딜러가 가진 카드 수 : {52-share_num-share_num}')
    player1.add_card_list(dealer.deck[:10])
    dealer.deck = dealer.deck[10:]
    player2.add_card_list(dealer.deck[:10])
    dealer.deck = dealer.deck[10:]
    print()

    player1.display_two_card_lists()
    player2.display_two_card_lists()


    print(' \n\n\n')
    # [카드게임 : 2단계]
    answer = ''
    #answer = input('[2]단계: 다음 단계 진행을 위해 Enter 키를 누르세요!: ')
    if answer == '':
        player1.check_one_pair_card()
        print('중복검사 완료')
        player1.display_two_card_lists()

        player2.check_one_pair_card()
        player2.display_two_card_lists()



if __name__ == '__main__':
    play_game()