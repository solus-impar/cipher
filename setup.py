"""cipher: pip setup file."""
from os import path
from setuptools import setup
from pip.req import parse_requirements

here = path.abspath(path.dirname(__file__))

requirements_path = path.join(here, 'requirements.txt')
install_requirements = parse_requirements(requirements_path, session=False)
requirements = [str(ir.req) for ir in install_requirements]

setup(
    name='cipher',
    version='0.0.0',
    description='A simple cipher.',
    author='Mike Canoy',
    author_email='mike@mikecanoy.net',
    url='https://github.com/solus-impar/cipher',
    install_requirements=requirements,
    packages=['cipher']
)
