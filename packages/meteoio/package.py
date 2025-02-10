# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Meteoio(CMakePackage):
    """The MeteoIO library aims at making data access easy and safe for numerical 
    simulations in environmental sciences requiring general meteorological data."""

    homepage = "https://meteoio.slf.ch/"
    url = "https://gitlabext.wsl.ch/snow-models/meteoio/-/archive/MeteoIO-2.8.0/meteoio-MeteoIO-2.8.0.tar.gz"

    maintainers("Chrismarsh")

    license("LGPL-3.0-or-later", checked_by="Chrismarsh")

    version("2.8.0", sha256="898bf0d0329000e7ae18064c30ea72362aac447deda0b013ee22e4aa63563efd")

    def cmake_args(self):
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
