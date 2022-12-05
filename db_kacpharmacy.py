# -*- coding: utf-8 -*-

import datetime

db.define_table(
    'States',
    Field('name', unique = True),
    Field('abbreviation', unique = True),
    format = '%(name)s')

# This creates the Prescribers Table
db.define_table(
   'Prescribers',
   Field('firstName'),
   Field('lastName'),
   Field('deaNumber', unique = True, requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('npiNumber', unique = True, requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('Address'),
   Field('phoneNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('faxNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   format = '%(lastName)s')

db.define_table(
   'Insurances',
   #Field('Insurer id', notnull = True, unique = True), 
   Field('companyName'),
   Field('policyNumber'),
   Field ('binNumber', requires = IS_MATCH('[\d\-\(\) ]+')), 
   Field('phoneNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('primaryCardholder', requires = IS_MATCH('[\d\-\(\) ]+')),
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
   format = '%(classification)s'
)

db.define_table(
   'Prescriptions',
   Field('rxNumber', unique = True),
   Field('brandName'),
   Field('genericName'),
   Field('DAW'),
   Field('ndcNumber'),
   Field('Quantity'),
   Field('SIG'),
   Field('Prescriber', 'reference Prescribers'),
   Field('Refills'),
   Field('drugSchedule', 'reference drugSchedules'),
   format = '%(rxNumber)s'
   )

db.define_table(
   'Medications',
   Field('ndcNumber'),
   Field('brandName'),
   Field('genericName'),
   Field('quanity'),
   Field('drugSchedule', 'reference drugSchedules')
)
db.define_table(
    'leadSource',
    Field('leadSource', unique = True),
    format = '%(leadSource)s')

db.define_table(
   'Patients',
   #Field('Contact ID', notnull = True, unique = True),
   Field('firstName'),
   Field('lastName'),
   Field('DOB'),
   Field('phoneNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('Address_1'),
   Field('Address_2'),
   Field('City'),
   Field('stateName', 'reference States'),
   Field('zipCode'),
   Field('Prescriber', 'reference Prescribers'), # db.Prescribers
   Field('Insurer', 'reference Insurances'), # db.Insurance
   Field('Allergies', 'reference allergyProfiles'),
   Field('Prescriptions', 'reference Prescriptions'),
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
   Field('rxNumber', 'reference Prescriptions'),
   Field('ndcNumber'),
   Field('brandName'),
   Field('genericName'),
   Field('SIG'),
   Field('Prescriber', 'reference Prescribers'),
   Field('Refill'),
   Field('DAW')
)
