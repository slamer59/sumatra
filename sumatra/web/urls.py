"""
Define URL dispatching for the Sumatra web interface.

:copyright: Copyright 2006-2015 by the Sumatra team, see doc/authors.txt
:license: BSD 2-clause, see LICENSE for details.
"""
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from sumatra.projects import Project
from sumatra.records import Record
from sumatra.web.views import (ProjectListView, ProjectDetailView, RecordListView,
                               RecordDetailView, DataListView, DataDetailView,
                               ImageListView, SettingsView, DiffView, image_thumbgrid, parameter_list, delete_records,
                               compare_records, show_script, datatable_record, datatable_data, datatable_image,
                               show_content)

P = {
    'project': Project.valid_name_pattern,
    'label': Record.valid_name_pattern,
}

urlpatterns = [
    url(r'^$', ProjectListView),
    url(r'^settings/$', SettingsView),
    url(r'^%(project)s/$' % P, RecordListView),
    url(r'^%(project)s/about/$' % P, ProjectDetailView),
    url(r'^%(project)s/data/$' % P, DataListView),
    url(r'^%(project)s/image/$' % P, ImageListView),
    url(r'^%(project)s/image/thumbgrid$' % P, image_thumbgrid),
    url(r'^%(project)s/parameter$' % P, parameter_list),
    url(r'^%(project)s/delete/$' % P, delete_records),
    url(r'^%(project)s/compare/$' % P, compare_records),
    url(r'^%(project)s/%(label)s/$' % P, RecordDetailView),
    url(r'^%(project)s/%(label)s/diff$' % P, DiffView),
    url(r'^%(project)s/%(label)s/diff/(?P<package>[\w_]+)*$' % P, DiffView),
    url(r'^%(project)s/%(label)s/script$' % P, show_script),
    url(r'^%(project)s/data/datafile$' % P, DataDetailView),
    url(r'^%(project)s/datatable/record$' % P, datatable_record),
    url(r'^%(project)s/datatable/data$' % P, datatable_data),
    url(r'^%(project)s/datatable/image$' % P, datatable_image),
    url(r'^data/(?P<datastore_id>\d+)$', show_content),
]

urlpatterns += staticfiles_urlpatterns()
