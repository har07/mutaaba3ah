#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2007 Google Inc.
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
#
import webapp2
from template_base import Handler
import tools.tools as tools
import models.models as models
from datetime import datetime
from google.appengine.ext import db

class FormHandler(Handler):
    def get(self):
        self.render("form.html", data={})

    def post(self):
        nama = self.request.get('nama')

        tanggal = self.request.get('tanggal')
        tanggal = datetime.strptime(tanggal , '%m/%d/%Y').date()

        dhuha = self.request.get('dhuha')
        dhuha = int(dhuha)

        ql = self.request.get('ql')
        ql = int(ql)

        tilawah = self.request.get('tilawah')
        tilawah = int(tilawah)

        tilawah_to = self.request.get('tilawah-to')
        tilawah_to = int(tilawah_to)

        shaum = self.request.get('shaum')
        shaum = bool(shaum)

        model = models.Entry(user_name=nama, user_id=-1, date=tanggal, dhuha=dhuha, ql=ql, tilawah_start=tilawah, tilawah_end=tilawah_to, shaum=shaum)
        model.put()

        # self.response.write(model)
        self.redirect("/search")

        # result = nama + "<br>"
        # result += tanggal + "<br>"
        # result += dhuha + "<br>"
        # result += ql + "<br>"
        # result += tilawah + "<br>"
        # result += tilawah_to + "<br>"
        # result += shaum + "<br>"
        # self.response.write(result)

    def getDefaultTemplate(self):
        path = 'odoj_template/weekly.txt'
        template, error = tools.getFileContent(path, __file__)
        if error == '':
            return template
        else:
            raise ValueError('failed to load default template: ' + error)

class SearchHandler(Handler):
    def get(self):
        self.render("search.html", data={})

    def post(self):
        name = self.request.get('nama')
        start = self.request.get('tanggal')
        end = self.request.get('tanggal-to')

        # result = name + '<br>' + start + '<br>' + end
        # self.response.write(result)

        # query = "SELECT * FROM Entry WHERE 1=1 "
        # if name and name.strip() != '':
        #     query += "AND user_name = {0} ".format(name)
        # if start and start.strip() != '':
        #     query += "AND date >= {0} ".format(start)
        # if end and end.strip() != '':
        #     query += "AND date <= {0} ".format(end)
        # query += "ORDER BY date DESC"
        query = "SELECT * FROM Entry ORDER BY date DESC"

        # self.response.write(query)

        entries = db.GqlQuery(query).fetch(100)
        self.render("search.html", data={'entries':entries})
        # self.render("search.html", data=entries)

class SampleHandler(Handler):
    def get(self):
        self.render("sample.html", data={})


app = webapp2.WSGIApplication([
    ('/', FormHandler)
    , ('/search', SearchHandler)
    , ('/sample', SampleHandler)
], debug=True)
