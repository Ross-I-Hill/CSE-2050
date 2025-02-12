import random
import time

def generate_lists(size):
    '''
    takes in the argument size and generates two lists that are the size 
    of the given size argument, then returns the two lists in a tuple 
    '''
    L1 = random.sample(range(size*2), size)
    L2 = random.sample(range(size*2), size)
    return L1, L2 

def find_common(list1, list2):
    '''
    using two lists as arguments, generates a list common_num and then compares each term in
    the first list to each term in the second list, adding the similar numbers to common_num
    finally returning the length of common_num
    '''
    common_num = []                    # 1
    for i in list1:                    #   n*
        for j in list2:                #      n*
            if i == j:                 #         1*
                common_num.append(j)   #            1
    return len(common_num)                  # + 1
                                       # 1 + n(n(1)) + 1 = n^2 + 2  = O(n^2)

def find_common_efficient(list1, list2):
    '''
    using two lists as arguments, turns both lists into sets and then uses
    the intersect function of sets to get a set of the common numbers of 
    both lists, then returns the length of the intersection set
    '''
    L1 = set(list1)
    L2 = set(list2)
    intersection = L1.intersection(L2)
    return len(intersection)

    
def measure_time():
    '''
    using the list sizes, which has the five sizes to check the run time, 
    we run the functions at each size at save the time to a list, so that
    when the data can be printed all of the info can be indexed out of a list
    '''
    sizes = [10, 100, 1000, 10000, 20000]
    com_times = []
    for i in sizes:
        start = time.time()
        find_common(*generate_lists(i))
        end = time.time()
        com_times.append(end - start)
    
    com_times_efficent = []
    for i in sizes:
        start = time.time()
        find_common_efficient(*generate_lists(i))
        end = time.time()
        com_times_efficent.append(end - start)

    print(f' List Size   find_common Time (s)    find_common_efficent Time (s)')
    print(f' ---------   --------------------    -----------------------------')
    print(f'     {sizes[0]:.2f}         {com_times[0]:.2f}                  {com_times_efficent[0]:.2f}')
    print(f'     {sizes[1]:.2f}        {com_times[1]:.2f}                  {com_times_efficent[1]:.2f}')
    print(f'     {sizes[2]:.2f}       {com_times[2]:.2f}                  {com_times_efficent[2]:.2f}')
    print(f'     {sizes[3]:.2f}      {com_times[3]:.2f}                  {com_times_efficent[3]:.2f}')
    print(f'     {sizes[4]:.2f}      {com_times[4]:.2f}                  {com_times_efficent[4]:.2f}')
   



if __name__ == "__main__":
   measure_time()