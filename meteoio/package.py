# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install meteoio
#
# You can edit this file again by typing:
#
#     spack edit meteoio
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Meteoio(CMakePackage):
    """The MeteoIO library aims at making data access easy and safe for numerical 
    simulations in environmental sciences requiring general meteorological data."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.gitlabext.wsl.ch"
    url = "https://gitlabext.wsl.ch/snow-models/meteoio/-/archive/MeteoIO-2.8.0/meteoio-MeteoIO-2.8.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("2.8.0", sha256="898bf0d0329000e7ae18064c30ea72362aac447deda0b013ee22e4aa63563efd")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        cmake_args = []
        cmake_args.append("-Dshared:BOOL=True")
        cmake_args.append("-DPLUGIN_A3DIO:BOOL=False")
        cmake_args.append("-DPLUGIN_ALPUG:BOOL=False")
        cmake_args.append("-DPLUGIN_ARCIO:BOOL=False")
        cmake_args.append("-DPLUGIN_ARPSIO:BOOL=False")
        cmake_args.append("-DPLUGIN_BORMAIO:BOOL=False")
        cmake_args.append("-DPLUGIN_CSVIO:BOOL=False")
        cmake_args.append("-DPLUGIN_COSMOXMLIO:BOOL=False")
        cmake_args.append("-DPLUGIN_DBO:BOOL=False")
        cmake_args.append("-DPLUGIN_GEOTOPIO:BOOL=False")
        cmake_args.append("-DPLUGIN_GRASSIO:BOOL=False")
        cmake_args.append("-DPLUGIN_GRIBIO:BOOL=False")
        cmake_args.append("-DPLUGIN_GSNIO:BOOL=False")
        cmake_args.append("-DPLUGIN_IMISIO:BOOL=False")
        cmake_args.append("-DPLUGIN_NETCDFIO:BOOL=False")
        cmake_args.append("-DPLUGIN_OSHDIO:BOOL=False")
        cmake_args.append("-DPLUGIN_PGMIO:BOOL=False")
        cmake_args.append("-DPLUGIN_PNGIO:BOOL=False")
        cmake_args.append("-DPLUGIN_PSQLIO:BOOL=False")
        cmake_args.append("-DPLUGIN_SMETIO:BOOL=False")
        cmake_args.append("-DPLUGIN_SNIO:BOOL=False")
        cmake_args.append("-DPLUGIN_SASEIO:BOOL=False")
        cmake_args.append("-DPROJ4:BOOL=False")
        return cmake_args
