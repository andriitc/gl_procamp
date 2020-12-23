import psutil
import argparse

arguments = argparse.ArgumentParser(description="Show info about memory and cpu")

arguments.add_argument('--option', '-o', default="all",
                       help="This argument is using to take status of Memory on machine. "
                            "Available options: memory, cpu."
                            "Use --option or -o. Without options script returns memory and cpu info ")

args = arguments.parse_args()

list_of_names_element_in_cpu_time = ['user:', 'nice:', 'system:', 'idle:', 'iowait:', 'irq:', 'softirq:', 'steal:',
                                     'guest:', 'guest_nice:']
list_of_names_element_in_memory = ['total:', 'available:', 'percent:', 'used:', 'free:', 'active:', 'inactive:',
                                   'buffers:', 'cached:', 'shared:', 'slab:']
list_of_names_element_in_swap_memory = ['total:', 'used:', 'free:', 'percent:', 'sin:', 'sout:']


def cpu_info():
    """
    Generates CPU info
    """
    cpu_time = list(psutil.cpu_times())
    result_cpu_time = dict(zip(list_of_names_element_in_cpu_time, cpu_time))
    print("=== System CPU times ===")
    for key, value in result_cpu_time.items():
        print(key, value)


def memory_info():
    """
    Generates Memory info
    """
    virtual_memory = list(psutil.virtual_memory())
    swap_memory = list(psutil.swap_memory())
    result_virtual_memory = dict(zip(list_of_names_element_in_memory, virtual_memory))
    result_swap_memory = dict(zip(list_of_names_element_in_swap_memory, swap_memory))
    print("=== Memory statistics ===")
    for key, value in result_virtual_memory.items():
        print(key, value)
    print("\n === Swap memory statistics ===")
    for key, value in result_swap_memory.items():
        print(key, value)


def result(option):
    """
    Depends on option generate CPU or Memory info
    :param option: command line argument
    """
    if option == "memory":
        memory_info()
    elif option == "cpu":
        cpu_info()
    elif option == "all":
        memory_info()
        cpu_info()
    else:
        print("Available options: memory, cpu")


if __name__ == "__main__":
    result(args.option)
