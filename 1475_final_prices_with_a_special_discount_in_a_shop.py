# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        results = prices.copy()
        for i, price in enumerate(prices[:-1]):
            for next_item in prices[i+1:]:
                if next_item <= price:
                    results[i] = results[i] - next_item
                    break
        return results


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        print(prices)
        right_mins = [0,]*n
        stack = []
        stack.append(prices[-1])
        print("Initial stack:", stack)
        for i in range(n-2, -1, -1):
            print("Stack:", stack)
            print(f"{i=}  {prices[i]=}")
            inp = input()
            while stack and stack[-1] > prices[i]:
                inp = input()
                stack.pop()
                print("stack:", stack)
            if stack and stack[-1] <= prices[i]:
                right_mins[i] = stack[-1]
                print("right_mins:", right_mins)
            elif not stack:
                right_mins[i] = 0
                print("right_mins:", right_mins)
            stack.append(prices[i])
        for i in range(n):
            right_mins[i] = prices[i] - right_mins[i]
        print("Answer: ", right_mins)
        return right_mins

class Solution2:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        right_mins = [0,]*n
        stack = []
        stack.append(prices[-1])
        for i in range(n-2, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if stack and stack[-1] <= prices[i]:
                right_mins[i] = stack[-1]
            elif not stack:
                right_mins[i] = 0
            stack.append(prices[i])
        for i in range(n):
            right_mins[i] = prices[i] - right_mins[i]
        return right_mins


class Solution3:
    def finalPrices(self, prices):
        n = len(prices)
        stack = []
        right_mins = [0,]*n
        right_mins[-1] = 0
        for i in range(n - 2, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if stack and stack[-1] <= prices[i]:
                right_mins[i] = stack[-1]
                


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ms = [] 
        #i = 0
        l = len(prices)
        answer = prices.copy()
        for j, price in enumerate(prices):
            print(ms , answer)
            if ms == []:
                ms.append([j, price])
            elif price > ms[-1][1]:
                ms.append([j, price])
            else:
                while ms and price <= ms[-1][1]: #ms[-1][1] - top stack element.
                    answer[ms[-1][0]] = ms[-1][1] - price
                    ms.pop()
            ms.append([j,price])
        print(answer) 
        return answer






class SolutionLesha2:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ms = [] 
        i = 0
        l = len(prices)
        #answer = prices.copy()
        for j,a in enumerate(prices):
            if ms == []:
                ms.append([j,a])
            elif a > ms[-1][1]:
                ms.append([j,a])
            else:
                while ms and a <= ms[-1][1] :
                    prices[ms[-1][0]] = ms[-1][1] - a
                    ms.pop()
                ms.append([j,a])

        return prices

#class SolutionLesha1:
    #n = len(prices)
    #ms = []
    #answer = prices.copy()
    #for i, price in enumerate(
    




sol = Solution()

prices = [8,4,6,2,3]
print(sol.finalPrices(prices))

prices = [1,2,3,4,5]
print(sol.finalPrices(prices))

prices = [10,1,1,6]
print(sol.finalPrices(prices))



