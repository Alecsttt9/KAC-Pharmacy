# -*- coding: utf-8 -*-

# Connect to database
db = DAL('sqlite://storage.sqlite')

# This creates the Contacts Table
db.define_table(
   'Prescribers',
   #Field('Prescriber ID', notnull = True, unique = True),
   Field('First Name', notnull = True),
   Field('Last Name', notnull = True),
   Field('DEA number', unique = True, requires = IS_MATCH('[\d\-\(\) ]+'),
   Field('NPI number', notnull = True, unique = True, requires = IS_MATCH('[\d\-\(\) ]+'),
   Field('Address' notnull = True),
   Field('Phone Number', requires = IS_MATCH('[\d\-\(\) ]+'))
   Filed('Fax Number', requires = IS_MATCH('[\d\-\(\) ]+'))
   format = '%(name)s'
   )
   db.define_table(
   'Insurances',
<<<<<<< Updated upstream
   #Field('Insurer id', notnull = True, unique = True), 
   Field('Company Name', notnull = True),
   Field('Policy Number', notnull = True),
   Field ('Bin Number', requires = IS_MATCH('[\d\-\(\) ]+')), 
   Field('Phone Number', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('Primary Cardholder', requires = IS_MATCH('[\d\-\(\) ]+')),
   )
   db.define_table(
    'Allergy Profiles'
    Field('Status', notnull = True)
    Field('Medication Name')
    Field('Entry Date',type='datetime', default=datetime.datetime.now(), notnull = True)
    Field('Severity')
    Field('Raction')

db.define_table(
   'Perscriptions',
   Field('Rx Number', notnull = True) unique = True), format = '%(name)s'),
   Field('Brand Name', notnull = True),
`  Field('Generic Name', notnull = True),
   Field('DAW', notnull = True),
   Field('NDC Number', notnull = True),
   Field('Quanty', notnull = True),
   Field('SIG', notnull = True),
   Field('Prescriber', notnull = True),
`  Field('Refills', notnull = True),
   Field('Drug Schedule', 'refrence Drug Schedules')
=======
   Field('companyName', notnull = True),
   Field('primaryCardholder')),
   Field('policyNumber', notnull = True),
   Field('binNumber', requires = IS_MATCH('[\d\-\(\) ]+')), 
   Field('phoneNumber', requires = IS_MATCH('[\d\-\(\) ]+'))
   
   
db.define_table(
    'allergyProfiles',
    Field('Status', notnull = True),
    Field('medicationName', notnull = True),
    Field('entryDate', type='datetime', default=datetime.datetime.now(), notnull = True),
    Field('Severity'),
    Field('Reaction'))

db.define_table(
   'Medications'
   Field('ndcNumber', notnull = True)
   Field('brandName', notnull = True),
   Field('genericName')
   Field('quanity')
   Field('drugSchedule', 'reference drugSchedules')
)
db.define_table(
   'drugSchedules',
   #Field('ID', notnull = True, unique = True),
   Field('Schedule', notnull = True),
   Field('Classification', notnull = True),
   format = '%(classification)s'
)

db.define_table(
   'Prescriptions',
   Field('rxNumber', notnull = True, unique = True, format = '%(name)s'),
   Field('brandName', notnull = True),
   Field('genericName', notnull = True),
   Field('DAW', notnull = True),
   Field('ndcNumber', notnull = True),
    Field('SIG', notnull = True),
   Field('Quantity', notnull = True),
   Field('Prescriber', 'refrence Prescribers' notnull = True),
   Field('Refills')
   
)
>>>>>>> Stashed changes

db.define_table(
   'Drug Schedules',
   #Field('ID', notnull = True, unique = True),
   Field('Schedule' notnull = True),
   Field('Classification', notnull = True)
   format = '%(name)s'
)

db.define_table(
   'Patients',
   #Field('Contact ID', notnull = True, unique = True),
   Field('First Name'),
   Field('Last Name'),
   Field('DOB')
   Field('Phone Number', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('Address 1', 'refrence States'),
   Field('Address 2'),
   Field('Prescriber', 'reference Prescribers'), # db.Prescribers
   Field('Insurer', 'reference Insurances'), # db.Insurance
   Field('Allergies', 'refrence Allergy Profiles')
   Field('Prescriptions', 'refrence Perscriptions'),
   format = '%(name)s'  # what is this?
)

# This creates the Insurance Table

   
)

<<<<<<< Updated upstream
#contacts table should be renamed to 'Patients'
    #table needs to include 'Policy Number' , 'Bin Number', 'Cardholder Name' , 'DOB', 'Alergies'

)







=======
db.define_table(
   'Users'
   Field('employeeID', notnull = True),
   Field('fName', notnull = True),
   Field('lName', notnull = True),
   Field('email'),
   Field('title', notnull = True),
   Field('credentials'),
   Field('userName', notnull = True)
   Field('password')
)

db.define_table(
   'fillStations'
   Field('fName', notnull = True),
   Field('lName', notnull = True),
   Field('rxNumber', 'refrence Perscriptions'),
   Field('ndcNumber'),
   Field('brandName', notnull = True),
   Field('genericName'),
   Field('SIG')
   Field('Prescriber', 'refrence Prescribers'),
   Field('Refill')
   Field('DAW')
)
>>>>>>> Stashed changes
