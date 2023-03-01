import threading
import random
import time
import statistics

def random_array(length, start, end):
    random_list = []
    for i in range(0, length):
        n = random.randint(start, end)
        random_list.append(n)
    return random_list


def thread_function(numArray, N):
    sum(numArray[0:N])
    return


if __name__ == "__main__":
    random.seed(42)
    maxN = 1000
    numArray = random_array(maxN, 1, 1000)
    time_samples = []
    for i in range(1, 1000):
        start_time = time.time()
        N = random.randint(2, 999)
        thread_handle = threading.Thread(target=thread_function, args=(numArray, N))
        thread_handle.start()
        thread_handle.join()
        # thread_function(numArray,N) # for experiment without creating a thread
        end_time = time.time()
        time_samples.append(end_time - start_time)

    mean = statistics.fmean(time_samples) * 1000
    std_dev = statistics.stdev(time_samples) * 1000
    minimum = min(time_samples) * 1000
    maximum = max(time_samples) * 1000

    print(f"statistics summary:\nmean: {mean}ms\nstandard deviation: {std_dev}ms\nminimum: {minimum}ms\nmaximum: {maximum}ms")
