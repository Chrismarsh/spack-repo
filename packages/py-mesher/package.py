# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakeBuilder
from spack_repo.builtin.build_systems import python
from spack.package import *


class PyMesher(python.PythonPackage):
    """
    Mesher is a novel multi-objective unstructured mesh generation software 
    that allows mesh generation to be generated from an arbitrary number of hydrologically 
    important features while maintaining a variable spatial resolution. 
    """

    homepage = "https://github.com/Chrismarsh/mesher/"
    pypi = "mesher/mesher-2.1.2.tar.gz"
    git = "https://github.com/Chrismarsh/mesher.git"

    maintainers("Chrismarsh")

    license("GPL-3.0-or-later", checked_by="Chrismarsh")

    version("develop", branch="dev")
    version("2.1.11", sha256="74beeb84d96edeb56e7502403956861dd66de138eb96ec0fdc10cd493c3b33b8")
    version("2.1.10", sha256="33340dd65877dacfc9200db2fec11369b4b6eda3d89f21b6bdca281e359332b7")
    version("2.1.9", sha256="62409a6c8a92225caaf30171fdde3c32e98bcfeadb5844b303186e6c92b9124d")
    version("2.1.8", sha256="ef7fb1d1b0cbb3d4e7fa48ec35187f49232cf185af7c14a227ec82a041b30b3c")
    version("2.1.7", sha256="8c6635cdcd3426fa1583a2b59d4546e209a324754f32c487da301c03b6170726")
    version("2.1.6", sha256="0620598c44fc5c4256fb3f93b1c7583b143b21729f780621efa9824d7d9e4a55")
    version("2.1.4", sha256="a142b6c5773187ddd98bb9f422a9a8545f90f2482f4c9f5089b1f7f54ea30caf")
    version("2.1.3", sha256="4f57208da5440a21b44046eab7fcf74b428a662bb39b9f1c35b301d3b66db90e")
    version("2.1.2", sha256="5bfd4382c74138eef6d509b41777c1daf28919dd78cf392c63a5f032f13f67c7")
    version("2.1.1", sha256="512a4ca81391420550a2414cc9c8d74c60bfa6635c964af5f515166c9ffff619")
    version("2.1.0", sha256="672ad5549399372473dff811604ee79c0112ad6f15e3e2acaed4f5ec602d2610")

    depends_on("cxx", type="build") 
    
    # pyproject.toml
    depends_on("py-scikit-build-core +pyproject", type="build")

    # setup.py
    depends_on("vtk+python@9.2:")
    depends_on("py-numpy")
    depends_on("py-matplotlib")
    depends_on("py-cloudpickle")
    depends_on("py-metis")
    depends_on("py-mpi4py")
    depends_on("py-natsort")
    depends_on("py-scipy")


    # cmake build
    depends_on("cgal@:5 +header_only", when="@:2.1.8")
    depends_on("cgal@6: +gmp")
    depends_on("metis")
    depends_on("boost@1.71.0: +program_options+filesystem")
    depends_on("gdal@3.5: +python")



class PythonPipBuilder(python.PythonPipBuilder):

    def setup_build_environment(self, env):

        std_args = CMakeBuilder.std_args(self.pkg) + CMakeBuilder.cmake_args(self.pkg)
        std_args = std_args[2:] # drop "-G Makefile"

        # pass through all the spack cmake args to scikit-build
        # https://scikit-build-core.readthedocs.io/en/latest/configuration.html#configuring-cmake-arguments-and-defines
        SKBUILD_CMAKE_ARGS = ' '.join(std_args)
        env.set("CMAKE_ARGS", SKBUILD_CMAKE_ARGS)