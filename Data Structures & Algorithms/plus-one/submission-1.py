class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = 0
        carry = 1
        while carry and i < len(digits):
            digits[len(digits)-1-i] += 1
            if digits[len(digits)-1-i] == 10:
                digits[len(digits)-1-i] = 0
            else:
                carry = 0
            
            i += 1
        
        if i == len(digits) and carry:
            return [1] + digits

        return digits