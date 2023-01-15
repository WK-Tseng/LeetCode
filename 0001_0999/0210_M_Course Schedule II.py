class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        unlock = collections.defaultdict(list)
        for a, b in prerequisites:
            unlock[b].append(a)

        prerequisites_counter = {i:0 for i in range(numCourses)}
        for a, _ in prerequisites:
            prerequisites_counter[a] += 1

        result = []

        remove_flag = True
        while remove_flag:
            remove_flag = False
            remove_course = []
            for course, counter in prerequisites_counter.items():
                if counter == 0:
                    remove_flag = True

                    result.append(course)
                    for unlock_course in unlock[course]:
                        prerequisites_counter[unlock_course] -= 1

                    remove_course.append(course)
            
            for course in remove_course:
                prerequisites_counter.pop(course)


        if len(prerequisites_counter) > 0:
            result = []

        return result