import time

current_time = time.time()

print(current_time)  # Seconds since january 1st, 1970.

# Write your code below.


def speed_calc_decorator(function):
    def speed_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return speed_function()


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        x = i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        x = i * i
