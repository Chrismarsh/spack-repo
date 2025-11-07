# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakeBuilder
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPychm(PythonPackage):
    """
    Tools for working with CHM
    """

    homepage = "https://github.com/Chrismarsh/pyCHM/"
    git = 'https://github.com/Chrismarsh/pyCHM.git'
    pypi = "CHM/chm-1.4.4.tar.gz"

    maintainers("Chrismarsh")

    license("GPL-3.0-or-later", checked_by="Chrismarsh")

    version("develop", branch="develop", no_cache=True) # don't source cache this git repo
    version("1.4.4", sha256="7dce46311e1978456257fb4b8c8fa0fc8dc434b574623f23e21076da107a88fc")


    # setup.py
    depends_on("vtk +python@9.2:", type=("build", "run"))
    depends_on("py-numpy@1.26:", type=("build", "run")) #forces a new version of setuptools needed for bokeh
    depends_on("py-xarray@2025: +io +viz +parallel", type=("build", "run"))
    depends_on("py-uxarray", type=("build", "run"))
    depends_on("py-netcdf4", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("gdal@3.5: +python +netcdf +hdf5", type=("build", "run"))
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-pyvista@0.29:", type=("build", "run"))
    depends_on("py-rioxarray@0.19:", type=("build", "run"))
    depends_on("py-rasterio", type=("build", "run"))
    depends_on("py-cftime", type=("build", "run"))
    depends_on("py-pyproj", type=("build", "run"))
    depends_on("esmf +python", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))

