# Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

# Q2
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        if(self.value > 100):
             self.value = 100

class MaxLimitCalculator(Calculator):
    # def add(self, val):
    #     self.value += val
    #     if(self.value > 100):
    #         self.value = 100
    def __init__(self):
        super().__init__()
        
cal = MaxLimitCalculator()
cal.add(50)
print(cal.value)
cal.add(60)
print(cal.value)


#Q6
def multi(numberlist):
    result = []
    for number in numberlist:
        result.append(number * 3)
    return result        
result = multi([1,2,3,4])
print(result)

def multi(numberlist):
    return list(map(lambda number: number * 3, numberlist))
result = multi([1, 2, 3, 4])
print(result)

result = list(map(lambda number:number*3, [1,2,3,4]))
print(result)

