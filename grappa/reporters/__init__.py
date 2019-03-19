from . import (
    assertion, code, diff, error, expected,
    information, message, reasons, subject,myassertion
)

# Symbols to export
__all__ = ('reporters',)
__fucked__ = ('myreporters')
# Stores error message reporters
# Reporters will be executed in definition order.
reporters = [
    assertion.AssertionReporter,
    message.MessageReporter,
    error.UnexpectedError,
    reasons.ReasonsReporter,
    expected.ExpectedMessageReporter,
    subject.SubjectMessageReporter,
    information.InformationReporter,
    diff.DiffReporter,
    code.CodeReporter,
    myassertion.MyAssertionReporter
]

myreporters = [myassertion.MyAssertionReporter]

