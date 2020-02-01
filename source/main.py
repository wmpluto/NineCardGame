import itertools
import time
from random import sample

from tqdm import trange

from Card import *
from NineCardEvaluator import NineCardEvaluator
from ThreeCardEvaluator import ThreeCardEvaluator

PLAYER_NUM = 4
ROUND_NUM = 100
TARGET_GROUP = 2

MY_CARD = ['H2', 'C2', 'D3']

def get_pool():
    if MY_CARD:
        my_cards = [SUIT_CONST.index(i[0]) + 4*RANK_CONST.index(i[1]) for i in MY_CARD]
        return sample([i for i in list(range(52)) if i not in my_cards], (PLAYER_NUM - 1)*9)
    else:
        return sample(range(52), (PLAYER_NUM - 1)*9)


def main():
    win_num_0 = 0
    win_num_1 = 0
    win_num_2 = 0

    my_card_value = ThreeCardEvaluator.evaluate([Card(_) for _ in MY_CARD])

    for _i in trange(ROUND_NUM, ascii=True):
        # Drawing Cards
        pool = get_pool()

        target_results_0 = []
        target_results_1 = []
        target_results_2 = []
        for j in range(PLAYER_NUM-1):
            cards = pool[j*9:j*9+9]
            m, _ = NineCardEvaluator.max(cards)
            target_results_0.append(ThreeCardEvaluator.evaluate(m[0]))
            target_results_1.append(ThreeCardEvaluator.evaluate(m[1]))
            target_results_2.append(ThreeCardEvaluator.evaluate(m[2]))

            # print(f"{[', '.join([str(_) for _ in case]) for case in m]} {v}")
        # print(target_results_1)

        if my_card_value >= max(target_results_0):
            win_num_0 += 1
        if my_card_value >= max(target_results_1):
            win_num_1 += 1
        if my_card_value >= max(target_results_2):
            win_num_2 += 1            

    print(f"{MY_CARD} WIN@0: {win_num_0:3} {win_num_0/ROUND_NUM:7.2%}")
    print(f"{MY_CARD} WIN@1: {win_num_1:3} {win_num_1/ROUND_NUM:7.2%}")
    print(f"{MY_CARD} WIN@2: {win_num_2:3} {win_num_2/ROUND_NUM:7.2%}")


if __name__ == '__main__':
    time.clock()
    main()
    print(time.clock())