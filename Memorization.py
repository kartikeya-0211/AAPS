def fun(coins, target):
    memo = {}
    def count(idx, target):
        if target == 0:
            return 1
        if idx == len(coins) or target < 0:
            return 0
        key = (idx, target)
        if key in memo:
            return memo[key]
        include = count(idx, target - coins[idx])
        exclude = count(idx + 1, target)
        memo[key] = include + exclude
        return memo[key]
    return count(0, target)
print(fun([1, 3, 6], 128))
