class Solution:
    def isValid(self, s: str) -> bool:
        result=[]
        check={'(':')','{':'}','[':']'}
        for i in s:
            if i in check:
                result.append(i)
            else:
                if not result or check[result[-1]]!=i:
                    return False
                result.pop()
        return len(result)==0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna