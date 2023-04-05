from textual.app import ComposeResult
from textual.widgets import Button, Static

class TimeDisplay(Static):
    """Empty?"""

class StopwatchWidget(Static):
    """ Stopwatch widget. """

    def compose(self) -> ComposeResult:
        """ Stopwatch yield construction. """

        yield Button("Start", id='start', variant='primary')
        yield Button("Stop", id='stop', variant='error')
        yield Button("Reset", id='reset')
        yield TimeDisplay("00:00:00.00")
