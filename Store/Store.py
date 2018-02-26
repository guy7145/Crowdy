import subprocess,json,time
from multiprocessing.pool import Pool
import grequests
cmd = "zbarcam.exe --nodisplay"
def run():
    from subprocess import Popen, PIPE, CalledProcessError
    with Pool() as pool:
        with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
            for line in p.stdout:
                if(line == ""):
                    print("Hello")
                # print(line, end='') # process line here
                data = json.loads(line.split(":")[1])
                pool.apply_async(handle,[data])

def handle(data):
    print(data)
    grequests.get('localhost:8080/entered?data=' + data)

if __name__=="__main__":
    run()
