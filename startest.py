#! /usr/bin/env python
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

if __name__ == '__main__':
    """
    Test Django App in travis.ci
    """
    import django
    if hasattr(django, 'setup'):
        django.setup()
    from django.test.runner import DiscoverRunner

    failures = DiscoverRunner().run_tests(("star",), verbosity=2)
    if failures:
        sys.exit(failures)
