# -*- coding: utf-8 -*-
from .base import BaseReporter


class MessageReporter(BaseReporter):

    title = 'Message'

    def run(self, error):
        show_message = any([
            self.ctx.show_message,
            self.from_operator('show_message', False)
        ])
        if not show_message:
            return
        return self.ctx.message
