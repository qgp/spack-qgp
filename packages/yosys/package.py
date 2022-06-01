# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Yosys(MakefilePackage):
    """Yosys toolchain"""

    homepage = "https://https://yosyshq.net/yosys"
    url      = "https://github.com/YosysHQ/yosys/archive/refs/tags/yosys-0.17.tar.gz"

    maintainers = ['qgp']

    version('0.17', sha256='37db450d08884a7c411f44ddf639284967ed1a39e11cd6b78d816186113d0173')
    version('0.16', sha256='c7a161e5f567b853a18be8417b60d31ce77804994dafc93306b897ddc335aa3c')
    version('0.15', sha256='a40fcc487d2a31c2abc6f61d39a84e262f2650e40de479542bbde317308c4612')

    depends_on('flex')
    depends_on('bison')

    def edit(self, spec, prefix):
        env['PREFIX'] = prefix
        makefile = FileFilter('Makefile')
        makefile.filter('CONFIG := .*', 'CONFIG := gcc')
