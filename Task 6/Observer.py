class Logger:

    @staticmethod
    def write_to_file(lst, file_name="events.txt"):
        f = open(file_name, 'a')
        f.write(str(lst) + '\n')
        f.close()


class Observer:
    subscriber = []

    def __init__(self):
        self.subscriber.append(self)
        self.notifier = {}

    def observe(self, event_name, callback=Logger.write_to_file):
        self.notifier[event_name] = callback


class Event:

    def log_event(self):
        for subscriber in Observer.subscriber:
            if self.name in subscriber.notifier:
                subscriber.notifier[self.name](self)

    def __init__(self, name, changes, position, changed, log=True):
        self.name = name
        self.changes = changes
        self.position = position
        self.changed = changed

        if log:
            self.log_event()

    def __str__(self):
        return "Event({}, ( {}, {}, {} )".format(self.name, self.changes, self.position, self.changed)
