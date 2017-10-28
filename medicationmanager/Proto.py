# Title     : TODO
# Objective : TODO
# Created by: dean.wright
# Created on: 17/10/2017

from medicationmanager.services.core import Patient, Medication, Contact

# create a person *** change this to a Patient and reuse person for contacts also!!
person1 = Patient("Dean", "Wright", 45)

# create a contact for the person
contact1 = Contact("Karen", "22360223@student.uwa.edu.au", "0438749904")

#create first medication
med = Medication()
med.dosage = "2 Tablet"
med.name = "Panadiene Forte"
med.strength = "500mg"
med.application = "6hr"
med.repeats = 5
med.script = True

#create a second medication
med2 = Medication()
med2.dosage = "2 Tablet"
med2.name = "Panadiene Forte"
med2.strength = "500mg"
med2.application = "6hr"
med2.repeats = 5
med2.script = True

#add the medications to the person
person1.medications.append(med)
person1.medications.append(med2)


# start Medication manager

# Start Notifcation manager

# start UI
