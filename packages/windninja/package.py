# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Windninja(CMakePackage):
    """WindNinja is a diagnostic wind model developed for use in wildland fire modeling."""

    url = "https://github.com/firelab/windninja/archive/refs/tags/3.10.0.tar.gz"
    git = "https://github.com/firelab/windninja"
 
    maintainers("Chrismarsh")

    # rebranded NIST fallback license
    # https://github.com/firelab/windninja/blob/master/LICENSE
    license("NIST-PD-fallback")

    version("3.10.0", sha256="7ab120c7465afbe5e95e5eec32523a41ff010094c9b2db87cf9ac4b8eac1f956")
    # version("3.9.0", sha256="0c13f6e054c373d2f78a14f4bbe6808782aa8f37760a45c20db8118e905b2ed6")
    # version("3.8.1", sha256="20e2d51837f7d104bdbc8c9ac1256b0be69de129a51fa9afcc4ba04dea7a1410")
    # version("3.8.0", sha256="fbf2484adae29660219c9b9f9f5d75d4e5d88e68f85778e7918771798ab76809")
    # version("3.7.5", sha256="31e57d40885752f53f1d14ac554c89a10472905ea79317e749672f3df1f528cd")
    # version("3.7.4", sha256="edbc954b153113376cd991bdf5c855e301837356dc488de999050edc80e9800b")
    # version("3.7.3", sha256="f26897da2279ad9aea8d2c607dc1c2e0464a470a5ce4f2f423d6c199472f2e58")
    # version("3.7.2", sha256="4465ab9fe15ee13a15e95bfc94601b5a5b7453abcc38e1ee171bb74ae20f990e")
    # version("3.7.1", sha256="ed4f4c21b6606f1663b0aeb38b506f7258937bfa9984d68dd12eb6adb5754f25")
    # version("3.7.0", sha256="218e43d4e2b128a61003e8227b1c06495ed99461ce7034689d87470bac8996e4")

    variant("openmp", default=True, description="Enable OpenMP support")

    depends_on("cmake@3.0:",type="build")
    depends_on("boost@1.74.0: +date_time +program_options +test")
    depends_on("gdal@3.4.1: +netcdf +curl")
    

    def cmake_args(self):

        args = [

            self.define("NINJA_QTGUI", False),
            self.define("NINJAFOAM", False),
            self.define_from_variant("OPENMP_SUPPORT", "openmp"),
            self.define("CMAKE_CXX_STANDARD", "11")
        ]
        return args
