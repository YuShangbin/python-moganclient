#   Copyright 2016 Huawei, Inc. All rights reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

import logging

from nimbleclient.i18n import _LE

LOG = logging.getLogger(__name__)


def get_response_body(resp):
    body = resp.content
    if 'application/json' in resp.headers.get('content-type', ''):
        try:
            body = resp.json()
        except ValueError:
            LOG.error(_LE('Could not decode response body as JSON'))
    else:
        body = None
    return body
