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
    maintainers("Chrismarsh")

    version("master", branch="master")
    version("2.2.0", sha256="bd4ecbc27096fa0b913fb46059e02298a96afd4912d549eb68b5c4c090999976")
    version("2.1.0", sha256="150cc53fe90df16a1b06f34c3293f4aef4557ce42b30e1095e7570b1c367b9f7")
    version("2.0", sha256="ca25b960c72bebc5b0be0fedc189ef24e669d21a7571fd59f751a187fb6c1cea")
    version("1.0", sha256="60dbc353f82208efde08eeaea1fabd15e805b6c517a8e033d168027c89884fbf")

    variant("armadillo", default=True, description="Use Armadillo to enable ChebyInterpTables or PadeTable tables.")
    variant("openmp", default=True, description="Enable OpenMP")
    variant("examples", default=False, description="Build examples")

    depends_on("cxx", type="build") 
    
    depends_on("boost")
    depends_on("armadillo", when="+armadillo")


    def cmake_args(self):
        args = [
            self.define_from_variant("FUNC_USE_OPENMP", "openmp"),
            self.define_from_variant("FUNC_USE_ARMADILLO", "armadillo"),
            self.define_from_variant("BUILD_EXAMPLES", "examples"),
        ]
        return args
