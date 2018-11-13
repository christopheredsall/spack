# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Bbcp(Package):
    """Securely and quickly copy data from source to target"""

    homepage = "http://www.slac.stanford.edu/~abh/bbcp/"
    git      = "http://www.slac.stanford.edu/~abh/bbcp/bbcp.git"

    version('git', branch='master')

    depends_on('zlib')
    depends_on('openssl')

    def install(self, spec, prefix):
        cd("src")
        make()
        # BBCP wants to build the executable in a directory whose name depends
        # on the system type
        makesname = Executable("../MakeSname")
        bbcp_executable_path = "../bin/%s/bbcp" % makesname(
            output=str).rstrip("\n")
        destination_path = "%s/bin/" % prefix
        mkdirp(destination_path)
        install(bbcp_executable_path, destination_path)
