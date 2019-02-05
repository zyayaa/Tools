#!/usr/bin/python2

import multiprocessing
import subprocess
import os

def pinger( job_q, results_q ):
    DEVNULL = open(os.devnull,'w')
    while True:
        ip = job_q.get()
        if ip is None: break

        try:
            subprocess.check_call(['ping','-c1',ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
            print(ip)
        except:
            pass

if __name__ == '__main__':
    pool_size = 255

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [ multiprocessing.Process(target=pinger, args=(jobs,results))
             for i in range(pool_size) ]

    for p in pool:
        p.start()
<<<<<<< HEAD
    
    for x in range(0, 3):
        for i in range(1,pool_size):
            jobs.put('172.16.{0}.{1}'.format(x,i))
||||||| merged common ancestors

    for i in range(1,255):
        jobs.put('155.133.194.{0}'.format(i))
=======

    for i in range(1,255):
        jobs.put('192.168.0.{0}'.format(i))
>>>>>>> d22b645db8ae9314c35d6b37b92187f97b93531b

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()
