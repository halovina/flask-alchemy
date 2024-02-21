from  .. import celery

@celery.task
def print_messages(str_message):
    print("========")
    print(str_message)
    print("========")