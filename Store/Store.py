import subprocess,json,time,sys
from multiprocessing.pool import Pool
import grequests
cmd = "zbarcam.exe --nodisplay"
def run(host):
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
    grequests.get(host + ':8080/scannedQR?data=' + data)


def start_store():
    run(sys.argv[0])
    return
