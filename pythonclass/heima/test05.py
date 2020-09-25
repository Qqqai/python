class Time:
    def __init__(self, hour, minute, secound):
        self.hour = hour
        self.minute = minute
        self.secound = secound

    def show(self):
        print("当前时间%d:%d:%d" % (self.hour, self.minute, self.secound))

    @classmethod
    def str_to_time(cls, str):
        hour, minute, secound = [int(x) for x in str.split("-")]
        t = cls(hour, minute, secound)
        return t

