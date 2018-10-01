#!/bin/python 
from cbapi.response import *
import csv

cbquery=raw_input("Enter Carbon Black Proces Query:")
filename=raw_input("Enter FileName:")
cb = CbResponseAPI()
query = cb.select(Process).where(cbquery)

with open(filename, 'wb') as csvfile:
    ProcessExport = csv.writer(csvfile, delimiter='#',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    ProcessExport.writerow(['process_md5','sensor_id','filtering_known_dlls','modload_count','parent_unique_id','emet_count','cmdline','filemod_count','id','parent_name','group','parent_id','hostname','last_update','start','comms_ip','regmod_count','interface_ip','process_pid','username','terminated','process_name','last_server_update','path','netconn_count','parent_pid','crossproc_count','segment_id','host_type','processblock_count','os_type','childproc_count','unique_id'])
    for proc in query:
		ProcessExport.writerow([proc.process_md5,proc.sensor_id,proc.filtering_known_dlls,proc.modload_count,proc.parent_unique_id,proc.emet_count,proc.cmdline,proc.filemod_count,proc.id,proc.parent_name,proc.group,proc.parent_id,proc.hostname,proc.last_update,proc.start,proc.comms_ip,proc.regmod_count,proc.interface_ip,proc.process_pid,proc.username,proc.terminated,proc.process_name,proc.last_server_update,proc.path,proc.netconn_count,proc.parent_pid,proc.crossproc_count,proc.segment_id,proc.host_type,proc.processblock_count,proc.os_type,proc.childproc_count,proc.unique_id])
