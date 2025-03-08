class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # 使用埃拉托斯特尼篩法(Sieve of Eratosthenes)找出所有質數
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        
        i = 2
        while i * i <= right:
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False
            i += 1
        
        # 找出範圍內的質數
        primes = [n for n in range(max(2, left), right + 1) if sieve[n]]
        
        # 如果質數數量少於2個，返回[-1, -1]
        if len(primes) < 2:
            return [-1, -1]
        
        # 尋找差距最小的質數對
        min_diff = float('inf')
        closest_pair = [-1, -1]
        
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i-1]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes[i-1], primes[i]]
        
        return closest_pair