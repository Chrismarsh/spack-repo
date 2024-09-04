# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.build_systems.cmake import CMakeBuilder

class PyPychm(PythonPackage):
    """
    Mesher is a novel multi-objective unstructured mesh generation software 
    that allows mesh generation to be generated from an arbitrary number of hydrologically 
    important features while maintaining a variable spatial resolution. 
    """

    homepage = "https://github.com/Chrismarsh/mesher/"
    git = 'https://github.com/Chrismarsh/pyCHM.git'

    maintainers("Chrismarsh")

    license("GPL-3.0-or-later", checked_by="Chrismarsh")

    version("develop", branch="develop")


    # setup.py
    depends_on("vtk+python@9.2:")
    depends_on("py-numpy")
    depends_on("py-xarray +io +viz +parallel")
    depends_on("py-netcdf4")
    depends_on("py-pandas")
    depends_on("gdal@3.5: +python +netcdf +hdf5")
    depends_on("py-dask")
    depends_on("py-pyvista@0.29:")
    depends_on("py-rioxarray")
    depends_on("py-rasterio")
    depends_on("py-cftime")
    depends_on("py-pyproj")

