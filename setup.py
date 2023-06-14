from setuptools import setup

CLASSIFIERS = '''\
License :: OSI Approved
Programming Language :: Python :: 3.9
Topic :: Software Development
'''

DISTNAME = 'GSoC_QGAN'
AUTHOR = 'Tom Magorsch'
AUTHOR_EMAIL = 'tom.magorsch@tum.de'
DESCRIPTION = 'Quantum Generative Adversarial Networks for hep data analysis'
LICENSE = 'MIT'
README = 'Quantum Generative Adversarial Networks for hep data analysis'

VERSION = '0.1.0'
ISRELEASED = False

PYTHON_MIN_VERSION = '3.9'
PYTHON_REQUIRES = f'>={PYTHON_MIN_VERSION}'

PACKAGES = [
    'GSoC_QGAN',
]

metadata = dict(
    name=DISTNAME,
    version=VERSION,
    long_description=README,
    packages=PACKAGES,
    python_requires=PYTHON_REQUIRES,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    classifiers=[CLASSIFIERS],
    license=LICENSE
)

if __name__ == '__main__':
    setup(**metadata)
