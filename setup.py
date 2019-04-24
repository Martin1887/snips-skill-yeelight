from setuptools import setup

setup(
    name='snipsyeelight',
    version='1.0',
    description='Yeelight bulbs skill for Snips',
    author='Martin1887',
    author_email='marcos.martin.pozo.delgado@gmail.com',
    url='https://github.com/Martin1887/snips-skill-yeelight.git',
    download_url='',
    license='MIT',
    install_requires=[
        'requests==2.6.0',
        'funcsigs==1.0.2',
        'mock==2.0.0',
        'pbr==3.1.1',
        'six==1.11.0'
    ],
    keywords=['snips', 'yeelight'],
    package_data={'snipsyeelight': ['Snipsspec']},
    packages=['snipsyeelight'],
    include_package_data=True
)
