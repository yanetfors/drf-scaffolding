# -*- coding: utf-8 -*-
import os

from django.apps import apps
from django.conf import settings as dj_settings
from django.core.management import BaseCommand
from django.template import Context, Template

from . import settings, templates


class Command(BaseCommand):
    help = "Create autodiscover to add api urls to project."

    can_import_settings = True
    requires_system_checks = False

    def write(self, msg):
        self.stderr.write(msg)

    def join_label_app(self, label, app, is_py_file=True):
        extension = '.py' if is_py_file else ''
        return '{0}/{1}{2}'.format(label, app, extension)

    def file_exists(self, path):
        return os.path.isfile(path)

    def create_file(self, path, context=None, template=None):
        if not self.file_exists(path):
            with open(path, 'w') as f:
                msg = self.join_label_app(
                    'Writing: ', path, is_py_file=False)
                self.write(msg)
                if not context:
                    context = Context()

                if not template:
                    template = ''

                template_loaded = Template(template)
                api_text = template_loaded.render(context)
                f.write(api_text)

    def create_init_file(self, path):
        url = self.join_label_app(path, '__init__')
        self.create_file(url)

    def get_or_create_file(self, path, context=None, template=None):
        if not self.file_exists(path):
            self.create_file(path, context, template)

    def dir_exists(self, path):
        return os.path.isdir(path)

    def create_dir(self, path):
        return os.makedirs(path)

    def get_or_create_dir(self, path):
        if not self.dir_exists(path):
            return self.create_dir(path)
        else:
            return True

    def create_api_files(self, api_uri):
        autodiscover_path = self.join_label_app(api_uri, 'autodiscover')
        api_urls_path = self.join_label_app(api_uri, 'urls')

        #
        # Create init file into api folder
        #
        self.create_init_file(api_uri)

        #
        # Create autodiscover file into api folder
        #
        context = Context({
            'apps': [],
        })
        self.get_or_create_file(
            autodiscover_path,
            context=context,
            template=templates.AUTODISCOVER_TEMPLATE
        )

        #
        # create urls file into api folder
        #
        self.get_or_create_file(
            api_urls_path,
            template=templates.API_URLS_TEMPLATE
        )

    def create_api_version_files(self, api_uri):
        api_version_urls_path = self.join_label_app(api_uri, 'urls')
        api_router_path = self.join_label_app(api_uri, 'routers')

        #
        # Create init file into api/v1 folder
        #
        self.create_init_file(api_uri)

        #
        # Create urls file into api/v1 folder
        #
        self.get_or_create_file(
            api_version_urls_path,
            template=templates.API_V1_URLS_TEMPLATE
        )

        #
        # Create routers file into api/v1 folder
        #
        self.get_or_create_file(
            api_router_path,
            template=templates.ROUTER_TEMPLATE
        )

    def create_api_folder(self, project_path, version):
        api_url = 'api'
        api_version_url = self.join_label_app(api_url, 'v1', False)

        #
        # first, create api directories
        #
        self.get_or_create_dir(api_url)
        self.get_or_create_dir(api_version_url)

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
