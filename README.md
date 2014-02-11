celery_djange_example
=====================

Integrate celery into django framework, using backend.

##contents
this is a demo to show how you can use celery within django project.

###prereqs

1.install broker(I choose rabitmq)

	$ sudo apt-get install rabbitmq-server (in ubuntu)  
	$ brew install rabbitmq (in mac os)  

2.install celery  
	
	$ pip install celery

###deploy

1. create celery.py in celeryProj/celery.py  
	`from __future__ import absolute_import`
2. startapp(demo)
3. create tasks.py in demo/tasks.py
4. register app in settings
5. check status by using backend of database(celerytest_010), rabbitmq(celerytest_011)
7. finish your own stuff

###start

1.start worker  
	
	$ celery -A `celeryProj` worker -l info

2.start your project  
	
	runserver

###screenshot
1. using database as backend
![](https://raw2.github.com/jionghuming/docs/master/pic/celery_example/database_celery_result.png)
2. using amqp as backend
![](https://raw2.github.com/jionghuming/docs/master/pic/celery_example/amqp_celery_result.png)



##参考
1. [first-steps-with-django](http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)  
2. [conf-amqp-result-backend](http://docs.celeryproject.org/en/latest/configuration.html#conf-amqp-result-backend)