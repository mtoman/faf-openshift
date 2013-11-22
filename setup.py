#!/usr/bin/env python

from setuptools import setup

REQUIRES = ['Django <= 1.4',
            'argparse',
            'bunch',
            'backports.ssl_match_hostname',
            'chardet',
            'django-authopenid',
            'django-dajax',
            'django-dajaxice',
            'django-openid',
            'kitchen',
            'ordereddict',
            'psycopg2',
            'python-bugzilla',
            'python-openid',
            'requests',
            'six',
            'sqlalchemy >= 0.7',
            'urllib3']

# Only install python-fedora if kitchen is available
try:
    import kitchen
    REQUIRES.append("python-fedora")
except:
    pass

setup(
    name='FAF',
    version='0.9-1.20131113',
    description='FAF image for OpenShift',
    author='ABRT Team',
    author_email='crash-catcher@lists.fedorahosted.org',
    url='https://github.com/mtoman/faf-openshift',
    install_requires=REQUIRES,
)
