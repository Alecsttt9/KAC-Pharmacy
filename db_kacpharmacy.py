# -*- coding: utf-8 -*-

import datetime

db.define_table(
    'States',
    Field('name', notnull = True, unique = True),
    Field('abbreviation', notnull = True, unique = True),
    format = '%(name)s')

# This creates the Prescribers Table
db.define_table(
   'Prescribers',
   Field('firstName',  notnull = True),
   Field('lastName', notnull = True ),
   Field('deaNumber', unique = True, requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('npiNumber', notnull = True, unique = True, requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('Address', notnull = True),
   Field('phoneNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('faxNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   format = '%(lastName)s')

db.define_table(
   'Insurances',
   #Field('Insurer id', notnull = True, unique = True), 
   Field('companyName', notnull = True),
   Field('policyNumber', notnull = True),
   Field ('binNumber', requires = IS_MATCH('[\d\-\(\) ]+')), 
   Field('phoneNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('primaryCardholder', requires = IS_MATCH('[\d\-\(\) ]+')),
   )

db.define_table(
    'allergyProfiles',
    Field('Status', notnull = True),
    Field('medicationName'),
    Field('entryDate', type='datetime', default=datetime.datetime.now(), notnull = True),
    Field('Severity'),
    Field('Reaction'))

db.define_table(
   'drugSchedules',
   #Field('ID', notnull = True, unique = True),
   Field('Schedule', notnull = True),
   Field('Classification', notnull = True),
   format = '%(classification)s'
)

db.define_table(
   'Prescriptions',
   Field('rxNumber', notnull = True, unique = True),
   Field('brandName', notnull = True),
   Field('genericName', notnull = True),
   Field('DAW', notnull = True),
   Field('ndcNumber', notnull = True),
   Field('Quantity', notnull = True),
   Field('SIG', notnull = True),
   Field('Prescriber', 'reference Prescribers', notnull = True),
   Field('Refills', notnull = True),
   Field('drugSchedule', 'reference drugSchedules'),
   format = '%(rxNumber)s'
   )

db.define_table(
   'Medications',
   Field('ndcNumber', notnull = True),
   Field('brandName', notnull = True),
   Field('genericName'),
   Field('quanity'),
   Field('drugSchedule', 'reference drugSchedules')
)

db.define_table(
   'Patients',
   #Field('Contact ID', notnull = True, unique = True),
   Field('firstName'),
   Field('lastName'),
   Field('DOB'),
   Field('phoneNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('Address1'),
   Field('Address2'),
   Field('City'),
   Field('stateName', 'reference States'),
   Field('zipCode'),
   Field('Prescriber', 'reference Prescribers'), # db.Prescribers
   Field('Insurer', 'reference Insurances'), # db.Insurance
   Field('Allergies', 'reference allergyProfiles'),
   Field('Prescriptions', 'reference Prescriptions'),
   Field('leadSource', 'reference leadSource'),
   format = '%(lastName)s'  
)

db.define_table(
   'Users',
   Field('employeeID', notnull = True),
   Field('fName', notnull = True),
   Field('lName', notnull = True),
   Field('email'),
   Field('title', notnull = True),
   Field('credentials'),
   Field('userName', notnull = True),
   Field('password')
)

db.define_table(
   'fillStations',
   Field('fName', notnull = True),
   Field('lName', notnull = True),
   Field('rxNumber', 'refrence Perscriptions'),
   Field('ndcNumber'),
   Field('brandName', notnull = True),
   Field('genericName'),
   Field('SIG'),
   Field('Prescriber', 'refrence Prescribers'),
   Field('Refill'),
   Field('DAW')
)
