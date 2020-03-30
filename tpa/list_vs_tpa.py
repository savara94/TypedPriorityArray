from src.stefan.typed_priority_array import TypedPriorityArray
import time

maximum = 70000
data = range(maximum)

collection = list(data)
#collection = TypedPriorityArray(*data)
times = []

print("Started testing for {}".format(type(collection)))
start = time.time()
for x in range(maximum + 1000):
    query_time = time.time()
    x in collection
    times.append(time.time() - query_time)

print('Average time {}'.format(sum(times) / len(times)))
print('Total time {}'.format(time.time() - start))