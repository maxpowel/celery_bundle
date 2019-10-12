# Celery bundle for AppLauncher

[![Build Status](https://travis-ci.org/applauncher-team/celery_bundle.svg?branch=master)](https://travis-ci.org/applauncher-team/celery_bundle)

Celery support for applauncher

Installation
-----------
```bash
pip install celery_bundle 
```
Then add to your main.py
```python
import celery_bundle

bundle_list = [
    celery_bundle.CeleryBundle(),
]
```

Configuration
-------------
```yml
celery:
  broker: 'pyamqp://guest@localhost//'
  result_backend: 'redis://localhost:6379/1'
  worker: True
```
If you dont want a backend, just ignore the field. Set 'worker' to to True when this applauncher instance should run a worker, set it to False when 
this instance should not execute tasks.

The whole configuration options with the default values is:
```yml
celery:
    broker: 'pyamqp://guest@localhost//'
    name: ''
    result_backend: ''
    worker: True
    queues:  [celery]
    task_routes: []
    task_serializer: json
    accept_content: [json]
    result_serializer: 'json'
    result_expires: 3600 # 1 hour
    timezone: 'Europe/Madrid'
    concurrency: 0
    worker_max_tasks_per_child: -1
    broker_pool_limit: 1
    broker_heartbeat: 0 # Disabled, put some greater value if you network is not good
    broker_connection_timeout: 30
    event_queue_expires: 60
    worker_prefetch_multiplier: 1
    quiet: True
    without_gossip: True
    without_mingle: True

```

Registering tasks
-----------------
Create a file for your tasks, for example "tasks.py" (you can create any files you want always you register it later)

```python
import inject
from celery import Celery 
app = inject.instance(Celery)


@app.task
def add(x, y):
    return x + y

```

Then in your app application bundle, create the method "registe_tasks"
```python
class MyBundle(object):
    def register_tasks(self):
        import task
```
The objective is to load the tasks after the kernel (indeed just the depenency injection) is ready. This method (register_tasks)
will be called automatically by celery_bundle
