from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def climb(n):
            if n==1:
                return 1
            if n==2:
                return 2
            return climb(n-1)+climb(n-2)
        return climb(n)

            
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna