# 一个可迭代对象可以构建出任意多个不同的迭代器
# 一种迭代器可以应用于多个可迭代对象（包括其他迭代器）


file_list = ['hi','bye']
run_list = ['hi world','bye','ok fine']

class wutongIterator:
    def __init__(self,actions):
        self.actions = actions
        self.index = 0
    
    def __next__(self):
        while self.index < len(self.actions):
            action =self.actions[self.index]
            self.index +=1
            if action in file_list:
                continue
            elif 'world' in action:
                return action * 2
            else:
                return action

        raise StopIteration  # 抛出异常
    
    # 如果不增加iter接口，无法进行for循环，会抛出异常表示不是可迭代对象
    def __iter__(self):
        return self

run = wutongIterator(run_list)
# while True:
#     try:
#         print(next(run))
#     except StopIteration:
#         break

for i in wutongIterator(run_list):
    print(i)