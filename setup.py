from distutils.core import setup

from meterplugin import PluginManifest


setup(
    name='meter-plugin-port-scan',
    version='0.8.0',
    url="http://github.io/boundary/meter-plugin-port-scan",
    author='David Gwartney',
    author_email='david_gwartney@bmc.com',
    packages=['meterplugin', ],
    scripts=[],
    package_data={'meterplugin': ['templates/*']},
    license='LICENSE',
    description='TrueSight Pulse Meter Plugin SDK for Python',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)
