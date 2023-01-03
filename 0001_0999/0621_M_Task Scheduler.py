class Solution:
    # AC, fast
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_times_list = list(Counter(tasks).values())
        max_times = max(max_times_list)
        max_times_count = max_times_list.count(max_times)
        return max(len(tasks), (n + 1) * (max_times - 1) + max_times_count)

    # AC
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     max_times_list = list(Counter(tasks).values())
    #     max_times = max(max_times_list)
    #     max_times_count = max_times_list.count(max_times)
        
    #     tasks_len = len(tasks)

    #     idle = (max_times - 1) * ((n + 1) - max_times_count)
    #     idle -= tasks_len - max_times * max_times_count
    #     idle = max(0, idle)
    #     return tasks_len + idle

    # AC, timeout
    # def leastInterval(self, tasks: List[str], n: int) -> int:

    #     tasks_counter = Counter(tasks)
    #     max_times = max(tasks_counter.values())
    #     total_task = 0
    #     tasks_times = {t: set() for t in range(1, max_times+1)}
    #     for task, times in Counter(tasks).items():
    #         tasks_times[times].add(task)
    #         total_task += times
        
    #     # print(tasks_times)

    #     running = {}
    #     time = 0
    #     while total_task > 0:
            
    #         for t in range(max_times, 0, -1):
                
    #             break_flag = False
    #             for task in tasks_times[t]:
    #                 if task not in running or time - running[task] > n:
    #                     running[task] = time

    #                     tasks_times_set = tasks_times[t]
    #                     tasks_times_set.remove(task)

    #                     if t > 1:
    #                         tasks_times[t-1].add(task)

    #                     if t == max_times:
    #                         for tt in range(max_times, 0, -1):
    #                             if len(tasks_times[tt]) > 0:
    #                                 max_times = tt
    #                                 break

                        
    #                     # print(tasks_times, running)
    #                     total_task -= 1
    #                     break_flag = True
    #                     break

    #             if break_flag:
    #                 break

    #         time += 1

    #     return time