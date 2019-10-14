from setuptools import setup, find_packages

setup(
    name = "Salmon Fisher Python Prototype",
    version = "0.1-SNAPSHOT",
    packages = find_packages(),
    install_requires = [
        'flask==1.0',
        'pyjade==1.5',
        'Flask-Login==0.1.3',
        'flask-peewee==0.5.4',
        'Flask-WTF==0.8',
        'Flask-Script==0.3.3',
        'Flask-DebugToolbar==0.7.1',
        'wtf-peewee==0.1.3'#,
        #'Flask-Babel==0.8'
    ],
    extras_require= {
        'statlib': ['1.1',],
    },
    package_data = {
        '': ['*.txt', '*.rst'],
    },
    author='Daroth',
    author_email='daroth@braindead.fr',
    description='POC of Salmon Fisher ported to python'
)
