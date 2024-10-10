def linear_search(data, key) :
    i = 0
    while True : 
        if data[i] == key :
            print("검색 성공!\nkey값은 %d입니다." %data[i])
            break
        
        if i+1 == len(data) :
            print("검색 실패!")
            break
        i += 1


a=[6,32,25,6765,1,58,2,5]

linear_search(a, 2)


def binary_search(data, key) :
    data.sort()
    start=0
    end=len(data) - 1

    while start <= end :
        mid = (start + end) // 2

        if data[mid] == key :
            print('검색 성공!\n%d번 인덱스에 key값이 존재합니다.' %mid)
            return 0
        
        elif data[mid] > key :
            end = mid - 1

        elif data[mid] < key :
            start = mid + 1

    return 0

binary_search(a, 7)



class Stack() :
    def __init__(self):
        self.stack = []

    def push(self, data) :
        self. stack.append(data)

    def pop(self) :
        pop_object = None
        if self.isEmpty() : 
            print("Stack is Empty")
        else : 
            pop_object = self.stack.pop()

        return pop_object
    
    def top(self) :
        top_object = None
        if self.isEmpty() :
            print("Stack is Empty")
        else : 
            top_object = self.stack[-1]

        return top_object

    def isEmpty(self) :
        is_empty = False
        if len(self.stack) == 0 :
            is_empty = True
        return is_empty



stack = [4,5,6,6,7,8,8]

stack.append(7)

print(stack)



class Queue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return -1
        else:
            return self.queue.pop(0)
        
    def printQueue(self):
        print(self.queue)

if __name__ == "__main__":
    queue_list = ListQueue()
    queue_list.enqueue(1)
    queue_list.enqueue(2)
    queue_list.enqueue(3)
    queue_list.enqueue(4) 
    queue_list.enqueue(5)
    queue_list.printQueue()
    print(queue_list.dequeue())
    print(queue_list.dequeue())
    print(queue_list.dequeue())
    print(queue_list.dequeue())
    print(queue_list.dequeue())
    queue_list.printQueue()


from collections import dequedq=deque([])

dq= 
   