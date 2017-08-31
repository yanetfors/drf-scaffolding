# -*- coding: utf-8 -*-
from django.conf import settings as dj_settings
from django.core.management import BaseCommand
from django.template import Context

from . import settings, templates
from .utils import (
    create_init_file,
    get_or_create_dir,
    get_or_create_file,
    join_label_app
)


class Command(BaseCommand):
    help = "Create autodiscover to add api urls to project."

    can_import_settings = True
    requires_system_checks = False

    def create_api_files(self, api_uri):
        autodiscover_path = join_label_app(api_uri, 'autodiscover')
        api_urls_path = join_label_app(api_uri, 'urls')

        #
        # Create init file into api folder
        #
        create_init_file(api_uri)

        #
        # Create autodiscover file into api folder
        #
        context = Context({
            'apps': [],
        })
        get_or_create_file(
            autodiscover_path,
            context=context,
            template=templates.AUTODISCOVER_TEMPLATE
        )

        #
        # create urls file into api folder
        #
        get_or_create_file(
            api_urls_path,
            template=templates.API_URLS_TEMPLATE
        )

    def create_api_version_files(self, api_uri):
        api_version_urls_path = join_label_app(api_uri, 'urls')
        api_router_path = join_label_app(api_uri, 'routers')

        #
        # Create init file into api/v1 folder
        #
        create_init_file(api_uri)

        #
        # Create urls file into api/v1 folder
        #
        get_or_create_file(
            api_version_urls_path,
            template=templates.API_V1_URLS_TEMPLATE
        )

        #
        # Create routers file into api/v1 folder
        #
        get_or_create_file(
            api_router_path,
            template=templates.ROUTER_TEMPLATE
        )

    def create_api_folder(self, project_path, version):
        api_url = 'api'
        api_version_url = join_label_app(api_url, 'v1', False)

        #
        # first, create api directories
        #
        get_or_create_dir(api_url)
        get_or_create_dir(api_version_url)

        #
        # second, create files
        #
        self.create_api_files(api_url)
        self.create_api_version_files(api_version_url)
        return True

    def handle(self, *app_labels, **options):
        PROJECT_NAME = dj_settings.BASE_DIR.split('/')[-1]
        API_VERSION = settings.DRF_SETTINGS['version']

        self.create_api_folder(PROJECT_NAME, API_VERSION)
