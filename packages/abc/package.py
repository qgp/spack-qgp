# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

# FIXME: What do we need this for?

class Abc(CMakePackage):
    """System for Sequential Logic Synthesis and Formal Verification"""

    homepage = "https://github.com/berkeley-abc/abc"
    git      = "https://github.com/berkeley-abc/abc"

    maintainers = ['qgp']

    # FIXME: use safe downloads
    # https://spack.readthedocs.io/en/latest/packaging_guide.html#github
    version('master')
    version('0.30-yosys', git='https://github.com/YosysHQ/abc', tag='yosys-0.30')
