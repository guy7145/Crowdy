import json
from Data.http import fetch_url
cmd = "zbarcam.exe --nodisplay"


def handle(data,host):
    print(json.dumps(data))
    store="Castro"
    query = 'http://{}:8080/scannedQR?store={}&id={id}&creation_date={creation_date}'.format(host, store, **data)
    print(query)
    print(fetch_url(query))


def run(host):
    from subprocess import Popen, PIPE, CalledProcessError
    # with Pool() as pool:
    with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            if(line == ""):
                continue
            data = json.loads(line[line.find(":")+1:])
            # pool.apply_async(handle,[data])
            handle(data,host)


def start_store(host):
    run(host)
    return
