from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='celery_bundle',
    packages=['celery_bundle'],
    version='1.24',
    description='Celery support for applauncher',
    author='Alvaro Garcia Gomez',
    author_email='maxpowel@gmail.com',
    url='https://github.com/applauncher-team/celery_bundle',
    download_url='https://github.com/applauncher-team/celery_bundle',
    keywords=['celery'],
    classifiers=['Topic :: Adaptive Technologies', 'Topic :: Software Development', 'Topic :: System', 'Topic :: Utilities'],
    install_requires=install_requires
)
