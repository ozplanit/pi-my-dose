# Title     : TODO
# Objective : TODO
# Created by: dean.wright
# Created on: 25/10/2017

class Person(object):
    def __init__(self, firstname, lastname, age):
        # The persons identifying attributes
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        # A collection of Medications being used by the Person
        self.medications = []
        # A collection of contacts the person would like to notify of medication problems
        self.contacts = []


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

class DoseAlarm(object):
    def __init__(self, medications):
        self.medications = medications



