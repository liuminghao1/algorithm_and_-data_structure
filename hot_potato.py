from basic.queue import Queue


def hot_potato(name_list,num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.en_queue(name)
    while sim_queue.size() > 1:
        for i in range(num):
            # 用队尾来数数
            sim_queue.en_queue(sim_queue.de_queue())
        sim_queue.de_queue()

    return sim_queue.de_queue()


c = hot_potato([1,2,3,4,5], 3)

