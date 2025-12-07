class Logger:
    def __init__(self):
        self.tracker = {}  # message -> last printed timestamp

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.tracker:
            self.tracker[message] = timestamp
            return True
        else:
            time = self.tracker[message]
            
            if timestamp - time >= 10:
                self.tracker[message] = timestamp
                return True
            return False
            