from setuptools import setup

setup(
    name='click_utils',
    version='0.1.0',
    py_modules=['click_hello'],
    install_requires=[
        'Click',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'click_utils = click_hello:main_group',
        ],
    },
)