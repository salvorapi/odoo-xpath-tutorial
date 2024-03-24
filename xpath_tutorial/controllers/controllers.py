# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class XpathTutorial(http.Controller):
    @http.route('/xpath_tutorial/', auth='public', website=True)
    def index(self, **kw):
        return request.render("xpath_tutorial.index")

