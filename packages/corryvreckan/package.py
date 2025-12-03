# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Corryvreckan(CMakePackage):
    """The Maelstrom for Your Test Beam Data"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://gitlab.cern.ch/corryvreckan/corryvreckan/-/archive/v2.0/corryvreckan-v2.0.tar.bz2"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("2.0", sha256="49665c96981b1275eef23e71cd7f313aae5222b0947ecdd422cc39ed1bb7f066")

    depends_on("cxx", type="build")

    # FIXME: Add dependencies if required.
    depends_on("vdt")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
