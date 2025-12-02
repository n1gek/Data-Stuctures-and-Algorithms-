class Logger:
    def __init__(self):
        self.tracker = {}  # message -> last printed timestamp

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.tracker:
            last = self.tracker[message]
        else:
            last = None
            
        if last is None or timestamp - last >= 10:
            self.tracker[message] = timestamp
            return True
        return False