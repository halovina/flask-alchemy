from .. import celery

@celery.task
def print_message(str_msg):
    print("=========")
    print(str_msg)
    print("=========")