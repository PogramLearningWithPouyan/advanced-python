#range(10,50,5)
class myrange:
    def __init__(self,start,end,step=1):
        self.count=start
        self.end=end
        self.step=step
    def __iter__(self):
        return self
    def __next__(self):
        if self.count<self.end:
            num=self.count
            self.count+=self.step
            return num
        raise StopIteration
    def __len__(self):
        return 10
x=myrange(10,20)
iter(x)
#print(len(x))
for num in x:
    print(num)