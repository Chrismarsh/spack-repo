# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Chm(CMakePackage):
    """The Canadian Hydrological Model (CHM) uses a novel, modular, mesh-based approach for developing
     and testing process representations in hydrological modelling. """


    homepage = "https://github.com/Chrismarsh/CHM"
    url = "https://github.com/Chrismarsh/CHM/archive/refs/tags/1.2.7.tar.gz"
    git = "https://github.com/Chrismarsh/CHM.git"

    maintainers("Chrismarsh")

    license("GPL-3.0-or-later", checked_by="Chrismarsh")

    version("develop", branch="develop", no_cache=True) # don't source cache this git repo

    version("1.5.1",
            sha256="d29d18d8a0b5e0fbfef2899313cbba0b9acc280b15dc0a40875e0c9e30ccc571",
            preferred=True
    )

    version("1.5.0",
            sha256="a9fb42cd39baeeec9e5e1157b5d9aa787a12d9c3c661b37402444d88852e76d0"
    )
    version("1.4.5", sha256="d22f3c25743495029d044f7b536d4cae930e01de275fbac98e2a687da7edc016")
    version("1.4.3", sha256="fa07e2c8c2f88afef4842a14074a4cade8c137bf314b54ee1b0a6640d8aa0d15")
    version("1.4.2", sha256="4fdf2fdcca5b1141cac85599d3da3bef5900667b21edf09ab314fc107b5e37f7")
    version("1.4.1", sha256="89b6d592cfaddf1b6debf1f2c462bce0ac29a86dbf82df858dce146e56235dbb")
    version("1.4.0", sha256="2291a730619703bd52e990dff294d92f785e8f66ecc2745dfd4243fb473c8faa")
    version("1.3.1", sha256="595779861be15726eb6d198ea6f4dc5fb100cbdecb00e844bd63ae589c10cb5f")
    version("1.3.0", sha256="39ba8daa000d00a4162b3a672b32682b145ff3ac2c32f7db7f72ef3fd9263287")
    version("1.2.7", sha256="cb6314b58e45aaa9b5b316bbd6a5fd2c5cd906c49f7f3a497bae86bbf1cc7e61")
    version("1.2.6", sha256="06878a7c7efc69a5ff08240b0fcecb7d6f1f4f33c1074ba8121cbea740c50047")
    version("1.2.5", sha256="2892cd341c0cd8e92ab680ad5606886a67668d668ed4d9b6ce6751c57eaf1477")
    version("1.2.4", sha256="d0b3dcf5257095945fe6b9ba2a91535da4ab1788feb846f151fcaa8406e60df7")
    version("1.2.3", sha256="8118da1ec6ff8bfc129ba50fb3691a2a4d7a18042b4866e34d9f60ff35f15342")
    version("1.2.2", sha256="c391ca774bf4ec251838a3e2e70fcfba3faad58168112172d8460af9965bea38")
    version("1.2.0", sha256="ceff6bb16bc6cf3b54aeeffebce3cd46c0764e3531cd135fa81d453cda072754")
    version("1.1.0", sha256="93ba35bf4570ba3793674195b51e7f868fac04332929cf4c4db251da3a51ea8a")
    version("1.0.0", sha256="737ca919c83973f8064c474141b1366b345f7ba8477d019f33278e9074f49318")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("cmake@3.30:", type="build")

    depends_on("boost@1.85.0: +system+filesystem+date_time+thread+chrono+regex+iostreams+program_options+mpi+serialization")
    depends_on("cgal@5:")
    requires("^cgal~gmp", when="^cgal@6:")

    depends_on("hdf5 +cxx")
    depends_on("netcdf-c@4.9.0: +mpi")
    depends_on("netcdf-cxx4@4.3:")
    depends_on("gdal@3.9: +hdf5 +netcdf")
    depends_on("proj@9: +curl+tiff")
    depends_on("sparsehash")
    depends_on("gperftools build_system=autotools")
    depends_on("gsl +external-cblas")
    depends_on("armadillo")

    depends_on("intel-tbb", when="platform=darwin")
    depends_on("intel-oneapi-tbb", when="platform=linux")

    depends_on("eigen")
    depends_on("meteoio")
    depends_on("func@2.2: ~openmp", when="~openmp")
    depends_on("func@2.2: +openmp", when="+openmp")
    depends_on("trilinos@15: +mpi +openmp +threadsafe", when="+openmp")
    depends_on("trilinos@15: +mpi ~openmp", when="~openmp")
    depends_on("jemalloc")
    depends_on("vtk@9.3") # keep bounded at 9.3 as 9.4, 9.5 fail on macos
    depends_on("spdlog")
    depends_on("openblas")
    # depends_on("udunits")

    variant("openmp", default=False, description="Enable OpenMP. Disable for better errors")

    def cmake_args(self):
        # args = ["--debug-find"]
        args = []

        if self.spec.satisfies("^cgal@6:"):
            args.extend(
                [
                    self.define("CGAL_DISABLE_GMP",1),
                ]
            )

        args.extend(
            [
                self.define_from_variant("USE_OMP", "openmp"),
            ]
        )


        return args
