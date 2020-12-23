##  General Info
Scripts for monitoring system resources (memory and cpu)
* sysinfo.py  
* sys_info.sh
#### Basic Information
For better understand output from script , we should know next:

##### Memory
* **total:** total physical memory (exclusive swap).
* **available:** the memory that can be given instantly to processes without the system going into swap.
* **used:** memory used, calculated differently depending on the platform and designed for informational purposes only. total - free does not necessarily match used.
* **free:** memory not being used at all (zeroed) that is readily available; note that this doesn’t reflect the actual memory available (use available instead). total -  used does not necessarily match free.
* **active (UNIX):** memory currently in use or very recently used, and so it is in RAM.
* **inactive (UNIX):** memory that is marked as not used.
* **buffers (Linux, BSD):** cache for things like file system metadata.
* **cached (Linux, BSD):** cache for various things.
* **shared (Linux, BSD):** memory that may be simultaneously accessed by multiple processes.
* **slab (Linux):** in-kernel data structures cache.
* **wired (BSD, macOS):** memory that is marked to always stay in RAM. It is never moved to disk.
##### CPU 
* **user:** time spent by normal processes executing in user mode; on Linux this also includes guest time
* **system:** time spent by processes executing in kernel mode
* **idle:** time spent doing nothing
* **nice (UNIX):** time spent by niced (prioritized) processes executing in user mode; on Linux this also includes guest_nice time
* **iowait (Linux):** time spent waiting for I/O to complete. This is not accounted in idle time counter.
* **irq (Linux, BSD):** time spent for servicing hardware interrupts
* **softirq (Linux):** time spent for servicing software interrupts
* **steal (Linux 2.6.11+):** time spent by other operating systems running in a virtualized environment
* **guest (Linux 2.6.24+):** time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
* **guest_nice (Linux 3.2.0+):** time spent running a niced guest (virtual CPU for guest operating systems under the control of the Linux kernel)
##### SWAP
* **total:** total swap memory in bytes
* **used:** used swap memory in bytes
* **free:** free swap memory in bytes
* **percent:** the percentage usage calculated as (total - available) / total * 100
* **sin:** the number of bytes the system has swapped in from disk (cumulative)
* **sout:** the number of bytes the system has swapped out from disk (cumulative)

#### Technologies
* python3+
* bash
* linux

#### Setup
* **python**
```
$ sudo apt-get install gcc python3-dev
$ sudo pip3 install psutil
```
```
$ ptython3 sysinfo.py -h
```
```
$ ptython3 sysinfo.py -o cpu
```
```
$ ptython3 sysinfo.py --option memory
```
* **bash**
```
$ bash sys_info.sh -h
```
```
$ bash sys_info.sh cpu
```
```
$ bash sys_info.sh memory
```
