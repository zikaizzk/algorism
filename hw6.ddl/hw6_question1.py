import sys
from ast import literal_eval


class PriorityQueue:
    def __init__(self):
        self.data=[]

    def is_empty(self):
        return len(self.data)==0

    def push(self,item):
        self.data.append(item)
        i=len(self.data)-1

        while i>0:
            parent=(i-1)//2

            if self.data[i]>=self.data[parent]:
                break

            self.data[i],self.data[parent]=self.data[parent],self.data[i]
            i=parent

    def pop(self):
        if self.is_empty():
            raise IndexError("Empty priority queue")

        smallest=self.data[0]
        last=self.data.pop()

        if self.data:
            self.data[0]=last
            i=0

            while True:
                left=2*i+1
                right=2*i+2
                smallest_index=i

                if left<len(self.data) and self.data[left]<self.data[smallest_index]:
                    smallest_index=left

                if right<len(self.data) and self.data[right]<self.data[smallest_index]:
                    smallest_index=right

                if smallest_index==i:
                    break

                self.data[i],self.data[smallest_index]=self.data[smallest_index],self.data[i]
                i=smallest_index

        return smallest


def merge_logs(logs):
    queue=PriorityQueue()
    result=[]

    for register,log in enumerate(logs,1):
        if log:
            queue.push((log[0],register,0))

    while not queue.is_empty():
        time,register,index=queue.pop()
        result.append((time,register))

        index+=1
        log=logs[register-1]

        if index<len(log):
            queue.push((log[index],register,index))

    return result


def main():
    logs=[]

    for line in sys.stdin:
        if line.strip():
            logs.append(literal_eval(line))

    result=merge_logs(logs)

    print("Registers:",len(logs))
    print("Total sales:",len(result))
    print("Merged log:",result)


if __name__=="__main__":
    main()