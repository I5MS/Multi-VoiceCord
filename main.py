from subprocess import Popen
from time import sleep

scripts = ['app1.py', 'app2.py', 'app3.py', 'app4.py']
processes = []

while True:
    for p in processes:
        p.terminate()
    processes = [Popen(['python', s]) for s in scripts]
    sleep(21600)
