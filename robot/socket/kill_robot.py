import os

if __name__ == '__main__':
    fin = open('run.pid', 'r')
    pids = []
    for line in fin:
        pids.append(line.strip())
    for pid in pids:
        cmd = 'kill ' + pid
        os.system(cmd)