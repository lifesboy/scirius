import subprocess
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

print('====> Setting up...')
setup(
    name='scirius',
    version='3.8.0',
    packages=['scirius','rules','suricata', 'accounts', 'viz'],
    scripts=['manage.py'],
    include_package_data=True,
    description='A web interface to manage Suricata rulesets',
    long_description=README,
    url='https://www.stamus-networks.com/open-source/#scirius',
    author='Eric Leblond',
    author_email='eleblond@stamus-networks.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

# setup supervisor service
cmd = '''
    mkdir -p /usr/share/python3/scirius
    cp -R ./usr/share/python3/scirius/bin /usr/share/python3/scirius
    cp ./usr/share/python3/scirius/requirements.txt /usr/share/python3/scirius
    cp ./usr/share/python3/scirius/get-pip.py /usr/share/python3/scirius
    cd /usr/share/python3/scirius
    . bin/activate
    python3 get-pip.py
    python3 -m pip install -r requirements.txt
    deactivate
    cd -

    mkdir -p /usr/share/doc
    cp -R ./usr/share/doc/scirius /usr/share/doc

    mkdir -p /usr/share/python3/scirius/lib
    ln -sf /usr/lib/python3.7 /usr/share/python3/scirius/lib/python3.7

    ln -sf /etc/scirius/local_settings.py scirius/local_settings.py
    if [ -e /usr/share/python3/scirius/lib/python3.7/site-packages/scirius-3.8.0-py3.7.egg/scirius/ ]; then
        ln -sf /etc/scirius/local_settings.py /usr/share/python3/scirius/lib/python3.7/site-packages/scirius-3.8.0-py3.7.egg/scirius/local_settings.py
    fi
    if [ -e /usr/local/lib/python3.7/dist-packages/scirius-3.8.0-py3.7.egg/scirius/ ]; then
        ln -sf /etc/scirius/local_settings.py /usr/local/lib/python3.7/dist-packages/scirius-3.8.0-py3.7.egg/scirius/local_settings.py
    fi
'''
print('====> Setting up supervisor...')
exit_status = subprocess.call(cmd, shell=True)
