# -*- coding: utf-8 -*-
# admin.views
# BaseHandler
from kay.handlers import BaseHandler

import logging

from google.appengine.api import users
from google.appengine.api import memcache
from werkzeug import (
  unescape, redirect, Response,
)
from werkzeug.exceptions import (
  NotFound, MethodNotAllowed, BadRequest
)

from kay.utils import (
  render_to_response, reverse,
  get_by_key_name_or_404, get_by_id_or_404,
  to_utc, to_local_timezone, url_for, raise_on_dev
)
from kay.i18n import gettext as _
from kay.auth.decorators import admin_required


class AppHandler(BaseHandler):

  def init_handler(self):
    self.url  = self.request.url
    self.user = self.request.user
