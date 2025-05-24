MAX_DAYS = 50

def magic_cows(C, N, M, initial_cows, queries):
    dp = [[0 for _ in range(C + 1)] for _ in range(MAX_DAYS + 1)]
    for cows in initial_cows:
        dp[0][cows] += 1

    for day in range(MAX_DAYS):
        for i in range(1, C + 1):  #farm sizes
            if dp[day][i] == 0:
                continue  #no farms of this size
            if i * 2 <= C:  #doubling will not exceed the limit
                dp[day + 1][i * 2] += dp[day][i]
            else:   #doubling exceeds limit:
                dp[day + 1][i] += 2 * dp[day][i]

    results = []
    for day in queries:
        total_farms = sum(dp[day][1:])
        results.append(total_farms)

    return results

#example
C = 8
N = 4
M = 13
initial_cows = [2, 3, 2, 1]
queries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
answers = magic_cows(C, N, M, initial_cows, queries)
print(answers)
