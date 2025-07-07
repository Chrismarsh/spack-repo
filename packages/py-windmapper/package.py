# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakeBuilder
from spack_repo.builtin.build_systems import python
from spack.package import *


class PyWindmapper(python.PythonPackage):
    """
    Windmapper is a tool used to produce pre-computed libraries of wind field used 
    for wind downscaling using the WindNinja wind diagnostic model.
    """

    homepage = "https://github.com/Chrismarsh/Windmapper"
    url = "https://github.com/Chrismarsh/Windmapper/archive/refs/tags/2.1.16.tar.gz"
    git = "https://github.com/Chrismarsh/Windmapper.git"

    maintainers("Chrismarsh")

    license("GPL-3.0-or-later", checked_by="Chrismarsh")

    version("develop", branch="develop", no_cache=True)
    version("2.1.16", sha256="da7dca6d16557221814377f90aef7bdf3434c0ac75978969975f9b93672ffe1c")

    # pyproject.toml
    depends_on("cmake@3.16:", type="build")
    depends_on("py-scikit-build-core +pyproject", type="build")

    # setup.py
    depends_on("py-numpy")
    depends_on("py-scipy")
    depends_on("py-elevation")
    depends_on("py-pyproj")
    depends_on("py-tqdm")
    depends_on("py-rasterio")
    depends_on("py-mpi4py")
    depends_on("py-cloudpickle")

    depends_on("gdal@3.5: +python")
    depends_on("windninja", type="run")

    def setup_build_environment(self, env):
        env.set("BUILD_WINDNINJA", False)

    
class PythonPipBuilder(python.PythonPipBuilder):

    def setup_build_environment(self, env):

        std_args = CMakeBuilder.std_args(self.pkg) + CMakeBuilder.cmake_args(self.pkg)
        std_args = std_args[2:] # drop "-G Makefile"

        # pass through all the spack cmake args to scikit-build
        # https://scikit-build-core.readthedocs.io/en/latest/configuration.html#configuring-cmake-arguments-and-defines
        SKBUILD_CMAKE_ARGS = ' '.join(std_args)
        env.set("CMAKE_ARGS", SKBUILD_CMAKE_ARGS)
        env.set("BUILD_WINDNINJA", False)