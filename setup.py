import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()


CONTROLLER = True
COMPUTE_NODE = True

requires = [
    'mongoengine',
    'paho-mqtt'
]


scripts = ['bin/apmn-server']
setup(name='apaimanee',
      version='0.0',
      description='',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python :: 3",
          "Framework :: nokkhum",
      ],
      author='Aran Khunaree',
      author_email='alunnice2537@gmail.com',
      scripts=scripts,
      license='xxx License',
      packages=find_packages(),
      url='https://github.com/NiNiiWs/apaimanee-server.git',
      keywords='MOBA, GAME',
      #      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      #      tests_require=requires,
      #      test_suite="nokkhum-controller",
      )
