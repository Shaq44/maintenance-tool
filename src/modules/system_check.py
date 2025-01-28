import logging
import psutil
import sched
import time 

logger=logging.getLogger("Foo")

logging.basicConfig(filename='system.log', level=logging.INFO)



def systemCheck():
    cpu_percent=psutil.cpu_percent(interval=1)
    cpu_cores=psutil.cpu_count(logical=False)
    logical_process=psutil.cpu_count()


    logger.info("CPU Percent:{} ".format(cpu_percent))
    logger.info("CPU Cores:{} ".format(cpu_cores))
    logger.info("Logical Processes:{} ".format(logical_process))
    print("CPU Usage: {0} \nCPU Cores: {1} \nLogical Processes: {2}".format(cpu_percent,cpu_cores,logical_process))


systemCheck()            
