class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return -1
        if len(tokens) == 1:
            return int(tokens[0])

        operators = ["+", "-", "/", "*"]

        result = 0
        def calc(digit_1, digit_2, operator):
            nonlocal result
            match operator:
                case "+":
                    result = digit_1 + digit_2 
                case "-":
                    result = digit_1 - digit_2
                case "*":
                    result = digit_1 * digit_2
                case "/":
                    result = int(digit_1 / digit_2)

        nums = []
        for token in tokens:
            if token in operators:
                if len(nums) >= 2:
                    digit_2 = nums.pop()
                    digit_1 = nums.pop()

                    calc(int(digit_1), int(digit_2), token)
                    nums.append(result)
            else:
                nums.append(token)

        return result