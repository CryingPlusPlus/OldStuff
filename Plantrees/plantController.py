import subprocess, time, psutil

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

procs = [subprocess.Popen('python plantrees4.py', shell=True), subprocess.Popen('python plantrees4.py', shell=True), subprocess.Popen('python plantrees4.py', shell=True)]

while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    print('CPU: ', cpu, 'RAM: ', ram, 'Win: ', len(procs), '\n')
    if cpu < 80 and ram < 80:
        procs.append(subprocess.Popen('python plantrees4.py', shell=True))

    if cpu > 90 or ram > 90:

        kill(procs[-1].pid)
        procs.pop(-1)

    time.sleep(69)

