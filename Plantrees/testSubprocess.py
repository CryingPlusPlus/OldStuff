import subprocess, time, psutil

# p = subprocess.Popen('exec python cpuTest.py', shell=True)

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

procs = [subprocess.Popen('python cpuTest.py', shell=True)]

time.sleep(5)
kill(procs[0].pid)
