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
    card_all = 52

    print(' \n')

    # [카드게임 : 1단계]
    print('=' * 50)
    share_num = 10
    print(f'카드 나누어 주기: {share_num}장')
    print('-' * 50)
    card_all = card_all - share_num - share_num
    print(f'[GameDealer] 딜러가 가진 카드 수 : {card_all}')
    player1.add_card_list(dealer.deck[:10])
    dealer.deck = dealer.deck[10:]
    player2.add_card_list(dealer.deck[:10])
    dealer.deck = dealer.deck[10:]
    print()

    player1.display_two_card_lists()
    player2.display_two_card_lists()

    print(' \n')

    # [카드게임 : 2단계]
    # answer = ''
    answer = input('[2]단계: 다음 단계 진행을 위해 Enter 키를 누르세요!: ')
    if answer == '':
        player1.check_one_pair_card()
        print(f"-{player1.name}의 중복검사 완료-")
        player1.display_two_card_lists()

        player2.check_one_pair_card()
        print(f'-{player2.name}의 중복검사 완료-')
        player2.display_two_card_lists()

    level_count = 3
    game_end = True
    while game_end:
        # [카드게임 : 3단계]
        answer = input(f'[{level_count}]단계: 다음 단계 진행을 위해 Enter 키를 누르세요!: ')
        if answer == '':
            print('='*50)
            share_num = 4
            print(f'카드 나누어 주기: {share_num}장')
            print('-'*50)
            card_all = card_all - share_num - share_num
            print(f'[GameDealer] 딜러가 가진 카드 수 : {card_all}')
            player1.add_card_list(dealer.deck[:10])
            dealer.deck = dealer.deck[10:]
            player2.add_card_list(dealer.deck[:10])
            dealer.deck = dealer.deck[10:]
            print()

            player1.display_two_card_lists()
            player2.display_two_card_lists()
            print(' \n')


            player1.check_one_pair_card()
            print(f"-{player1.name}의 중복검사 완료-")
            player1.display_two_card_lists()

            player2.check_one_pair_card()
            print(f'-{player2.name}의 중복검사 완료-')
            player2.display_two_card_lists()


            # 게임 종료 조건
            if ((len(dealer.deck) == 0) |
                (len(player1.holding_card_list) == 0) |
                (len(player2.holding_card_list) == 0)):
                print(f"딜러가 가진 카드의 수 : {len(dealer.deck)}")
                print(f"{player1.name}이 가진 카드의 수 : {len(player1.holding_card_list)}")
                print(f"{player2.name}이 가진 카드의 수 : {len(player2.holding_card_list)}")
                print('   게   임   종   료   ')
                game_end = False

            level_count += 1





if __name__ == '__main__':
    play_game()