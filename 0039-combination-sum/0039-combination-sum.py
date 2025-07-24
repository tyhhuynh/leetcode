class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []

        def dfs(i, current, total):
            # base cases:
            if total == target:
                results.append(list(current)) # current.copy()
                return
            if i >= len(candidates) or total > target:
                return

            # recursive case:
            current.append(candidates[i])
            dfs(i, current, total + candidates[i]) # continue w/ candidates[i]
            current.pop()
            dfs(i + 1, current, total) # remove candidates[i] option and move onto next
        
        dfs(0,[], 0)
        return results