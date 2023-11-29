# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install func
#
# You can edit this file again by typing:
#
#     spack edit func
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Func(CMakePackage):
    """(Function Comparator) is a C++ tool for quickly profiling the performance of various different abstracted implementations of mathematical function evaluations"""


    homepage = "https://github.com/uofs-simlab/func"
    url = "https://github.com/uofs-simlab/func/archive/refs/tags/v2.0.tar.gz"

    license("GPL/LGPL")

    version("2.0", sha256="ca25b960c72bebc5b0be0fedc189ef24e669d21a7571fd59f751a187fb6c1cea")

    depends_on("boost")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
