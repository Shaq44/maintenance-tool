import logging
import psutil
 

logger=logging.getLogger("Foo")

logging.basicConfig(filename='system.log', level=logging.INFO, format='%(asctime)s %(message)s')



def systemCheck():
    cpu_percent=psutil.cpu_percent(interval=1)
    cpu_cores=psutil.cpu_count(logical=False)
    logical_process=psutil.cpu_count()
    disk_usage=psutil.disk_usage('/')
    virtual_memory=psutil.virtual_memory()

    logger.info("CPU Percent:{} ".format(cpu_percent))
    logger.info("CPU Cores:{} ".format(cpu_cores))
    logger.info("Logical Processes:{} ".format(logical_process))
    logger.info("Disk Usage:{} ".format(disk_usage))
    logger.info("Virtual Memory:{} ".format(virtual_memory))
    print("CPU Usage: {0} \nCPU Cores: {1} \nLogical Processes: {2} \nDisk Usage: {3} \nVirtual Memory: {4}".format(cpu_percent,cpu_cores,logical_process,disk_usage,virtual_memory))


systemCheck()            
