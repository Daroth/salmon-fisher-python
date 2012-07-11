from setuptools import setup, find_packages

setup(
    name = "Salmon Fisher Python Prototype",
    version = "0.1-SNAPSHOT",
    packages = find_packages(),
    install_requires = [
        'flask==0.9',
        'pyjade==1.5',
        'Flask-Login==0.1.3',
        'flask-peewee==0.5.4',
        'Flask-WTF==0.8',
    ],
    package_data = {
        '': ['*.txt', '*.rst'],
    },
    author='Daroth',
    author_email='daroth@braindead.fr',
    description='POC of Salmon Fisher ported to python'
)
