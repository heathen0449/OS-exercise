import random

buffer = ['*' for i in range(8)]
full = []
empty = []
mutex_list= []
bufferempty = 8
bufferfull = 0
mutex = 1
current_process ='null'
pointer = 0


class Process:
    content = 0 
    owner ='root'

    def show(self):
        print(self.owner,end=' ')
    
    def work(self):
        pass

    def show_init(self):
        print(self.content,end=' ')

class Producer(Process):
    
    def __init__(self,content):
        self.content = content
        self.owner = 'P'+str(random.randrange(10))
    
    def get_content(self):
        return self.content
    
    def get_owner(self):
        return self.owner
    
    def work(self):
        global pointer
        global current_process
        if pointer>7:
            pointer = pointer%8
        buffer[pointer] = self
        current_process = self.owner
        pointer += 1

        
class Customer(Process):
    
    def __init__(self):
        self.owner = 'C'+str(random.randrange(0,10))
    
    def get_owner(self):
        return self.owner
    
    def work(self):
        global pointer
        global current_process
        if pointer>7:
            pointer = pointer%8
        self.content = buffer[pointer].get_content()
        buffer[pointer]='*'
        pointer += 1
        current_process = self.owner


def show():
    print('\n---------------------------------------------------')
    print('缓冲区此时情况：')
    for a in range(8):
        if isinstance(buffer[a],Process):
            buffer[a].show_init()
        else:
            print(buffer[a],end=' ')
    print('\n')
    print('满等待队列情况：')
    for a in full:
        a.show()
    print('\n')
    print('空等待队列情况：')
    for a in empty:
        a.show()
    print('\n')
    print('互斥等待队列情况：')
    for a in mutex_list:
        a.show()
    print('\n')
    print('缓冲区空闲数：%d'%bufferempty)
    print('缓冲区占有数：%d'%bufferfull)
    print('互斥锁：%d'%mutex)
    print('当前工作进程%s'%current_process)
    print('-------------------------------------------------\n')

def processor():
    global bufferempty,pointer,mutex
    proc1 = Producer(random.randrange(0,100))
    bufferempty = bufferempty-1
    if bufferempty>-1:       
        if mutex ==1:
            mutex = mutex-1
            proc1.work()
        else:
            mutex_list.append(proc1)
            bufferempty+=1
    else:
        empty.append(proc1)
        bufferempty+=1
    

def con():
    global bufferfull,pointer,mutex
    proc2 = Customer()
    bufferfull -= 1
    if bufferfull >-1:
        if mutex==1:
            mutex = 0
            proc2.work()
        else:
            mutex_list.append(proc2)
            bufferfull+=1
    else:
        full.append(proc2)
        bufferfull+=1

def exit(number):
    global mutex
    global bufferfull
    global bufferempty
    global current_process
    mutex=1
    current_process = 'null'
    if number==0:
        bufferfull +=1
        if len(mutex_list)>0:
            bufferempty -=1
            mutex_list[0].work()
            mutex_list.pop(0)
        elif len(empty)>0:
            empty[0].work()
            empty.pop(0)
    elif number==1:
        bufferempty +=1
        if len(mutex_list)>0:
            bufferfull-=1
            mutex_list[0].work()
            mutex_list.pop(0)
        elif len(full)>0:
            full[0].work()
            full.pop(0)
    

def proof():
    for i in buffer:
        if i !='*':
            return True
    return False

def error(choice):
    right = ['p','c','e','q']
    ans = choice
    while ans not in right:
        ans=input('请输入您的操作，操作为p/c/e,q为退出:')
    return ans


def init():
    show()
    choice= input('请输入您的操作，操作为p/c/e,q为退出:')
    choice = error(choice)
    while choice!='q':
        if choice =='p':
            processor()
            show()
            no = 0
        elif choice =='e':
            exit(no)
            show()
        elif choice =='c':
            con()
            show()
            no=1
        choice = input('请输入您的操作，操作为p/c/e,q为退出:')
        choice = error(choice)
    print("感谢使用")
    return

if __name__=="__main__":
    init()



        
