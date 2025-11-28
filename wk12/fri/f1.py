class Task:
    def __init__(self, name, duration, priority):
        self._allowed_priorities = ["low", "med", "high"]
        self.name = name
        # self._duration = duration
        # self._priority = priority
        self.set_priority(priority)
        self.set_duration(duration)
    def get_duration(self): return self._duration
    def set_duration(self, duration):
        if isinstance(duration, int) and duration >=0 and duration <=180:
            self._duration = duration
    def get_priority(self): return self._priority
    def set_priority(self, priority):
        if isinstance(priority, str) and priority.lower() in self._allowed_priorities:
            self._priority = priority

class FreeTime:
    def __init__(self):
        self._free_time_by_dow = dict()
        self.foo = "bar"
        
    def get_free_time(self, dow): 
        if not isinstance(dow, str): 
            return None
        
        return self._free_time_by_dow[dow] if dow in self._free_time_by_dow.keys() else 0
    
    def set_free_time(self, dow, time): 
        if isinstance(dow, str) and isinstance(time, int):
            self._free_time_by_dow[dow] = time

    def use_free_time(self, dow, time_used): 
        if isinstance(dow, str) and isinstance(time_used, int):
            time_available = self._free_time_by_dow[dow]
            if time_available - time_used >= 0:
                self._free_time_by_dow[dow] -= time_used
                return True
        return False

ft = FreeTime()
ft.set_free_time("fri", 300)
ft.set_free_time("sat", 60)
ft.set_free_time("sun", 120)

print(ft.get_free_time("fri"))  # 300

ft.use_free_time("fri", 120)

print(ft.get_free_time("fri"))  # 180

print("*" * 20)

t1 = Task(name="Lab Exercise", priority="med", duration=60)
print(t1.get_duration())
print(t1.get_priority())
