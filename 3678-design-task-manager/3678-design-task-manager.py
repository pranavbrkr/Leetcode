class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_info = {}
        self.heap = []
        for user_id, task_id, priority in tasks:
            self.task_info[task_id] = [priority, user_id]
            heapq.heappush(self.heap, [-priority, -task_id])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = [priority, userId]
        heapq.heappush(self.heap, [-priority, -taskId])

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_info[taskId][0] = newPriority
        heapq.heappush(self.heap, [-newPriority, -taskId])

    def rmv(self, taskId: int) -> None:
        self.task_info.pop(taskId)

    def execTop(self) -> int:
        while self.heap:
            priority, task_id = heapq.heappop(self.heap)
            priority, task_id = -priority, -task_id
            if priority == self.task_info.get(task_id, [-1, -1])[0]:
                return self.task_info.pop(task_id)[1]
        
        return -1



# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()