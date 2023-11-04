# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Yosys(MakefilePackage):
    """Yosys is a framework for Verilog RTL synthesis"""

    homepage = "https://https://yosyshq.net/yosys"
    url      = "https://github.com/YosysHQ/yosys/archive/refs/tags/yosys-0.30.tar.gz"

    maintainers = ['qgp']

    version("0.30", sha256="1b29c9ed3d396046b67c48f0900a5f2156c6136f2e0651671d05ee26369f147d")
    version("0.29", sha256="475ba8cd06eec9050ebfd63a01e7a7c894d8f06c838b35459b7e29bbc89f4a22")
    version("0.28", sha256="36048ef3493ab43cfaac0bb89fa405715b22acd3927bf7fd3c4b25f8ad541c22")
    version("0.27", sha256="bd6c933daf48c0929b4a9b3f75713d1f79c173be4bdb82fc5d2f5feb97f3668b")
    version("0.26", sha256="e869e3770797f7edf352fd3033d5bba8606d40d6b32bae5051d917d120b9a177")
    version('0.17', sha256='37db450d08884a7c411f44ddf639284967ed1a39e11cd6b78d816186113d0173')
    version('0.16', sha256='c7a161e5f567b853a18be8417b60d31ce77804994dafc93306b897ddc335aa3c')
    version('0.15', sha256='a40fcc487d2a31c2abc6f61d39a84e262f2650e40de479542bbde317308c4612')

    depends_on('flex')
    depends_on('bison')
    depends_on('libffi')
    depends_on('pkgconfig', type='build')
    depends_on('tcl')

    def edit(self, spec, prefix):
        env['PREFIX'] = prefix
        makefile = FileFilter('Makefile')
        makefile.filter('CONFIG := .*', 'CONFIG := gcc')
