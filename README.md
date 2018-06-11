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
  debug: False
  worker: True
```
If you dont want a backend, just ignore the field. By default, debug mode is disable so you only to specify it if you want to
enable it. The option 'worker' is useful when you want only clients that create tasks and only workers that execute tasks

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
