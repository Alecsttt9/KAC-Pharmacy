# -*- coding: utf-8 -*-

import datetime

db.define_table(
    'States',
    Field('stateName'),
    Field('abbreviation'),
    format = '%(stateName)s')

# This creates the Prescribers Table
db.define_table(
   'Prescribers',
   Field('firstName'),
   Field('lastName'),
   Field('deaNumber'),
   Field('npiNumber'),
   Field('Address'),
   Field('phoneNumber'),
   Field('faxNumber'),
   format = '%(lastName)s')

db.define_table(
   'Insurances',
   #Field('Insurer id', notnull = True, unique = True), 
   Field('companyName'),
   Field('policyNumber'),
   Field ('binNumber'), 
   Field('phoneNumber'),
   Field('primaryCardholder')
   )

db.define_table(
    'allergyProfiles',
    Field('Status'),
    Field('medicationName'),
    Field('entryDate', type='datetime', default=datetime.datetime.now()),
    Field('Severity'),
    Field('Reaction'))

db.define_table(
   'drugSchedules',
   #Field('ID', notnull = True, unique = True),
   Field('Schedule'),
   Field('Classification'),
   format = '%(Classification)s'
)

db.define_table(
   'Prescriptions',
   Field('rxNumber'),
   Field('brandName'),
   Field('genericName'),
   Field('DAW'),
   Field('ndcNumber'),
   Field('Quantity'),
   Field('SIG'),
   Field('Prescriber'),
   Field('Refills'),
   Field('drugSchedule'),
   format = '%(rxNumber)s'
   )

db.define_table(
   'Medications',
   Field('ndcNumber'),
   Field('brandName'),
   Field('genericName'),
   Field('quanity'),
   Field('drugSchedule')
)
db.define_table(
    'leadSource',
    Field('leadSource'),
    Field('leadSource'),
    format = '%(leadSource)s')

db.define_table(
   'Patients',
   #Field('Contact ID', notnull = True, unique = True),
   Field('firstName'),
   Field('lastName'),
   Field('DOB'),
   Field('phoneNumber'),
   Field('Address_1'),
   Field('Address_2'),
   Field('City'),
   Field('stateName'),
   Field('zipCode'),
   Field('Prescriber'), # db.Prescribers
   Field('Insurer'), # db.Insurance
   Field('Allergies'),
   Field('Prescriptions'),
   Field('leadSource'),
   format = '%(lastName)s'
)

db.define_table(
   'Users',
   Field('employeeID'),
   Field('firstName'),
   Field('lastName'),
   Field('email'),
   Field('title'),
   Field('credentials'),
   Field('userName'),
   Field('password')
)

db.define_table(
   'fillStations',
   Field('firstName'),
   Field('lastName'),
   Field('rxNumber'),
   Field('ndcNumber'),
   Field('brandName'),
   Field('genericName'),
   Field('SIG'),
   Field('Prescriber'),
   Field('Refill'),
   Field('DAW')
)
