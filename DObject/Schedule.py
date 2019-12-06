from DObject.Patient import Patient
from DObject.Doctor import Doctor
import numpy as np

identifiers = ['Doctor David', 'Doctor Trang', 'Doctor Kyle']

class Schedule:

    def __init__(self):
        self.practice = []
        self.patients = []
        for doctorname in identifiers:
            doctor = Doctor(doctorname)
            self.practice.append(doctor)

    def schedule_operations(self):
        opcode = 0
        while opcode != 6:
            print("What would you like to do?")
            print("1 = Schedule a new patient")
            print("2 = Show which doctors are available")
            print("3 = Show the schedule of a particular doctor")
            print("4 = Print out all the doctor's schedules")
            print("5 = Change doctor availabilty")
            print("6 = Exit the program")
            opcode = input()
            opcode = int(opcode)
            if opcode == 1:
                patient = self.make_patient()
                self.patients.append(patient)
                doctor = self.select_available_doctors()
                doctor.show_open_appointments()
                timeslot = input("What time would you like, or exit to cancel?")
                if timeslot != "cancel":
                    result = doctor.assign_schedule(patient, float(timeslot))
                    if result:
                        print("Appointment confirmed!")
            elif opcode == 2:
                self.print_all_doctor()
            elif opcode == 3:
                #show a particular doctors schedule and the patient information for each booked timeslot
                self.show_doctor_schedule_for_doctors()
            elif opcode == 4:
                for doctor in self.practice:
                    print(doctor.id)
                    doctor.show_doctor_schedule()
                    print('')
            elif opcode == 5:
                self.select_doctor_and_change()


    def get_name(self):
        name = input("What's your name: ")
        print("hello " + name)
        return name

    def get_age(self):
        age = input("what's your age:")
        print(age + " ...you're a spring chicken!")
        return age

    def get_problem(self):
        problems = []
        state = True
        while state:
            problem = input("What problem should I record?, if done type exit")
            if problem != "exit":
                problems.append(problem)
            else:
                state = False
        return problems

    def make_patient(self):
        name = self.get_name()
        age = self.get_age()
        problem = self.get_problem()
        patient = Patient(name, age, problem)
        return patient

    def get_doctor_name(self):
        self.print_all_doctor()
        doctorname = input("Type in the name of the doctor you want to see today.")

        return doctorname

    def make_doctor(self):
        name = self.get_doctor_name()
        doctor = Doctor(name)
        return doctor




    def select_doctor_and_change(self):
        self.print_all_doctor()
        docno = input("Enter the doctor number whose availability you want to change or -1 to exit")
        docno = int(docno)
        if docno == -1:
            return
        if docno < len(self.practice):
            self.change_availabilty(self.practice[docno])
            self.print_all_doctor()

    def change_availabilty(self, doctor):
        if doctor.status == 'available':
            doctor.change_doctor_availability('notavailable')
        else:
            doctor.change_doctor_availability('available')

    def print_all_doctor(self):
        counter = 0;
        for doctor in self.practice:
            print(str(counter) + ": " + doctor.id + " with status = " + doctor.status)
            counter = counter + 1

    def show_doctor_schedule_for_patients(self):
        self.print_all_doctor()
        docno = input("Enter the doctor number whose schedule you want to see or -1 to exit.")
        docno = int(docno)
        if docno == -1 or docno >= len(self.practice):
            return
        else:
            self.practice[docno].show_open_appointments()

    def show_doctor_schedule_for_doctors(self):
        self.print_all_doctor()
        docno = input("Enter the doctor number whose schedule you want to see or -1 to exit.")
        docno = int(docno)
        if docno == -1 or docno >= len(self.practice):
            return
        else:
            self.practice[docno].show_doctor_schedule()

    def select_available_doctors(self):
        self.print_all_doctor()
        docno = input("Select the doctor you would like to see today  or -1 to exit.")
        docno = int(docno)
        if docno == -1 or docno >= len(self.practice):
            return None
        elif self.practice[docno].status != "available":
            return None
        else:
            return self.practice[docno]

s = Schedule()
p = Patient("David Jamieson", 26, ["Psoriasis", "Leg pain"])
s.schedule_operations()

