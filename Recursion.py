def fun(coins, target):
    def count(idx, target):
        if target == 0:
            return 1
        if idx == len(coins) or target < 0:
            return 0
        include = count(idx, target - coins[idx])
        exclude = count(idx + 1, target)
        return include + exclude
    return count(0, target)
print(fun([1, 3, 6], 12))
