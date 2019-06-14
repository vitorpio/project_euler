from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='project_euler',
    version='0.1.0',
    description='My solutions to projecteuler.net problems',
    long_description=readme,
    author='Vitor Pio',
    author_email='vitormarquespio@gmail.com',
    url='https://github.com/vitorpio/project_euler',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
