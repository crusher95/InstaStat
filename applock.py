import os

default_method = 1
default_pid_file = "process.pid"


class Lock(object):
    def __init__(self, method=default_method, filename=default_pid_file, pid=None):
        self.method = method
        self.filename = filename
        if pid:
            self.pid = pid
        else:
            self.readpid()

    def isPresent(self):
        if self.method == 1:
            if self.pid:
                x = "/proc/" + str(self.pid)
                if os.path.exists(x):
                    return True
                else:
                    self.droppid()
                    return False

    def readpid(self):
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as f:
                self.pid = f.readline()
        else:
            self.pid = "000"
        return None

    def droppid(self):
        with open(self.filename, 'w') as f:
            f.write(str(os.getpid()))
        return True


if __name__ == '__main__':
    print "Read instruction on how to use"