from time import monotonic

from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widgets import Button, Static

class TimeDisplay(Static):
    """Empty?"""

    start_time = reactive(monotonic)
    time = reactive(0.0)
    total = reactive(0.0)

    def on_mount(self) -> None:
        """ Event on when added to app. """
        self.update_timer = \
                self.set_interval(
                    1 / 60, 
                    self.update_time, 
                    pause=True
                )

    def update_time(self) -> None:
        """ Update time on widget. """
        self.time = self.total + (monotonic() - self.start_time)

    def watch_time(self, time: float) -> None:
        """ Called when time changes. """

        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(
                f"{hours:02,.0f}:"
                f"{minutes:02.0f}:"
                f"{seconds:05.2f}"
                )

    def start(self) -> None:
        """ Start (or resume) time updates. """
        self.start_time = monotonic()
        self.update_timer.resume()

    def stop(self) -> None:
        """ Stop the time display updates. """
        self.update_timer.pause()
        self.total += monotonic() - self.start_time
        self.time = self.total

    def reset(self) -> None:
        """ Reset the time display to zero. """
        self.total = 0
        self.time = 0

class StopwatchWidget(Static):
    """ Stopwatch widget. """

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """ Event Handling button press. """

        id = event.button.id
        time_display = self.query_one(TimeDisplay)

        if id == "start":
            
            time_display.start()

            self.add_class("started")

        if id == "stop":

            time_display.stop()
            
            self.remove_class("started")

        if id == "reset":
            time_display.reset()


    def compose(self) -> ComposeResult:
        """ Stopwatch yield construction. """

        yield Button("Start", id='start', variant='primary')
        yield Button("Stop", id='stop', variant='error')
        yield Button("Reset", id='reset')
        yield TimeDisplay("00:00:00.00")
