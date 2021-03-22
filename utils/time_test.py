import time

def time_test(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result=func(*args,**kwargs)
        end = time.time()
        print("%s the spent time is %s secs" % (func.__name__,end-start))
        return result
    return wrapper