import time
import psutil


def get_system_metrics():
    return {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent
    }


def measure_inference_time(func, *args, **kwargs):

    start = time.time()

    result = func(*args, **kwargs)

    end = time.time()

    return {
        "result": result,
        "latency_seconds": round(end - start, 4)
    }