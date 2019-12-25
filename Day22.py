import re

def solution_part_one(input_list):
    card_deck = [card for card in range(10007)]
    deal_into_pattern = re.compile(r"(deal into new stack)")
    cut_cards_pattern = re.compile(r"(cut) (-?\d+)")
    deal_with_pattern = re.compile(r"(deal with increment) (\d+)")

    def deal_into_new_stack():
        print("Deal into new stack")

    def cut_cards(number):
        print(f"Cut {number} cards")

    def deal_with_increment(number):
        print(f"Deal with increment {number}")

    for operation in input_list:
        if deal_into_pattern.match(operation):
            deal_into_new_stack()
        elif cut_cards_pattern.match(operation):
            number = cut_cards_pattern.match(operation).group(2)
            cut_cards(number)
        else: # deal with increment
            number = deal_with_pattern.match(operation).group(2)
            deal_with_increment(number)

    position_of_2019 = card_deck.index(2019)
    print(f"Position of card 2019 is {position_of_2019}")

if __name__ == '__main__':
    with open("Day22Input.txt") as file:
        result = [line.rstrip('\n') for line in file.readlines()]
    solution_part_one(result)
