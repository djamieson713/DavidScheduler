
import numpy as np

class Doctor:
    def __init__(self, identifier):
        self.id = identifier
        self.status = "available"
        self.schedule ={}
        for slot in np.arange(8.0, 17.0, .5):
            self.schedule[slot] = 'open'

    def __str__(self):
        return "Hello I am " + self.id

    def assign_schedule(self, patient, timeslot):

        if self.status == 'notavailable':
            print("This doctor is not available.")
            return False

        if self.schedule[timeslot] != 'open':
            print('This appointment time is not available.')
            return False
        else:
            self.schedule[timeslot] = patient
            return True

    def change_doctor_availability(self, status):
        self.status = status

    def show_open_appointments(self):
        for x, y in self.schedule.items():
            if y == 'open':
                print("Appointment at time: " + str(x) + " is " + y)
            else:
                print("Appointment at time: " + str(x) + " is not open")

    def show_doctor_schedule(self):
        for x, y in self.schedule.items():
            if y == 'open':
                print("Appointment at time: " + str(x) + " is " + y)
            else:
                print("Appointment at time: " + str(x) + " with patient: ")
                print(y)



