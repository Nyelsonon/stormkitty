from setuptools import setup, find_packages


setup(
    name='stormkitty',
    version='0.1',
    license='MIT',
    author="nyelson",
    author_email='nyelsonexists@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Nyelsonon/stormkitty',
    keywords='stormbound',
    install_requires=[
          'requests',
      ],

)
