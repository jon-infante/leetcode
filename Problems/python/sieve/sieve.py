def primes(limit):
    prime = [2]

    if limit == 1:
        return []

    for i in range(2, limit + 1): 
        if i > 1: 
            for j in range(2, i//2 + 2): 
                if (i % j) == 0: 
                    break
                else: 
                    if j == i//2 + 1: 
                        prime.append(i) 
    
    return prime