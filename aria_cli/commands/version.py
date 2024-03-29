########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

"""
Handles 'aria --version'
"""

import argparse
from StringIO import StringIO
from aria_cli.utils import get_version_data


class VersionAction(argparse.Action):
    def __init__(self,
                 option_strings,
                 dest=argparse.SUPPRESS,
                 default=argparse.SUPPRESS,
                 help=None):
        super(VersionAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            help=help)

    @staticmethod
    def _format_version_data(version_data, prefix=None, suffix=None,
                             infix=None):
        all_data = version_data.copy()
        all_data['prefix'] = prefix or ''
        all_data['suffix'] = suffix or ''
        all_data['infix'] = infix or ''
        output = StringIO()
        output.write('{prefix}{version}'.format(**all_data))
        if version_data['build']:
            output.write('{infix}(build: {build}, date: {date})'.format(
                **all_data))
        output.write('{suffix}'.format(**all_data))
        return output.getvalue()

    def __call__(self, parser, namespace, values, option_string=None):
        cli_version_data = get_version_data()
        cli_version = self._format_version_data(
            cli_version_data,
            prefix='ARIA CLI ',
            infix=' ' * 5,
            suffix='\n')

        parser.exit(message='{0}'.format(cli_version))
