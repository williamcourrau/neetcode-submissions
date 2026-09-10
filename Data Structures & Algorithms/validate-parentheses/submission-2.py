class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        stack_brackets = []

        for bracket in s:
            if bracket in brackets: # [(])
                stack_brackets.append(bracket)
            else: # closed bracket case "]"
                if not stack_brackets:
                    return False
            
                open_bracket = stack_brackets.pop()
                if brackets[open_bracket] != bracket: # Not follow the order brackets
                    return False
        
        return True if len(stack_brackets) == 0 else False