# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMesher(PythonPackage):
    """
    Mesher is a novel multi-objective unstructured mesh generation software 
    that allows mesh generation to be generated from an arbitrary number of hydrologically 
    important features while maintaining a variable spatial resolution. 
    """

    homepage = "https://github.com/Chrismarsh/mesher/"
    url = "https://github.com/Chrismarsh/mesher/archive/refs/tags/2.0.7.tar.gz"

    maintainers("Chrismarsh")

    license("GPL-3.0-or-later", checked_by="Chrismarsh")

    version("develop")
    version("2.0.7", sha256="2af40d5fe86ae93cd4f3b999359e47e183f531c6cbb4bada9339c923db79315d")

    # pyproject.toml
    depends_on("py-scikit-build-core +pyproject", type="build")

    # setup.py
    depends_on("vtk+python@9:")
    depends_on("py-numpy")
    depends_on("py-matplotlib")
    depends_on("py-cloudpickle")
    depends_on("py-metis")
    depends_on("py-mpi4py")
    depends_on("py-natsort")
    depends_on("py-scipy")


    # cmake build
    depends_on("cgal@5: +header_only")
    depends_on("metis")
    depends_on("boost@1.71.0: +program_options+filesystem")
    depends_on("gdal@3.5: +python")

