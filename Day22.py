import re

def apply_shuffle_seq(sequence_list, deck_len):
    card_deck = [card for card in range(deck_len)]
    deal_into_pattern = re.compile(r"(deal into new stack)")
    cut_cards_pattern = re.compile(r"(cut) (-?\d+)")
    deal_with_pattern = re.compile(r"(deal with increment) (\d+)")

    def deal_into_new_stack():
        card_deck.reverse()

    def cut_cards(number):
        return card_deck[number:] + card_deck[:number]

    def deal_with_increment(number):
        new_deck = card_deck[:]
        step = 0
        for i in range(deck_len):
            new_deck[step] = card_deck[i]
            step = (step + number) % deck_len
        return new_deck

    for operation in sequence_list:
        if deal_into_pattern.match(operation):
            deal_into_new_stack()
        elif cut_cards_pattern.match(operation):
            number = int(cut_cards_pattern.match(operation).group(2))
            card_deck = cut_cards(number)
        else: # deal with increment
            number = int(deal_with_pattern.match(operation).group(2))
            card_deck = deal_with_increment(number)

    return card_deck

def solution_part_one(input_list, deck_len):
    card_deck = [card for card in range(deck_len)]
    card_deck = apply_shuffle_seq(input_list, deck_len)
    position_of_2019 = card_deck.index(2019)
    print(f"Position of card 2019 is {position_of_2019}")

if __name__ == '__main__':
    with open("Day22Input.txt") as file:
        result = [line.rstrip('\n') for line in file.readlines()]
    deck_len = 10007
    solution_part_one(result, deck_len)
