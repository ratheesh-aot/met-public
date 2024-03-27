# Copyright © 2021 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""API endpoints for managing an engagement custom content resource."""

from http import HTTPStatus

from flask import jsonify, request
from flask_cors import cross_origin
from flask_restx import Namespace, Resource

from met_api.auth import jwt as _jwt
from met_api.exceptions.business_exception import BusinessException
from met_api.schemas.engagement_custom_content import EngagementCustomSchema
from met_api.services.engagement_custom_content_service import EngagementCustomContentService
from met_api.utils.util import allowedorigins, cors_preflight


API = Namespace('custom_content', description='Endpoints for Engagement Custom Content Management')
"""Custom exception messages
"""


@cors_preflight('GET, POST, PATCH, OPTIONS')
@API.route('')
class CustomContent(Resource):
    """Resource for managing engagement custom content."""

    @staticmethod
    @cross_origin(origins=allowedorigins())
    def get(content_id):
        """Get engagement custom content."""
        try:
            custom_content = EngagementCustomContentService().get_custom_content(content_id)
            return jsonify(EngagementCustomSchema().dump(custom_content, many=True)), HTTPStatus.OK
        except BusinessException as err:
            return str(err), err.status_code

    @staticmethod
    @cross_origin(origins=allowedorigins())
    @_jwt.requires_auth
    def post(content_id):
        """Create engagement custom content."""
        try:
            request_json = request.get_json()
            custom_content = EngagementCustomContentService().create_custom_content(content_id,
                                                                                    request_json)
            return EngagementCustomSchema().dump(custom_content), HTTPStatus.OK
        except BusinessException as err:
            return str(err), err.status_code

    @staticmethod
    @cross_origin(origins=allowedorigins())
    @_jwt.requires_auth
    def patch(content_id):
        """Update engagement custom content."""
        request_json = request.get_json()
        try:
            custom_content = EngagementCustomContentService().update_custom_content(content_id, request_json)
            return EngagementCustomSchema().dump(custom_content), HTTPStatus.OK
        except BusinessException as err:
            return str(err), err.status_code
