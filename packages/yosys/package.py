# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Yosys(MakefilePackage):
    """Yosys is a framework for Verilog RTL synthesis"""

    homepage = "https://https://yosyshq.net/yosys"
    # url      = "https://github.com/YosysHQ/yosys/archive/refs/tags/yosys-0.30.tar.gz"
    # url      = "https://github.com/YosysHQ/yosys/archive/refs/tags/v0.56.tar.gz"
    url      = "https://github.com/YosysHQ/yosys/releases/download/v0.59.1/yosys.tar.gz"

    maintainers = ['qgp']

    version("0.59.1", sha256="5d442ed3b8ba90147be3939953f5104f019b46dfee6472a904d46b7143fcec1a")
    version("0.59", sha256="5e80ea92d7f88a50600b57716226ea0496b8d08e4e135551862bb7f52ea391c5")
    version("0.58", sha256="c67f35c0d3c6946b7bce6eb168180edfda7f1ce295bf4c3ac1b7cd7ccd81cb4b")
    version("0.57", sha256="38e4edecd91006b45cadd33daa38f39c42ab625fe7a58cbfd8ab023d4a87bc4d")
    version("0.56", sha256="b5270419812a38ab3dade6003130fc2eebc9757a4ed9e48b0ceb311428743d04")
    version("0.55", sha256="7dbbabf35a08732104768a43f8143e0c7714b01a7fe978c044cf0df2f8fe961c")
    version("0.54", sha256="99e2a5661e998a23c7c100af4bb63aebb96f13d5d68086ae6a5f1ce920e9783c")
    version("0.53", sha256="126e93d82ceca9ece1cf973b395b46a1cc8105651a8ecf3de9afbe786cdeea58")
    version("0.52", sha256="cf741e7971ba7701b71f2aff18b202de182d55e7803803c16b972dda9b77c490")
    version("0.51", sha256="72abcf81925fc7232cba25d190a48d7be5079569ec2ba233bac2bb116c383eea")

    version("0.30", sha256="1b29c9ed3d396046b67c48f0900a5f2156c6136f2e0651671d05ee26369f147d")
    version("0.29", sha256="475ba8cd06eec9050ebfd63a01e7a7c894d8f06c838b35459b7e29bbc89f4a22")
    version("0.28", sha256="36048ef3493ab43cfaac0bb89fa405715b22acd3927bf7fd3c4b25f8ad541c22")
    version("0.27", sha256="bd6c933daf48c0929b4a9b3f75713d1f79c173be4bdb82fc5d2f5feb97f3668b")
    version("0.26", sha256="e869e3770797f7edf352fd3033d5bba8606d40d6b32bae5051d917d120b9a177")
    version('0.17', sha256='37db450d08884a7c411f44ddf639284967ed1a39e11cd6b78d816186113d0173')
    version('0.16', sha256='c7a161e5f567b853a18be8417b60d31ce77804994dafc93306b897ddc335aa3c')
    version('0.15', sha256='a40fcc487d2a31c2abc6f61d39a84e262f2650e40de479542bbde317308c4612')

    depends_on('abc')
    depends_on('cxxopts')
    depends_on('flex')
    depends_on('bison')
    depends_on('libffi')
    depends_on('pkgconfig', type='build')
    depends_on('tcl')

    @property
    def build_targets(self):
        return [f"ABCEXTERNAL={self.spec["abc"].prefix.lib}"]

    def edit(self, spec, prefix):
        env['PREFIX'] = prefix
        makefile = FileFilter('Makefile')
        makefile.filter('CONFIG := .*', 'CONFIG := gcc')
