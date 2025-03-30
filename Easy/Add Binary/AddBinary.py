class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i,j = len(a) - 1, len(b) - 1

        while i>=0 or j >= 0 or carry:
            binary_a = int(a[i]) if i >= 0 else 0
            binary_b = int(b[j]) if j >= 0 else 0
            curr_sum = binary_a + binary_b + carry
            res.append(str(curr_sum % 2))
            carry = curr_sum // 2
            i -= 1
            j -= 1
        return ''.join(res[::-1])

#QED
#Problem 67 (Easy Of Add Binary) - Jason Balayev (python)