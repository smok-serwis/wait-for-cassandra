# coding=UTF-8

from setuptools import setup

setup(
    keywords=['cassandra', 'ci', 'utility'],
    version="1.9_a2",
    install_requires=['cassandra-driver'],
    packages=[
        'wait_for_cassandra',
    ],
    entry_points={
        'console_scripts': [
            'wait-for-cassandra = wait_for_cassandra.run:run'
        ]
    }
)
