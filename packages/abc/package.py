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
    url      = "https://github.com/YosysHQ/abc/archive/refs/tags/v0.51.tar.gz"

    maintainers = ['qgp']

    # FIXME: use safe downloads
    # https://spack.readthedocs.io/en/latest/packaging_guide.html#github
    version('master')
    version("0.59", sha256="45218e72b06726d58080907f2a9c2534fa0fad697b0f32577a94392e745495e7")
    # version('0.59', url="https://github.com/YosysHQ/abc/archive/refs/tags/v0.59.tar.gz")
    version('0.30-yosys', git='https://github.com/YosysHQ/abc', tag='yosys-0.30')
