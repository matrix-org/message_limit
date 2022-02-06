# -*- coding: utf-8 -*-
# Copyright 2019 The Matrix.org Foundation C.I.C.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Limiter(object):
    def __init__(self, config, api):
        self.api = api
        # message length limit
        self.limit = config.get("limit", 1000)
        # list of protected rooms. Omit to protect all rooms
        self.protected_rooms = config.get("protected_rooms")

    # --- spam checker interface below here ---

    def check_event_for_spam(self, event):
        body = event.get("content", {}).get("body", "")
        room_id = event.get("room_id", "")
        if len <= self.limit:
            # below the limit, not spam
            return False  # not spam (as far as we're concerned)

        if self.protected_rooms is not None and room_id not in self.protected_rooms:
            # not in a protected room
            return False

        return True # over the limit and in a protected room


    def user_may_invite(self, inviter_user_id, invitee_user_id, room_id):
        return True  # allowed (as far as we're concerned)

    def check_username_for_spam(self, user_profile):
        return True

    def user_may_create_room(self, user_id):
        return True  # allowed

    def user_may_create_room_alias(self, user_id, room_alias):
        return True  # allowed

    def user_may_publish_room(self, user_id, room_id):
        return True  # allowed

    @staticmethod
    def parse_config(config):
        return config  # no parsing needed
