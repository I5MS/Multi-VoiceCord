from subprocess import Popen
from time import sleep

# Variables to hold references to the running processes
processes = []

while True:
    # Terminate old processes
    for process in processes:
        process.terminate()

    # Clear the list of old processes
    processes.clear()

    # Start bot1.py
    process1 = Popen(['python', 'app1.py'])
    processes.append(process1)

    # Start app2.py
    process2 = Popen(['python', 'app2.py'])
    processes.append(process2)

    # Start app3.py
    process3 = Popen(['python', 'app3.py'])
    processes.append(process3)

    # Start app4.py
    process4 = Popen(['python', 'app4.py'])
    processes.append(process4)

    # Wait for 6 Hours before restarting the processes
    sleep(21600)
