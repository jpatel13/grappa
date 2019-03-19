# -*- coding: utf-8 -*-
from .base import BaseReporter


class InformationReporter(BaseReporter):

    title = 'Information'

    def run(self, error):
        show_info = any([
            self.ctx.show_info,
            self.from_operator('show_info', False)
        ])
        if not show_info:
            return
        return self.from_operator('information', None)
