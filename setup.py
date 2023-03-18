from setuptools import setup

setup(
    name='myflaskapp',
    packages=['myflaskapp'],
    version='0.1',
    description='A simple Flask app',
    author='Avijit Sen',
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    entry_points={
        'console_scripts': [
            'myflaskapp=myflaskapp.app:run',
        ],
    }
)