# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Icestorm(MakefilePackage):
    """Project IceStorm aims at documenting the bitstream format of Lattice iCE40 FPGAs
       and providing simple tools for analyzing and creating bitstream files."""

    homepage = "https://github.com/YosysHQ/icestorm"
    git      = "https://github.com/YosysHQ/icestorm"

    version('master', branch='master')

    maintainers = ['qgp']

    # FIXME: add variant with iceprog

    # depends_on('libftdi1') # FIXME: needed for iceprog
    depends_on('pkgconfig', type='build')

    def edit(self, spec, prefix):
        env['PREFIX'] = prefix
        env['ICEPROG'] = '0'
