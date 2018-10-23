from setuptools import setup

setup(
    name='scpfl',

    packages=['scpfl'],

    include_package_data=True,

    version='1.0.3',

    description='ESPN fantasy football API',

    author='Joshua Burns',

    author_email='joshua.s.burns@outlook.com',

    install_requires=['requests>=2.0.0,<3.0.0', 'apscheduler>3.0.0'],

    test_suite='nose.collector',

    tests_require=['nose', 'requests_mock'],

    url='https://github.com/snrubauhsoj/scpfl',

    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
