# Copyright 2022 Clivern
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

from django.db import models


class Server(models.Model):
    """Server Model"""

    name = models.CharField(max_length=100, verbose_name="Name")
    uuid = models.CharField(max_length=60, db_index=True, verbose_name="uuid")
    hostname = models.CharField(max_length=100, verbose_name="Hostname")
    ipaddress = models.CharField(max_length=100, verbose_name="IP Address")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    @property
    def tags(self):
        return []

    @property
    def keys(self):
        return []

    def __str__(self):
        return self.uuid

    class Meta:
        db_table = "app_server"
