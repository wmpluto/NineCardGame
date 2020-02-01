CARD_CONST = {
    "A": 14,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13
}

SUIT_CONST = ['S', 'H', 'C', 'D']
RANK_CONST = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]


class Card(object):
    """
        牌的花色+牌值
    """

    def __init__(self, val):
        if isinstance(val, int):
            self.suit = SUIT_CONST[val % 4]
            self.rank = RANK_CONST[int(val/4)]
            self.value = CARD_CONST[self.rank]
        else:
            self.suit = val[0]
            self.rank = val[1]
            self.value = CARD_CONST[val[1]]

    def __str__(self):
        return "%s%s" % (self.suit, self.rank)
