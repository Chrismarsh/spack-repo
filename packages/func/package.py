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
    git = "https://github.com/uofs-simlab/func"

    license("GPL/LGPL")

    version("master", branch="master")
    version("2.1.0", sha256="150cc53fe90df16a1b06f34c3293f4aef4557ce42b30e1095e7570b1c367b9f7")
    version("2.0", sha256="ca25b960c72bebc5b0be0fedc189ef24e669d21a7571fd59f751a187fb6c1cea")
    version("1.0", sha256="60dbc353f82208efde08eeaea1fabd15e805b6c517a8e033d168027c89884fbf")


    depends_on("boost")

    variant("openmp", default=True, description="Enable OpenMP")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = [
        self.define_from_variant("FUNC_USE_OPENMP", "openmp")
        ]
        return args
