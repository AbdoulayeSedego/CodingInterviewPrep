class TwoSum:
    def __init__(self):
        # Your data structure here
        # Store numbers and their frequency
        self.nums = {}
        
    
    def add(self, number: int) -> None:
        # Add number to the collection
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1
    
    def find(self, value: int) -> bool:
        # For each stored number, check if its complement exists
        for num in self.nums:
            complement = value - num
            #check if complement exists
            if complement in self.nums:
                # if num == complement, we need at least 2 of that number
                if num == complement:
                    if self.nums[num] >= 2:
                        return True
                else:
                    return True
        return False

# Test
twoSum = TwoSum()
twoSum.add(1)
twoSum.add(3)
twoSum.add(5)
print(twoSum.find(4))  # True (1 + 3)
print(twoSum.find(7))  # False