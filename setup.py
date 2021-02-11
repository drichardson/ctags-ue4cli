from os.path import abspath, dirname, join
from setuptools import setup

# Read the README markdown data from README.md
with open(abspath(join(dirname(__file__), 'README.md')), 'rb') as readmeFile:
    __readme__ = readmeFile.read().decode('utf-8')

setup(
    name='ctags-ue4cli',
    version='0.0.2',
    description='Generate tags file for Unreal Engine projects using Universal Ctags',
    long_description=__readme__,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: The Unlicense (Unlicense)',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Build Tools',
        'Environment :: Console'
    ],
    keywords='epic unreal engine ctags',
    url='http://github.com/drichardson/ctags-ue4cli',
    author='Doug Richardson',
    author_email='doug@rekt.email',
    packages=[
        'ctags_ue4cli',
        'ctags_ue4cli.commands'
    ],
    zip_safe=False,
    python_requires='>=3.7',
    install_requires=[
        'setuptools',
        'ue4cli>=0.0.51'
    ],
    entry_points={
        'ue4cli.plugins': ['ctags=ctags_ue4cli:__PLUGIN_DESCRIPTOR__']
    }
)
