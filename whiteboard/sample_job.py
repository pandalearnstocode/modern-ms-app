# %%
import time

def add(x, y):
    return x + y

def sample_job(delta, x, y):
    time.sleep(delta)
    return add(x,y)

print(f"Result: {sample_job(delta = 1, x = 5, y = 9)}")
# %%
