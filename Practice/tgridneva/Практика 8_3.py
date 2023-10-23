import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print(f"Execution time: {execution_time} seconds")

with Timer():
    time.sleep(2)
