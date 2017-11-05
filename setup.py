from setuptools import setup

package = 'dsmeta'
version = '0.1'
description = "Meta-package depending on commonly-used tools for Data Science"

setup(name=package,
      version=version,
      description=description,
      install_requires=[
          'edward',
          'ipython',
          'keras',
          'matplotlib',
          'numpy',
          'pandas',
          'patsy',
          'psycopg2',
          'pymc3',
          'scipy',
          'seaborn',
          'sklearn',
          'statsmodels',
          'tables',
          'tensorflow',
          'theano'
      ],
      url='https://github.com/mcwitt/dsmeta')
