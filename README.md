# (Alfa) drf-scaffolding
Django app which allow create full APIs based on your models defined in your project

### How to use.
1.-  Install drfscaffolding following:
```bash
pip install drfscaffolding
```

2.- Add rest_framework, rest_framework_swagger and drf_scaffolding on your install apps.

We recommend you organize your installed applications as shown in the following example. Note that local applications are added in the LOCAL_APPS variable.
```python
...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    ...
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_swagger',
    'drf_scaffolding',
]

LOCAL_APPS = [
    'your_app',
    'other_local_app'
]

INSTALLED_APPS += THIRD_PARTY_APPS + LOCAL_APPS

...
```

3.- Define configurations on your models.
If you do not want to generate the API, just do not add the drf_config attribute in the Meta class.

The scaffolding attribute in 'api' is the one that defines whether an api will be generated for the model with that configuration.

The method attribute defines the http methods to be appended to the api. The you do not define this attribute will be assigned http methods:
```python
POST, GET, PATCH, DELETE
```

The serializer attribute also contains the scaffolding property to define whether you want to generate the serializers together with the api.The default value is false, so if you do not add the property the serializer will not be generated.

The fields field in serializer defines the fields that we want to be added in the serializer of the model to be used in api.If you leave this property undefined, then, only the id in the serializer will be assigned.

example:
```python
class Poll(models.Model):
    class Meta:
        drf_config = {
            'api': {
                'scaffolding': True,
                'methods': ['CREATE', 'UPDATE'] 
            },
	    'serializer': {
	        'scaffolding': True,
	        'fields': [
		    'title'
	        ]
	    }
        }

    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
```

4.- Execute django command to create apis
```bash
python manage.py createapi
python manage.py creatediscover
python manage.py createserializers
```

5.- Add apis urls generated on your urls project.
```python
urlpatterns = [
    ...
    url(r'^api/', include('api.urls', namespace="api")),
    ...
]

```

6.- Run your server
```bash
python manage.py runserver
```

7.- Now, you can check your urls in your web browser and use your api.
