# -*- coding: utf-8 -*-
# tasky.urls
# 
# Following few lines is an example urlmapping with a newer interface.

"""
from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(Rule('/', endpoint='index', view='tasky.views.index'))
]
"""

from werkzeug.routing import EndpointPrefix, Rule

# import views
import tasky.views.top

def make_rules():
  return [
    EndpointPrefix('tasky/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'tasky/index': tasky.views.top.TopHandler(),
}
