#!/usr/bin/env python

from setuptools import setup

REQUIRES = ['Django <= 1.4',
            'python-fedora',
            'argparse',
            'bunch',
            'backports.ssl_match_hostname',
            'chardet',
            'django-authopenid',
            'django-dajax',
            'django-dajaxice',
            'django-openid',
            'kitchen',
            'kobo',
            'ordereddict',
            'psycopg2',
            'python-bugzilla',
            'python-openid',
            'requests',
            'six',
            'sqlalchemy >= 0.7',
            'urllib3']

setup(
    name='FAF',
    version='0.9-1.20131113',
    description='FAF image for OpenShift',
    author='ABRT Team',
    author_email='crash-catcher@lists.fedorahosted.org',
    url='https://github.com/mtoman/faf-openshift',
    install_requires=REQUIRES,
)
