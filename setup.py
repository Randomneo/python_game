from distutils.core import setup

setup(
    name='game',
    version='0.1.0',
    description='Simple python game',
    author='Rostislav Misiura',
    author_email='rostislav9999@gmail.com',
    url='https://github.com/Randomneo/python_game',
    requirments=[
        'pygame==1.9.1release',
        'enum34',
    ],
    console=['main.py']
)
