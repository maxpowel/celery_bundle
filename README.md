# Celery bundle for AppLauncher

[![Build Status](https://travis-ci.org/applauncher-team/celery_bundle.svg?branch=master)](https://travis-ci.org/applauncher-team/celery_bundle)

Celery support for applauncher

Installation
-----------
```bash
pip install celery-bundle 
```
Then add to your main.py
```python
from applauncher import Kernel
from celery_bundle.bundle import CeleryBundle

with Kernel(bundles=[CeleryBundle()], environment="PROD") as kernel:
    CeleryBundle.start()
    kernel.wait()

```

Configuration
-------------
```yml
celery:
  broker_url: 'pyamqp://guest@localhost//'
  result_backend: 'redis://localhost:6379/1'
  worker: true
  task_queues:
    - my_queue
    - other_cue
  include:
    - 'my_package.tasks'
```
If you dont want a backend, just ignore the field. Set 'worker' to True when this applauncher instance should run a worker, set it to False when 
this instance should not execute tasks.

Registering tasks
-----------------
Create a file for your tasks, for example "tasks.py"

```python
from applauncher import ServiceContainer
# Inject the celery application
app = ServiceContainer.celery.app()

@app.task
def add(x, y):
    return x + y
```
And then add it to the configuration (`include` field) providing the whole path (this path will be imported by celery)

Another option to register your tasks is by injecting and modifying the celery configuration. This method is useful
when you want to get automatically registered your tasks, or you just want a cleaner config file.

```python
from applauncher import ServiceContainer
from applauncher.event import ConfigurationReadyEvent

class MyBundle:
    def __init__(self):
        # First we subscribe to the configuration ready event
        self.event_listeners = [
            (ConfigurationReadyEvent, self.configuration_ready)
        ]

    def configuration_ready(self, event):
        # Now we modify the celery config by appending my tasks path
        # This works because a this point the injector is not configured yet
        ServiceContainer.configuration().celery.include.append('my_bundle.tasks')
```
