import time

def longTask2(task_id):
    data = []
    data.append(f"Starting task processing (MultiProcessing): {task_id}")
    time.sleep(5)
    data.append(f"Completed task processing (MultiProcessing): {task_id}")
    return data