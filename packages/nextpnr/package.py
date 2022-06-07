# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Nextpnr(CMakePackage):
    """Place and route tool"""

    homepage = "https://https://github.com/YosysHQ/nextpnr"
    url      = "https://github.com/YosysHQ/nextpnr/archive/refs/tags/nextpnr-0.3.tar.gz"
    git      = "https://github.com/YosysHQ/nextpnr"

    maintainers = ['qgp']

    version('master', branch='master')
    version('0.3', sha256='6dda678d369a73ca262896b672958eebeb2e6817f60afb411db31abeff191c4a')

    depends_on('icestorm')

    def cmake_args(self):
        args = ['-DARCH=ice40', f'-DICESTORM_INSTALL_PREFIX={self.spec["icestorm"].prefix}']
        return args
