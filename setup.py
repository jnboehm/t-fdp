from distutils.core import setup
from distutils.extension import Extension

import numpy
from Cython.Build import cythonize

package = Extension(
    "bh_tforce",
    ["src/tfdp/bh_tforce/bh_tforce.c"],
    include_dirs=[numpy.get_include()],
    extra_compile_args=["-fopenmp"],
    extra_link_args=["-fopenmp"],
)
setup(ext_modules=cythonize([package]))
