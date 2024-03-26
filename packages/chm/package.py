# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Chm(CMakePackage):
    """FIXME: Put a proper description of your package here."""


    homepage = "https://github.com/Chrismarsh/CHM"
    url = "https://github.com/Chrismarsh/CHM/archive/refs/tags/1.2.7.tar.gz"

    maintainers("Chrismarsh")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("develop")
    version("1.2.7", sha256="cb6314b58e45aaa9b5b316bbd6a5fd2c5cd906c49f7f3a497bae86bbf1cc7e61")
    version("1.2.6", sha256="06878a7c7efc69a5ff08240b0fcecb7d6f1f4f33c1074ba8121cbea740c50047")
    version("1.2.5", sha256="2892cd341c0cd8e92ab680ad5606886a67668d668ed4d9b6ce6751c57eaf1477")
    version("1.2.4", sha256="d0b3dcf5257095945fe6b9ba2a91535da4ab1788feb846f151fcaa8406e60df7")
    version("1.2.3", sha256="8118da1ec6ff8bfc129ba50fb3691a2a4d7a18042b4866e34d9f60ff35f15342")
    version("1.2.2", sha256="c391ca774bf4ec251838a3e2e70fcfba3faad58168112172d8460af9965bea38")
    version("1.2.0", sha256="ceff6bb16bc6cf3b54aeeffebce3cd46c0764e3531cd135fa81d453cda072754")
    version("1.1.0", sha256="93ba35bf4570ba3793674195b51e7f868fac04332929cf4c4db251da3a51ea8a")
    version("1.0.0", sha256="737ca919c83973f8064c474141b1366b345f7ba8477d019f33278e9074f49318")

    depends_on("boost +system+filesystem+date_time+thread+regex+iostreams+program_options+mpi+serialization")
    depends_on("cgal +header_only")
    depends_on("hdf5 +cxx")
    depends_on("netcdf-cxx4@4.3.1:")
    depends_on("gdal@3.8.3: +hdf5 +netcdf ^proj@9.2.1+curl+tiff")
    depends_on("proj@9.2.1+curl+tiff")
    depends_on("sparsehash")
    depends_on("gperftools")
    depends_on("gsl +external-cblas")
    depends_on("armadillo")
    depends_on("intel-oneapi-tbb")
    depends_on("eigen")
    depends_on("meteoio")
    depends_on("func")
    depends_on("trilinos@14.4.0+mpi")
    depends_on("jemalloc")
    depends_on("vtk@9:")
    depends_on("spdlog")

    def cmake_args(self):
        # args = ["--debug-find"]
        args = []
        return args
