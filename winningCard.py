def winning_card(cards, trump=None):
    ranks = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
             'eight': 8, 'nine': 9, 'ten': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}

    if (trump == None):
        start_ranks = cards[0][0]
        start_suits = cards[0][1]

        for x in range(4):
            rank1 = ranks[cards[x][0]]
            rank2 = ranks[start_ranks]
            if (cards[x][1] == start_suits) and (rank1 > rank2):
                start_ranks = cards[x][0]

        return (start_ranks, start_suits)

    elif (trump != None):

        for x in range(4):
            if cards[x][1] == trump:
                start_suits = trump
                start_ranks = cards[x][0]
                break
            else:
                start_ranks = cards[0][0]
                start_suits = cards[0][1]
        for i in range(4):
            rank1 = ranks[cards[i][0]]
            rank2 = ranks[start_ranks]

            if (cards[i][1] == start_suits) and (rank1 > rank2):
                start_ranks = cards[i][0]
        return (start_ranks, start_suits)
