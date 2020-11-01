# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

coins = [1, 2, 5, 10, 20, 50, 100, 200]
result = 200


# comb = []

# for coin in coins:
#     value = "+".join( [str(coin) for _ in range(0, int(200/coin))])
#     print(value)
#     comb.append(value)

# for selected_coins in range(0, len(coins)):
#     print('selected_coin', coins[selected_coins])
#     print('selected_coins', coins[:selected_coins])


# print('Total combinations', len(comb))


# def _get_change_making_matrix(set_of_coins, r):
#     m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]

#     for i in range(r + 1):
#         m[0][i] = i

#     return m

# print('_get_change_making_matrix', _get_change_making_matrix(coins, result))

def changes(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]

print(changes(result, coins))