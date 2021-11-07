class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        product = [0 for _ in range(m + n)]
        num1r = num1[::-1]
        num2r = num2[::-1]
        for n1 in range(len(num1r)):
            for n2 in range(len(num2r)):
                val = int(num1r[n1]) * int(num2r[n2]) + product[n1 + n2]
                digit = val % 10
                carry = val // 10
                product[n1 + n2] = digit
                product[n1 + n2 + 1] += carry
        result = ""
        for i in range(len(product)):
            result = str(product[i]) + result
        else:
            return result.lstrip("0")