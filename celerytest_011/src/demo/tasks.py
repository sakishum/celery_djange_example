'''
Created on Feb 11, 2014

@author: joest
'''

from celery import task

@task
def add(x, y):
    return x+y