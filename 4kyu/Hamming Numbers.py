def hamming(n):
    # TODO: implement
    if n == 1:
        return 1
    i, j, k = 0, 0, 0
    dp = [1]
    while(len(dp) < n):
        min_ = min(dp[i]*2, dp[j]*3, dp[k]*5)
        if min_ == dp[i]*2:
          i += 1
          if dp[-1] == min_:
              continue
          dp.append(min_)
        elif min_ == dp[j]*3:
          j += 1
          if dp[-1] == min_:
              continue
          dp.append(min_)
        else:
          k += 1
          if dp[-1] == min_:
              continue
          dp.append(min_)
    return dp[-1]