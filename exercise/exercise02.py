ready_queue = [] 
run_queue = []
blocked_queue = []
exit_queue = []
start_queue = []
ready_suspend = []
blocked_suspend = []

name_list = [ready_queue,run_queue,blocked_queue,start_queue,exit_queue,ready_suspend,blocked_suspend]

memory_capactiy = 100 

class PCB:
    
    pid = ' '
    capacity = 0
    status = 'new'
    priority = ' '

    def __init__ (self,name,size,priority,status='new'):
        global start_queue
        self.pid = name
        self.capacity = size
        self.status =  status
        self.priority = priority
        start_queue.append(self)
    
    def show(self):
        print(self.pid,' ',self.capacity,' ',self.status,' ',self.priority)
    

        
def show(a):
    for i in range(len(a)):
        print(a[i].pid,end=' ')
    print('\n')

def show_all():
    print("就绪态进程对列内容：")
    show(ready_queue)
    print("执行态进程队列内容：")
    show(run_queue)
    print("挂起态进程对列内容:")
    show(blocked_queue)
    print("处于创建态进程：")
    show(start_queue)
    print('处于结束态进程：')
    show(exit_queue)
    print("处于就序挂起态进程：")
    show(ready_suspend)
    print("处于阻塞挂起态进程:")
    show(blocked_suspend)

def b_to_bs(lista,listc,listg,sign=0):
    global memory_capactiy
    if len(listc) ==0:
        raise Exception("阻塞进程队列为空，进行了非法操作")
    if len(lista)==0 or sign!=0:
        process = listc[0]
        listc.pop(0)
        process.status = 'blocked,suspend'
        listg.append(process)
        memory_capactiy = memory_capactiy + process.capacity

         
def r_to_rs(lista,listc,listf):
    global memory_capactiy
    if len(lista)==0:
        raise Exception("就绪对列为空，操作非法")
    if listc[0].priority == 'high' and lista[0].priority =='low':
        process = lista[0]
        process.status = 'ready,suspend'
        listf.append(process)
        memory_capactiy = memory_capactiy + process.capacity

def run_to_rs(lista,listb,listf):
    global memory_capactiy
    if len(listb)==0:
        raise Exception("运行队列为空，操作非法") 
    process = listb[0]
    listb.pop(0)
    process.status = 'ready,suspend'
    listf.append(process)
    memory_capactiy = memory_capactiy + process.capacity
    if len(listb)==0 and len(lista)>0:
        dispatch(lista,listb)

def dispatch(lista,listb):
    if len(lista)==0:
        raise Exception("就绪对列为空，操作非法") 
    process = lista[0]
    process.status = 'runnning'
    lista.pop(0)
    listb.append(process)


def time_out(lista,listb):
    if len(listb)==0:
        raise Exception("运行队列为空，操作非法")
    process = listb[0]
    process.status = 'ready'
    listb.pop(0)
    lista.append(process)
    dispatch(lista,listb)


def event_wait(lista,listb,listc):
    if len(listb)==0:
        raise Exception("运行队列为空，操作非法")
    process = listb[0]
    process.status = 'blocked'
    listb.pop(0)
    listc.append(process)
    if len(lista)>0:
        dispatch(lista,listb)

def event_occur(lista,listb,listc):
    if len(listc)==0:
        raise Exception("阻塞队列为空，操作非法")
    process = listc[0]
    process.status = 'ready'
    listc.pop(0)
    lista.append(process)
    if len(listb)==0:
        dispatch(lista,listb)

def create_process(lista,listb,listc,listd,liste,listf,listg):
    global memory_capactiy
    if len(listd)==0:
        raise Exception("无准备态进程，操作非法")
    elif len(lista)>0 and memory_capactiy<lista[0].capacity:
        new_to_rs(lista,listb,listc,listd,liste,listf,listg)
        return
    listd[0].show()
    process =  listd[0]
    process.status = 'ready'
    listd.pop(0)
    lista.append(process)
    memory_capactiy = memory_capactiy - process.capacity
    if len(listb)==0:
        dispatch(lista,listb)

def release(lista,listb,liste):
    if len(listb)==0:
        raise Exception("CPU内无运行进程，操作非法")
    process=listb[0]
    process.status = 'exit' 
    listb.pop(0)
    liste.append(process)
    if len(listb)==0:
        dispatch(lista,listb)

def bs_to_rs(lista,listb,listf,listg):
    if len(listg)==0:
        raise Exception("阻塞挂起队列为空，操作非法")
    process = listg[0]
    process.status = 'ready,suspend'
    listg.pop(0)
    listf.append(process)
    if process.priority == 'high'  and len(listb)!=0:
        run_to_rs(lista,listb,listf)

