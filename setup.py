from distutils.core import setup
from Cython.Build import cythonize

setup(name='Cython Verify Image',
      ext_modules=cythonize("cython_verify.pyx"))