# -*- coding: utf-8 -*-
from .base import BaseReporter


class ReasonsReporter(BaseReporter):

    title = 'Reasons'

    def run(self, error):
        show_reasons = any([
            self.ctx.show_reasons,
            self.from_operator('show_reasons', False)
        ])
        if not show_reasons:
            return
        else:

          return getattr(error, 'reasons', None)
