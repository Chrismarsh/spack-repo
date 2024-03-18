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
    version("2.0.1", sha256="2b0dc247c0b4a2344ce0207d8a4c24712c2804be43826e7f75f2e7dd977e98d9")
    version("2.0.3", sha256="10272ad5819badf2eb770ff4bacba75dde1cd22768fb6e9b2a6db3434f4a22cc")
    version("2.0.7", sha256="2af40d5fe86ae93cd4f3b999359e47e183f531c6cbb4bada9339c923db79315d")
    version("2.1.0", sha256="fce4ed52ecbd4d905fb224060eafd510ec91a01306268208519b0403e44c427d")
    version("2.1.1", sha256="a27cffe932a7c24f3d76c5f1fb584e96f75050a661baa1da8c2573e9b5c35578")

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

