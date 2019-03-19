# -*- coding: utf-8 -*-
from ..empty import empty
from colora
from .assertion import AssertionReporter
import pprint

class MyAssertionReporter(AssertionReporter):
    title = ''
    template = 'The differences are indicated below:\n\t {}'

    def run(self, error):
        # Assertion expression value
        subject = self.normalize(
            self.from_operator('subject', self.ctx.subject), use_raw=False)

        # List of used keyword operators
        keywords = []
        for keyword in self.ctx.keywords:
            if type(keyword) is dict and 'operator' in keyword:
                expected = self.get_expected(
                    keyword['operator'], keyword['call'])
                keywords.append(expected or '"Empty"')
            else:
                keywords.append(keyword)

        # Compose assertion sentence
        operators = ' '.join(keywords).replace('_', ' ')

        # Assertion expression value
        s = pprint.pformat(self.ctx.subject)

        assertion = self.template.format(s)

        # Return assertion formatted sentence
        return assertion

