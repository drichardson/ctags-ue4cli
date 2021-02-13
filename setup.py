import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='ctags-ue4cli',
    version='0.0.4',
    description='ctags plugin for ue4cli',
    long_description=long_description,
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
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'ue4cli>=0.0.51'
    ],
    entry_points={
        'ue4cli.plugins': ['ctags=ctags_ue4cli:__PLUGIN_DESCRIPTOR__']
    }
)
