from celery import shared_task

@shared_task
def test_celery_task():
    print('Celery is running a test task!')
    return "Task Completed"
