# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class FloatPlugin(CMSPluginBase):
    model = models.FloatModel
    module = _('Layout Helpers')
    name = _("Float")
    render_template = 'float_plugin/plugins/float.html'
    allow_children = True


plugin_pool.register_plugin(FloatPlugin)