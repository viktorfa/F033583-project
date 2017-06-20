"""
WSGI config for ir_project_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from retrieval.retrieval import Retriever

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()

retriever = Retriever(scraper_output_file='hip_hop_seed_unlimited_songs.json')
