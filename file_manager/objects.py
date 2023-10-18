class MinificationLog(object):
    def __init__(
            self,
            memory_usage: float = None,
            time_taken: float = None,
            ):

        self.memory_usage = memory_usage
        self.time_taken = time_taken

    def to_dict(self):
        return {
            "memory_usage": self.memory_usage,
            "time_taken": self.time_taken
        }
