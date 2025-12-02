# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Nextpnr(CMakePackage):
    """Place and route tool"""

    homepage = "https://https://github.com/YosysHQ/nextpnr"
    url      = "https://github.com/YosysHQ/nextpnr/archive/refs/tags/nextpnr-0.6.tar.gz"
    git      = "https://github.com/YosysHQ/nextpnr"

    maintainers = ['qgp']

    version('master', branch='master')
    version("0.9", sha256="8cebc65049ff91c411d963ea2304b1a3dd42036f79de2eb3e9834c842f934495")
    version("0.8", sha256="968ce3f39973e1d855c6bf1606a334d9f9650cff978554b822de0a6c088947bd")
    version("0.7", sha256="bd173cb218c97f66e4afdf7b886d70c8c0893f544a1cf20b50c0182a1d9f2f45")
    version("0.6", sha256="76fa4bca48cc8462a8a3c28f89673439e7632a9baabc7bb121c58b75936d2d0b")
    version("0.5", sha256="2e3485753123f1505351a37adec37ce47a3a96d3f67bbcaf59ec390c8ffc1cdd")
    version("0.4", sha256="ae8e01496c3bb6607cef0e2501b8cf00aba564e9b116dd323887575ab82757c0")
    version("0.3", sha256="6dda678d369a73ca262896b672958eebeb2e6817f60afb411db31abeff191c4a")
    version("0.2", sha256="022325d56502885e9a43ad04efe27014e7091acb6833837340d061451a7510a6")
    version("0.1", sha256="21ec82159c6b4c67c32fa16a8280230094a113c189af18762ddf4ae739db0b3c")

    depends_on('icestorm')
    depends_on('eigen')
    depends_on('python')
    depends_on('boost+filesystem+program_options+iostreams+system+thread')
    depends_on('pkgconfig', type='build')

    def cmake_args(self):
        args = ['-DARCH=ice40', f'-DICESTORM_INSTALL_PREFIX={self.spec["icestorm"].prefix}']
        return args
