# drf-scaffolding
Django app which allow create full APIs based on your models defined in your project

### How to use.
1.-  Install drfscaffolding following:
```bash
pip install pip install drfscaffolding
```

2.- Add rest_framework, rest_framework_swagger and drf_scaffolding on your install apps
```python
...

INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_swagger',
    'drf_scaffolding',
]

...
```

3.- Define configurations on your models. For example.
```python
class Poll(models.Model):
    class Meta:
        drf_config = {
            'api': {
                'scaffolding': True,
                'methods': ['CREATE', 'UPDATE'],
                'serializer': {
                    'scaffolding': True,
                    'fields': [
                        'title'
                    ]
                }
            }
        }

    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
```

4.- Execute django command to create apis
```bash
python manage.py createapi
```

5.- Add apis urls generated on your urls project.
```python
urlpatterns = [
    ...
    url(r'^api/', include('api.urls', namespace="api")),
    ...
]

```

6.- Now, you can check your urls in your web browser.
