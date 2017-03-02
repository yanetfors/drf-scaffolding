# -*- coding: utf-8 -*-
API_TEMPLATE = '''# -*- coding: utf-8 -*-
from drf_scaffolding.management.core.api import mixins
from drf_scaffolding.management.core.api.viewsets import GenericViewSet

from {{app_name}}.serializers import {{model.name|lower}} as serializers
from {{app_name}}.models import {{model.name}}


class {{model.name}}ViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.PartialUpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    serializer_class = serializers.{{model.name}}Serializer
    list_serializer_class = serializers.{{model.name}}Serializer
    retrieve_serializer_class = serializers.{{model.name}}Serializer
    create_serializer_class = serializers.{{model.name}}Serializer
    update_serializer_class = serializers.{{model.name}}Serializer

    permission_classes = []  # put your custom permissions here

    def create(self, request, *args, **kwargs):
        """
        Allows create a {{model.name}} in {{project_name}}.
        ---
        request_serializer: serializers.{{model.name}}Serializer
        response_serializer: serializers.{{model.name}}Serializer
        responseMessages:
            - code: 201
                message: CREATED
            - code: 400
                message: BAD REQUEST
            - code: 403
                message: FORBIDDEN
            - code: 500
                message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        return super({{model.name}}ViewSet, self).create(
            request, *args, **kwargs
        )

    def list(self, request, *args, **kwargs):
        """
        Returns a list of {{project_name}} {{model.name}}.
        ---
        response_serializer: serializers.{{model.name}}Serializer
        responseMessages:
            - code: 200
              message: OK
            - code: 404
              message: NOT FOUND
            - code: 500
              message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        return super({{model.name}}ViewSet, self).list(
            request, *args, **kwargs
        )

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieves information about a {{project_name}} {{model.name}}.
        ---
        response_serializer: serializers.{{model.name}}Serializer
        responseMessages:
            - code: 200
              message: OK
            - code: 403
              message: FORBIDDEN
            - code: 404
              message: NOT FOUND
            - code: 500
              message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        return super({{model.name}}ViewSet, self).retrieve(
            request, *args, **kwargs
        )

    def partial_update(self, request, pk=None):
        """
        Updates a {{model.name}}.
        ---
        request_serializer: serializers.{{model.name}}Serializer
        response_serializer: serializers.{{model.name}}Serializer
        responseMessages:
            - code: 200
              message: OK
            - code: 400
              message: BAD REQUEST
            - code: 403
              message: FORBIDDEN
            - code: 404
              message: NOT FOUND
            - code: 500
              message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        return super({{model.name}}ViewSet, self).partial_update(request)

    def destroy(self, request, pk=None):
        """
        Deletes a {{model.name}}.
        ---
        responseMessages:
            - code: 204
              message: NO CONTENT
            - code: 400
              message: BAD REQUEST
            - code: 403
              message: FORBIDDEN
            - code: 404
              message: NOT FOUND
            - code: 500
              message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        return super({{model.name}}ViewSet, self).destroy(request)

    def get_queryset(self, *args, **kwargs):
        queryset = {{model.name}}.objects.all()
        return queryset
'''

ROUTE_TEMPLATE = '''# -*- coding: utf-8 -*-
from .viewsets import (
    {%for model in models%}{{model.name|lower}},{% if not forloop.last %}\n    {%endif%}{%endfor%}
)
from api.v{{api_version}}.routers import router


{% for model in models %}router.register(
    r"{{model.name|lower}}s",
    {{model.name|lower}}.{{model.name}}ViewSet,
    base_name="{{model.name|lower}}s",
){% if not forloop.last %}\n\n{%endif%}{% endfor %}
'''

SERIALIZER_TEMPLATE = '''# -*- coding: utf-8 -*-
from drf_scaffolding.management.core.api.serializers import ModelSerializer

from {{app_name}}.models import {{model.name}}


class {{model.name}}Serializer(ModelSerializer):

    class Meta:
        model = {{model.name}}
        fields = ({%if model.fields%}{%for field in model.fields%}
            '{{field}}',{%endfor%}{%else%}
            'id',{%endif%}
        )
'''

ROUTER_TEMPLATE = '''# -*- coding: utf-8 -*-
from drf_scaffolding.management.core.api.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
'''

API_V1_URLS_TEMPLATE = '''# -*- coding: utf-8 -*-
from .routers import router
from ..autodiscover import autodiscover


autodiscover()

urlpatterns = router.urls
'''

API_URLS_TEMPLATE = '''# -*- coding: utf-8 -*-
from django.conf.urls import include, url


urlpatterns = [
    url(
        r'^v1/', include('api.v1.urls', namespace='v1')
    ),
]
'''

AUTODISCOVER_TEMPLATE = '''# -*- coding: utf-8 -*-


def autodiscover():
    """
    Perform an autodiscover of an viewsets.py file in the installed apps to
    generate the routes of the registered viewsets.
    """
    {% for app in apps %}from {{app}} import routes  # noqa{% if not forloop.last %}\n{%endif%}{% endfor %}
'''
