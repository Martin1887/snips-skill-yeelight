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
        'hermes_python'
    ],
    keywords=['snips', 'yeelight'],
    package_data={'snipsyeelight': ['Snipsspec']},
    packages=['snipsyeelight'],
    include_package_data=True
)
