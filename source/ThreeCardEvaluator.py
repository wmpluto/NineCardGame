from Card import Card

# 高high
HIGH_TYPE = 0
# 对子
PAIR_TYPE = 1 << 12
# 顺子
STRAIGHT_TYPE = 2 << 12
# 同花(金)
FLUSH_TYPE = 3 << 12
# 同花顺
STRAIGHT_FLUSH_TYPE = 4 << 12
# 豹子
LEOPARD_TYPE = 5 << 12


class ThreeCardEvaluator(object):
    """
    工具类
    """

    @staticmethod
    def evaluate(cards):
        if not isinstance(cards, list):
            return -1
        if len(cards) != 3:
            return -1

        vals = [card.value for card in cards]
        # 默认是从小到大排序
        vals.sort()

        # 豹子检测
        leopard_res, leopard_val = ThreeCardEvaluator.__leopard(cards, vals)
        if leopard_res:
            return LEOPARD_TYPE + (vals[0] << 8)

        # 同花检测
        flush_res, flush_list = ThreeCardEvaluator.__flush(cards, vals)
        # 顺子检测
        straight_res, straight_val = ThreeCardEvaluator.__straight(cards, vals)

        if flush_res and straight_res:
            return STRAIGHT_FLUSH_TYPE + (straight_val << 8)
        if flush_res:
            return FLUSH_TYPE + (flush_list[2] << 8) + (flush_list[1] << 4) + flush_list[2]
        if straight_res:
            return STRAIGHT_TYPE + (straight_val << 8)

        # 对子检测
        pair_res, pair_list = ThreeCardEvaluator.__pairs(cards, vals)
        if pair_res:
            return PAIR_TYPE + (pair_list[0] << 8) + (pair_list[1] << 4)

        # 剩下的高high
        return HIGH_TYPE + (vals[2] << 8) + (vals[1] << 4) + vals[2]

    @staticmethod
    def __leopard(cards, vals):
        if cards[0].rank == cards[1].rank and cards[1].rank == cards[2].rank:
            return True, cards[0].value
        return False, 0

    @staticmethod
    def __flush(cards, vals):
        if cards[0].suit == cards[1].suit and cards[1].suit == cards[2].suit:
            return True, vals
        return False, []

    @staticmethod
    def __straight(cards, vals):
        # 顺子按序递增
        if vals[0] + 1 == vals[1] and vals[1] + 1 == vals[2]:
            return True, vals[2]
        # 处理特殊的牌型, A23
        if vals[0] == 2 and vals[1] == 3 and vals[2] == 14:
            return True, 3
        return False, 0

    @staticmethod
    def __pairs(cards, vals):
        if vals[0] == vals[1]:
            return True, [vals[0], vals[2]]
        if vals[1] == vals[2]:
            return True, [vals[1], vals[0]]
        return False, []


if __name__ == "__main__":

    card_cases = [
        [Card('HA'), Card('SA'), Card('DA')],      # 豹子
        [Card('HA'), Card('HK'), Card('HQ')],      # 顺金
        [Card('HA'), Card('HK'), Card('HT')],      # 金
        [Card('HA'), Card('HK'), Card('SQ')],      # 顺子
        [Card('H9'), Card('D9'), Card('ST')],      # 对子
        [Card('H9'), Card('DA'), Card('ST')]       # 高牌
    ]

    for case in card_cases:
        card = ', '.join([str(_) for _ in case])
        hand_value = ThreeCardEvaluator.evaluate(case)
        print("[{}] = {}".format(card, hand_value))
