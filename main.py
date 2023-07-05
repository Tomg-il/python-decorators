# This is a sample code for using Python decoders. to allow wrapper of common functionality to
# functions

import time


def speed_calc_decorator(function):
    """ this decorator calculate function execution time and print the function name and result
    to the console """
    def wrapper_function():
        start_ts = time.time()
        function()
        end_ts = time.time()

        print(f"{function.__name__} run speed: {end_ts - start_ts}")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    time.sleep(1)
    return


@speed_calc_decorator
def slow_function():
    time.sleep(3)
    return 0


if __name__ == '__main__':
    fast_function()
    slow_function()
