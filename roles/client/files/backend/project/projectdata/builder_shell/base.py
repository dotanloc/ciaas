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

from django import forms

from project.projectdata.base import AbstractProjectData
from models import BuilderShellModel


class BuilderShellData(AbstractProjectData):

    def __init__(self, parent, formData):
        self.form = BuilderShellForm(formData)
        self.model = self.form.save(commit=False)
        self.model.parent = parent
        self.model.type = 'buildershellmodel'
        self.model.save()

    def getModel(self):
        return self.model

    def getForm(self):
        return self.form

    @staticmethod
    def getBlankForm():
        return BuilderShellForm()

    def getData(self):
        return {
            'builders': [
                {'shell': self.model.script}
            ]
        }


class BuilderShellForm(forms.ModelForm):

    class Meta:
        model = BuilderShellModel
        fields = ['script']
        widgets = {
            'script': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }
