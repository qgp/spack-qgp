# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class Libftdi1(CMakePackage):
    """libftdi"""

    homepage = "https://www.intra2net.com/en/developer/libftdi/index.php"
    url      = "https://www.intra2net.com/en/developer/libftdi/download/libftdi1-1.5.tar.bz2"

    maintainers = ['qgp']

    depends_on('libusb')

    version('1.5', sha256='7c7091e9c86196148bd41177b4590dccb1510bfe6cea5bf7407ff194482eb049')
