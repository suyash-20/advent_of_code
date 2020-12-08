f = open("day1.txt")
content = f.readlines()
print(content)
f.close()

data = []

for item in content:
    number_list = int(item)
    data.append(number_list)
    

class Solution(object):

    def __init__(self,first , second, third):
        self.first = first
        self.second = second
        self.third = third
        super().__init__()

    def find_answer(self):
        if self.first + self.second + self.third== 2020:
           # print(self.first, self.second, self.third, self.first*self.second*self.third)
            print(self.first*self.second*self.third)
            return True


for first in data:
    for second in data:
        for third in data:
            solution = Solution(first, second, third)
            solution.find_answer()




