class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def is_valid_combination(combination):
            count = 0
            for parenthesis in combination:

                count += 1 if parenthesis == "(" else -1
                if count < 0:
                    return False
            
            return count == 0
        
        def backtracking(combination):
            if len(combination) == 2 * n:

                if is_valid_combination(combination):
                    result.append(combination)

                return
            
            backtracking(combination + "(")
            backtracking(combination + ")")
            combination[:-1]
        

        backtracking("")
        return result
