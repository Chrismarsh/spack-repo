# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Windninja(CMakePackage):
    """WindNinja is a diagnostic wind model developed for use in wildland fire modeling."""

    url = "https://github.com/firelab/windninja/archive/refs/tags/3.10.0.tar.gz"
    git = "https://github.com/firelab/windninja"

    maintainers("Chrismarsh")

    # rebranded NIST fallback license
    # https://github.com/firelab/windninja/blob/master/LICENSE
    license("NIST-PD-fallback")

    version("3.12.1", sha256="c6a0bf3e79a7dca875f9c1bcec6b3b625192bdd6cebcfdfb1fc6c30def4bea63")
    version("3.11.2", sha256="c9b9af0c9905d8a0792ccf9db9958a0e3b201f653336fd59dbc7f5679cb79881")
    version("3.10.0", sha256="7ab120c7465afbe5e95e5eec32523a41ff010094c9b2db87cf9ac4b8eac1f956")

    variant("openmp", default=True, description="Enable OpenMP support")
    variant("ninjafoam", default=False, description="Enable OpenFoam support")
    variant("qtgui", default=False, description="Build Qt GUI")

    variant("build_fetch_dem", default=False, description="Build a standalone command line interface DEM utility")
    variant("build_stl_converter", default=False, description="Build a standalone command line interface for STL file conversions")
    variant("build_convert_output", default=False, description="Build a standalone command line interface for xyz file conversions")
    variant("build_solar_grid", default=False, description="Build a application for building solar grids")

    depends_on("cxx", type="build")
    depends_on("c", type="build")

    depends_on("cmake@3.5:",type="build")
    depends_on("boost@1.74.0: +date_time +program_options +test")
    depends_on("gdal@3.4.1: +netcdf +curl")
    depends_on("llvm-openmp", when="+openmp %apple-clang")
    depends_on("openfoam", when="+ninjafoam")

    depends_on("qt@4", when="+qtgui")

    conflicts(
        "+ninjafoam",
        when="platform=darwin",
        msg="ninjafoam is not supported on Macos because OpenFoam does not build on Macos",
    )

    # https://github.com/firelab/windninja/pull/650
    patch("https://github.com/firelab/windninja/commit/f849d4b11ec2a8e30915114b02211b7b57be0e2c.patch?full_index=1",
        sha256="5c9a6b377a04fa92bc56701e0676118741ea660e363a98bdf11d09eca88f81ad",
        when="@3.12.1"
    )

    # handle CPLIsNan removal in gdal 3.11.3
    # https://github.com/firelab/windninja/pull/651
    patch("https://github.com/firelab/windninja/commit/b71b90fcfd3ba91620ea932ce3378df5989f6d8c.patch?full_index=1",
        sha256="78f3d4913b4c7e83edd767cec65c7e9fdd3c41d9dba939d0bd4d10bb50075cd7",
        when="@3.12.1 ^gdal@3.11.3:"
    )

    def cmake_args(self):

        args = [
            self.define("NINJA_QTGUI", False),
            self.define("NINJAFOAM", False),
            self.define("CMAKE_CXX_STANDARD", "11"),

            # https://github.com/firelab/windninja/issues/630
            self.define("CMAKE_POLICY_VERSION_MINIMUM", "3.5"),

            self.define_from_variant("OPENMP_SUPPORT", "openmp"),
            self.define_from_variant("NINJAFOAM", "ninjafoam"),
            self.define_from_variant("NINJA_QTGUI", "qtgui"),
            self.define_from_variant("BUILD_FETCH_DEM", "build_fetch_dem"),
            self.define_from_variant("BUILD_STL_CONVERTER", "build_stl_converter"),
            self.define_from_variant("BUILD_CONVERT_OUTPUT", "build_convert_output"),
            self.define_from_variant("BUILD_SOLAR_GRID", "build_solar_grid"),
        ]
        return args


    @when("+openmp %apple-clang")
    def patch(self):
        # WN needs to link against openmp explicitly when using apple-clang
        cmake_files = find(self.stage.source_path, "CMakeLists.txt", recursive=True)
        filter_file(r"set\(LINK_LIBS", "set(LINK_LIBS OpenMP::OpenMP_CXX ", *cmake_files, ignore_absent=True)

