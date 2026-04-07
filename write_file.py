import datetime as dt

def to_do(tasks):
    file = open("output.txt", 'w')
    for task in tasks:
        ftime = task[0].strftime("%A %d %B %Y")
        file.write(f"{ftime}: {task[1]}\n")
    file.close()