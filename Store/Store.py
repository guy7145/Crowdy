import subprocess,json,time,sys
from multiprocessing.pool import Pool
from Data.http import fetch_url
cmd = "zbarcam.exe --nodisplay"

def handle(data):
    print(data)
    global host
    fetch_url(host + ':8080/scannedQR?data=' + data)

def run():
    from subprocess import Popen, PIPE, CalledProcessError
    # with Pool() as pool:
    with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            if(line == ""):
                continue
            data = json.loads(line[line.find(":")+1:])
            # pool.apply_async(handle,[data])
            handle(data)


if __name__=="__main__":
    global host
    host=sys.argv[1]
    run()
