# -*- coding: utf-8 -*-
import numbers
from ..operator import Operator


class EmptyDictOperator(Operator):
    """
    Asserts if a given subject is an empty object.

    A subject is considered empty if it's ``None``, ``0`` or ``len(subject)``
    is equals to ``0``.

    Example::

        # Should style
        [] | should.be.empty

        # Should style - negation form
        [1, 2, 3] | should.not_be.empty

        # Expect style
        tuple() | expect.to.be.empty

        # Expect style - negation form
        (1, 2, 3) | expect.to_not.be.empty
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Disable components of the report
    show_diff = False
    show_code = False
    show_expected = False
    show_info = False
    show_reasons =  False
    show_subject = False
    show_message = False
    show_assertion = False
    # Operator keywords
    operators = ('emptyDict',)

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'a value that is not "None" and its length is higher than zero'
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'The result dictionary has length of '
    )
    def match(self, subject):
        if subject is None or subject is 0:
            return True

        if subject in (True, False):
            return False

        if isinstance(subject, numbers.Number) and subject != 0:
            return False

        try:
            return len(subject) == 0
        except TypeError:
            try:
                next(subject)
            except StopIteration:
                return True
            except Exception:
                return True
        return False
