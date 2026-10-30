
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        hours = self.hours + other.hours
        minutes = self.minutes + other.minutes
        seconds = self.seconds + other.seconds

        if seconds >= 60:
            seconds -= 60
            minutes += 1

        if minutes >= 60:
            minutes -= 60
            hours += 1

        return Time(hours, minutes, seconds)

    def increment(self):
        self.seconds += 1

        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1

    def __gt__(self, other):
        return (self.hours, self.minutes, self.seconds) > (
            other.hours, other.minutes, other.seconds
        )

    def __str__(self):
        return f"{self.hours}:{self.minutes:02d}:{self.seconds:02d}"


t1 = Time(1, 50, 0)
t2 = Time(1, 20, 0)

print("Time 1:", t1)
print("Time 2:", t2)
print("Sum:", t1 + t2)

t1.increment()
print("After increment:", t1)

print("Is Time 1 greater than Time 2?", t1 > t2)
