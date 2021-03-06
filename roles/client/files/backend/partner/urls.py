# Copyright IBM Corp, 2016
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing
# permissions and limitations under the License.

from django.conf.urls import url
import views

app_name = 'partner'
urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^list$', views.list, name='list_full_url'),
    url(r'^register_node$', views.registerNode, name='register_node'),
    url(r'^new$', views.newPartner, name='new'),
    url(r'^(?P<pid>[0-9]+)/partner_artifacts.yml',
        views.artifacts, name='artifacts'),
    url(r'^whitelist.txt$', views.whitelist, name='whitelist'),
    url(r'^(?P<pid>[0-9]+)/block', views.block, name='block'),
    url(r'^(?P<pid>[0-9]+)/unblock', views.unblock, name='unblock'),
]
