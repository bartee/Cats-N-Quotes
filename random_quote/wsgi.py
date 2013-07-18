import os
import sys
import site


def find_parent_dir(filename, path):
    for root, dirs, names in os.walk(path):
        if filename in names:
            return os.path.basename(root)
    raise Exception('File not found')


version_string = "{0}.{1}".format(sys.version_info[0], sys.version_info[1])
LOCAL_PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
VENV_PACKAGES = os.path.join(LOCAL_PROJECT_ROOT, '../venv/lib/python' + version_string + '/site-packages')

site.addsitedir(LOCAL_PROJECT_ROOT)
site.addsitedir(VENV_PACKAGES)

# Directly assign to os.environ instead of using os.environ.setdefault as the former plays nice
# with having multiple django sites run from one WSGIProcessGroup, as done on test server.
# There seems to be no use case where the DJANGO_SETTINGS_MODULE needs to be defined elsewhere.
# See comment in default Django project wsgi
os.environ["DJANGO_SETTINGS_MODULE"] = "random_quote.settings"

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

try:
    # Celery
    import newrelic.agent
    import current_site.params as params

    newrelic_ini = os.path.abspath(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), 'etc', 'newrelic', 'newrelic.ini')
    )

    if getattr(params, 'ENV', None):
        newrelic.agent.initialize(newrelic_ini, getattr(params, 'ENV', None))
        application = newrelic.agent.wsgi_application()(application)

except:
    pass



