# -*- coding: utf-8 -*-

import datetime
#test comment
db.define_table(
    'States',
    Field('name', notnull = True, unique = True),
    Field('abbreviation', notnull = True, unique = True),
    format = '%(States)s')

# This creates the Contacts Table
db.define_table(
   'Prescribers',
   Field('firstName',  notnull = True),
   Field('lastName', notnull = True ),
   Field('deaNumber', unique = True, requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('npiNumber', notnull = True, unique = True, requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('Address', notnull = True),
   Field('phoneNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('faxNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   format = '%(Prescriber)s')

db.define_table(
   'Insurances',
   Field('companyName', notnull = True),
   Field('policyNumber', notnull = True),
   Field ('binNumber', requires = IS_MATCH('[\d\-\(\) ]+')), 
   Field('phoneNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('primaryCardholder'))
   
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
   format = '%(drugSchedules)s'
)

db.define_table(
   'Prescriptions',
   Field('rxNumber', notnull = True, unique = True, format = '%(name)s'),
   Field('brandName', notnull = True),
   Field('genericName', notnull = True),
   Field('DAW', notnull = True),
   Field('ndcNumber', notnull = True),
   Field('Quantity', notnull = True),
   Field('SIG', notnull = True),
   Field('Prescriber', notnull = True),
   Field('Refills', notnull = True),
   Field('drugSchedule', 'reference drugSchedules')
)

db.define_table(
    'leadSource',
    Field('leadSource', notnull = True, unique = True),
    format = '%(leadSource)s')

db.define_table(
   'Patients',
   #Field('Contact ID', notnull = True, unique = True),
   Field('firstName'),
   Field('lastName'),
   Field('DOB'),
   Field('phoneNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('Address1', 'reference States'),
   Field('Address2'),
   Field('Prescriber', 'reference Prescribers'), # db.Prescribers
   Field('Insurer', 'reference Insurances'), # db.Insurance
   Field('Allergies', 'reference allergyProfiles'),
   Field('Prescriptions', 'reference Prescriptions'),
   Field('leadSource', 'reference leadSource'),
   format = '%(firstName)s'  
)
