生产：

```shell
python manage.py collectstatic
```

测试：

```shell
celery -A cad_server worker -l info -B
```
