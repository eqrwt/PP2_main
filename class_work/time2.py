class Time:
  def __init__(self, hours, minutes, seconds, nott):
    self.seconds = seconds
    self.minutes = minutes
    self.hours = hours
    self.notaion = nott

  def increament_min(self, minute):
    total = self.hours * 60 + self.minutes + minute
    self.hours = (total // 60) % 12
    self.minutes = total % 60
  
  def increament_sec(self, seconds):
    total = self.hours*3600 + self.minutes*60+self.seconds
    total += seconds

    self.hours = (total // 3600) % 12
    self.minutes = (total % 3600) // 60
    self.seconds = (total % 3600) % 60
  
  def decreament_sec(self, seconds):
    total = self.hours*3600 + self.minutes * 60 + self.seconds
    total -= seconds

    self.hours = (total // 3600) % 12
    self.minutes = (total % 3600) // 60
    self.seconds = (total % 3600) % 60

  def decreament_minutes(self, minute):
    total = self.hours * 60 + self.minutes - minute
    self.hours = (total // 60) % 12
    self.minutes = total % 60

  def __str__(self):
    return f"{self.hours}:{self.minutes}:{self.seconds}"
  
t1 = Time(1, 59, 59, 'AM')
print(t1.__str__())
t1.increament_sec(3695)
print(t1.__str__())
t1.increament_min(259)
print(t1.__str__())
t1.decreament_minutes(245)
print(t1.__str__())

    