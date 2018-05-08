import random
from basic.queue import Queue


class Printer(object):
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True

        else:
            return False

    def start_next(self, next_task):
        self.current_task = next_task
        self.time_remaining = next_task.get_pages() * 60 / self.page_rate


class Task(object):
    def __init__(self, time):
        self.time_stamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.time_stamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.time_stamp

c = 0
def new_print_task():
    num = random.randrange(1,181)
    if num == 180:
        global c
        c += 1
        # print(c, num, 'num')
        return True
    else:
        return False


def simulation(num_seconds, page_per_minute):
    # 初始化一个打印机每分钟能打多少页， 初始化一个队列。
    lab_printer = Printer(page_per_minute)
    print_queue = Queue()
    wailting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.en_queue(task)
        # 打印机没任务 和  打印队列不为空
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            # 获取一个新打印任务
            next_task = print_queue.de_queue()
            # 添加这个任务的等待时间
            wailting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        # 这里模拟处理任务，立刻就完成
        lab_printer.tick()
    average_wait = sum(wailting_times) / len(wailting_times)
    print("Average Wait %6.2f secs %3d tasks remaining."%(average_wait, print_queue.size()))

for i in range(10):
    # 10次 的3600）每分钟打印5页
    simulation(3600, 5)
