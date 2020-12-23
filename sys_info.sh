#!/usr/bin/env sh

MEMINFO=$(grep 'MemTotal\|MemFree\|SwapTotal\|SwapFree\|SwapCached' /proc/meminfo)
UPTIME=$(uptime | grep -oe 'up .*' | sed 's/,//g' | awk -F  ' ' '{print $2}')
LOADAVERAGE=$(uptime | grep -oe 'load average.*' | awk -F ':' '{print $2}')
CPU_USAGE=$(top -b n1 | grep "Cpu" | awk -F ' ' '{ print "\nUser Cpu time: " $2,
                                                         "\nSystem CPU Time: " $4,
                                                         "\nNice time: " $6,
                                                         "\nIdle CPU Time: " $8,
                                                         "\nio wait cpu time: " $10,
                                                         "\nHardware irq: " $12,
                                                         "\nSoftware irq: " $14,
                                                         "\nSteal time: "$16}')

if [ -z $1 ]; then
  echo "All info: CPU,Memory,Uptime,Loadaverage"
  echo -e "MemInfo:\n$MEMINFO \nUptime:\n$UPTIME \nLoadaverage:\n$LOADAVERAGE \nCPU usage:$CPU_USAGE"
fi

case "$1" in
 "cpu") echo -e "CPU usage:$CPU_USAGE";;
 "memory") echo -e "MemInfo:$MEMINFO";;
 "-h" | "--help" | "help") echo "Available options: memory, cpu.";;
 *) echo "Available options: cpu, memory";;
esac