# Title     : TODO
# Objective : TODO
# Created by: dean.wright
# Created on: 25/10/2017
import asyncio
import datetime
import threading
import time


class Patient(object):
    def __init__(self, firstname, lastname, age):
        # The persons identifying attributes
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = None
        self.phone = None
        # A collection of Medications being used by the Person
        self.medications = []
        # A collection of contacts the person would like to notify of medication problems
        self.contacts = []

class Contact(object):
    def __init__(self, name, email, sms):
        self.name = name
        self.email = email
        self.sms = sms


class Medication(object):
    def __init__(self):
        # the name of the medication, this can be either the Brand or Trading name
        self.name = None
        # The strength of this prescription
        self.strength = None
        # The dosage to be used on each application or consumption e.g. 1 tablet or 10ml
        self.dosage = None
        # When to use the medication
        self.application = None
        # Is this medication prescription or over counter
        self.script = None
        # how many repeats on the script if this a prescription medication
        self.repeats = None


class DoseAlarm(threading.Thread):
    def __init__(self, alarmfor, datetime, notify):
        super(DoseAlarm, self).__init__()
        self.alarmfor = alarmfor
        self.datetime = datetime
        self.notify = notify

    def run(self):
        try:
            currenttime = datetime.datetime.now()
            timetoalarm = (self.datetime-currenttime).total_seconds()
            print(timetoalarm)
            time.sleep(timetoalarm)
            self.notify.put(self.alarmfor)
            return
        except Exception as exc:
            raise exc


class MedicationManager(object):
    def __init(self):
        # patients to manage
        self.patients = []
        #get the notification alarm notification queue ready
        self.alarms = asyncio.Queue()

        self.setup_alarms()
        #notification manager takes care of intereactions with the patient once the dosage due alarm has been raised
        self.notification_manager = NotificationManager()

        #load any existing patients

    def setup_alarms(self):
        # todo implement check for any saved patients and load an alarm for their medications
        self.alarms
        pass

    def add_patient(self, new_patient):
        #todo future version should check patient not already added
        self.patients.append(new_patient)

    def remove_patient(self, existing_patient):
        #todo if patient not in list raise patient not_found_error
        self.patients.remove(existing_patient)


class NotificationManager(object):
    def __init__(self):
        print("Time to take our medicine: ")
