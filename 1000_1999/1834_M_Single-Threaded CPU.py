class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        tasks.sort(key=lambda x : (x[0], x[1]))

        tasks_len = len(tasks)
        
        idx = 0
        time = 0
        busy = 0
        task_dict = {}
        result = []
        task_dict_keys = []
        while idx < tasks_len:
            next_time = tasks[idx][0]
            diff_time = next_time - time

            if busy == 0:
                time = next_time
            elif diff_time >= busy:
                time += busy
                busy = 0
            else:
                busy -= (next_time - time)
                time = next_time


            while idx < tasks_len and tasks[idx][0] == time:
                _, process_time, this_idx = tasks[idx]
                temp_idx_list = task_dict.get(process_time, [])

                if len(temp_idx_list) == 0:
                    heappush(task_dict_keys, process_time)

                heappush(temp_idx_list, this_idx)
                task_dict[process_time] = temp_idx_list
                idx += 1

            if busy <= 0 and len(task_dict) > 0:
                min_time = nsmallest(1, task_dict_keys)[0]
                min_idx = heappop(task_dict[min_time])
                busy = min_time
                result.append(min_idx)

                if len(task_dict[min_time]) == 0:
                    task_dict.pop(min_time)
                    heappop(task_dict_keys)

        for min_time in nsmallest(len(task_dict_keys), task_dict_keys):
            temp_idx_list = task_dict[min_time]
            result.extend(nsmallest(len(temp_idx_list), temp_idx_list))

        return result