# 那么显然是开进程，读取进程输出，保存到文件这样的过程，当然，也可以加个flask和图表，这样可以从网页访问统计信息。。。
from __future__ import print_function # Only Python 2.x
import subprocess
import termios,fcntl,struct,datetime
h, _ = struct.unpack('hh', fcntl.ioctl(1, termios.TIOCGWINSZ, '1234'))
def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    i=0
    with open("log.txt",mode="a+") as f:
        for stdout_line in iter(popen.stdout.readline, ""):
            if i==2:
                dd=stdout_line.split(" ")
                f.write(f"{dd[-2]},{datetime.datetime.now()}\n")
                print(dd[-2],datetime.datetime.now())
            elif i==h-1:
                i=0
            i+=1
            pass
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)
# Example
for path in execute(["top"]):
    # print(path,end="")
    pass