from distutils.core import setup

DISTNAME='module_name'
FULLVERSION='0.1'

setup(
    name=DISTNAME,
    version=FULLVERSION,
    packages=['module_name'],
    entry_points={
        'console_scripts': [
            'py-module-name = module_name.resolve:main',
        ]
    }
)
