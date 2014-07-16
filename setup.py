import os
from pip import req
from setuptools import setup, find_packages


REQUIREMENTS = [str(pip_req.req) for pip_req in req.parse_requirements(
    os.path.join(os.path.dirname(__file__), 'requirements.txt'))
]

setup(
    name='pysubdb',
    version='0.1',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
)