def rs_to_r(lista,listb,listc,listf,listg):
    global memory_capactiy
    if len(listf)==0:
        raise Exception("就序挂起对列为空，操作非法")    
    if len(lista)==0 or (listf[0].priority =='high' and lista[0].priority=='low'):
        process = listf[0]
        process.status = 'ready'
        listf.pop(0)
        while process.capacity > memory_capactiy:
            b_to_bs(lista,listc,listg,sign=1)
        lista.append(process)
        memory_capactiy = memory_capactiy-process.capacity
        if len(listb)==0:
            dispatch(lista,listb)
    else:
        raise Exception("该操作进程优先级不满足条件或就绪进程队列不为空，该操作不支持")

def bs_to_b(listc,listg):
    global memory_capactiy
    if len(listg)==0:
        raise Exception("阻塞挂起队列为空，操作非法")
    if memory_capactiy>listg[0].capacity and listg[0].priority =='high':
        process = listg[0]
        process.status = 'blocked'
        listg.pop(0)
        listc.append(process)
        memory_capactiy = memory_capactiy - process.priority
    else:
        raise Exception("容量不足，或当前就绪挂起态进程优先级不支持该操作")

def new_to_rs(lista,listb,listc,listd,liste,listf,listg):
    if len(listd)==0:
        raise Exception("操作非法，不存在创建态进程")
    process = listd[0]
    process.status = 'ready,suspend'
    listd.pop(0)
    listf.append(process)
    if len(lista)==0 or (listf[0].priority =='high' and lista[0].priority=='low'):
        rs_to_r(lista,listb,listc,listf,listg)

def error(choice):
    while choice.isdigit()==False  or int(choice)>13 or int(choice)<0:
        print("输入非法，请重新选择：")
        choice = input ("您的选择是：")
    return int(choice)

def system():
    print('系统目前状态：')
    print('--------------------------系统操作-------------------')
    print('0--进程创建态到就绪态 1-- 进程就绪态到运行态（一般为自动）2--超时、3--运行态的进程事件等待、4--阻塞态进程事件发生')
    print('5--结束进程、6--进程由创建态到就绪挂起态， 7--运行态到就绪挂起态 8--阻塞挂起态到就序挂起态')
    print('9--阻塞到阻塞挂起态 10--阻塞挂起态到阻塞态 11--就绪挂起态到就绪态 12--就绪态到就绪挂起态 13--结束系统')
    choice = input ("您的选择是：")
    option = error(choice)
    while option !=13:
        if option==0:
          create_process(ready_queue,run_queue,blocked_queue,\
              start_queue,exit_queue,ready_suspend,blocked_suspend)
        elif option==1:
            dispatch(ready_queue,run_queue)
        elif option==2:
            time_out(ready_queue,run_queue) 
        elif option==3:
            event_wait(ready_queue,run_queue,blocked_queue)
        elif option==4:
            event_occur(ready_queue,run_queue,blocked_queue)
        elif option==5:
            release (ready_queue,run_queue,exit_queue)
        elif option==6:
            new_to_rs (ready_queue,run_queue,blocked_queue,\
              start_queue,exit_queue,ready_suspend,blocked_suspend)
        elif option==7:
            run_to_rs(ready_queue,run_queue,ready_suspend)
        elif option==8:
            bs_to_rs(ready_queue,run_queue,ready_suspend,blocked_suspend)
        elif option==9:
            b_to_bs(ready_queue,blocked_queue,blocked_suspend,sign=1)
        elif option==10:
            bs_to_b(blocked_queue,blocked_suspend)
        elif option==11:
            rs_to_r(ready_queue,run_queue,blocked_queue,ready_suspend,blocked_suspend)
        elif option==12:
            r_to_rs(ready_queue,blocked_queue,ready_suspend)
        show_all()
        choice = input ("您的选择是：")
        option = error(choice)
    print("感谢您的使用")
    quit()    




if __name__ == "__main__":
    A = PCB(name='A',size=10,priority='high')
    B = PCB(name='B',size=20,priority='low')
    C = PCB(name='C',size=30,priority='high')
    D = PCB(name='D',size=40,priority='low')
    E = PCB(name='E',size=50,priority='low')
    system()
    # world = []
    # for i in range(0,15):
        # world.append(PCB('a'+str(i)))
    # run_queue.append(world[0])
    # for i in range(1,8):
        # ready_queue.append(world[i])
    # for i in range(8,15):
        # blocking_queue.append(world[i])
    # choice = int(input("请输入您的操作："))
    # while choice!= 0:
        # if choice ==2:
            # time_out(ready_queue,run_queue)
        # elif choice ==4:
            # event_occur(ready_queue,run_queue,blocking_queue)
        # elif choice ==3:
            # event_wait(ready_queue,run_queue,blocking_queue)
        #else:
            # print("暂无")
        #show_all()
        # choice = int(input("请输入您的操作："))
     
