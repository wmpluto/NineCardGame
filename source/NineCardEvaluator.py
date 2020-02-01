from Card import Card
from ThreeCardEvaluator import ThreeCardEvaluator
import itertools

class NineCardEvaluator(object):

    @staticmethod
    def max(cards):
        if not isinstance(cards, list):
            return -1
        if len(cards) != 9:
            return -1

        max_cards = []
        max_value = 0
        for i in itertools.combinations(cards, 3):
            remain = [_ for _ in cards if _ not in i]
            for j in itertools.combinations(remain, 3):
                k = [_ for _ in remain if _ not in j]
                card_cases = [
                    [Card(i[0]), Card(i[1]), Card(i[2])],       
                    [Card(j[0]), Card(j[1]), Card(j[2])],      
                    [Card(k[0]), Card(k[1]), Card(k[2])],       
                ]
                res, values = NineCardEvaluator.valid(card_cases)
                
                if res and values > max_value:
                    max_cards = card_cases
                    max_value = values
                ##elif res and values == max_value and ThreeCardEvaluator.evaluate(card_cases[0]) > ThreeCardEvaluator.evaluate(max_cards[0]):
                ##    max_cards = card_cases
                ##    max_value = values        

        return max_cards, max_value

    @staticmethod
    def valid(card_cases):     
        if not isinstance(card_cases, list):
            return -1
        if len(card_cases) != 3:
            return -1
        for case in card_cases:
            if len(case) != 3:
                return -1

        hand_values = []
        for case in card_cases:
            hand_value = ThreeCardEvaluator.evaluate(case)
            hand_values.append(hand_value)

        if (hand_values[0] <= hand_values[1]) and (hand_values[1] <= hand_values[2]):
            return True, sum(hand_values)
        else:
            return False, 0

if __name__ == "__main__":
    from random import sample

    cards = sample(range(52), 9)
    m, v = NineCardEvaluator.max(cards)
    print(f"{[', '.join([str(_) for _ in case]) for case in m]} {v}")

    cards = [
        'SA', 'S2', 'S4',
        'C6', 'CK', 
        'H4', 'H6', 'H9', 
        'DQ', 
    ]
    m, v = NineCardEvaluator.max(cards)
    print(f"{[', '.join([str(_) for _ in case]) for case in m]} {v}")