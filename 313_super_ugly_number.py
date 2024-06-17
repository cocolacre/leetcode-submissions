# https://leetcode.com/problems/super-ugly-number/
class Solution:
    """comprehensive dynamic programming solution, made via help of blackbox.ai.
    TODO: Rewrite myself dry.
    """
    def nthSuperUglyNumber(self,n, primes):
        uglies = [1]
        indices = [0] * len(primes)
        while len(uglies) < n:
            next_ugly = min([uglies[indices[i]] * primes[i] for i in range(len(primes))])
            print( indices, uglies, primes, [uglies[indices[i]] * primes[i] for i in range(len(primes))])
            uglies.append(next_ugly)
            for i in range(len(primes)):
                if uglies[indices[i]] * primes[i] == next_ugly:
                    indices[i] += 1
        return uglies[-1]

primes = [2,3]
primes = [2,7]
primes = [2,11,31]
primes = [2,5,7,11]
primes = [2,5,7,11,13,17,19,23,37]
