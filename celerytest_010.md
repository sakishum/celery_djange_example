example1
===


按照参考中的步骤部署，关键步骤  

	1.安装django-celery
		$ pip install django-celery
	2.在celery.py中添加
	app.conf.update(
    	CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
    )
    3.检查数据库表celery_taskmete,django中访问TaskMeta模型
    	from djcelery.models import 


##参考
[first-steps-with-django](http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)