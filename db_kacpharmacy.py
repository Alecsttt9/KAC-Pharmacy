# -*- coding: utf-8 -*-

# Connect to database
db = DAL('sqlite://storage.sqlite')

# This creates the Contacts Table
db.define_table(
   'Patients',
   #Field('Contact ID', notnull = True, unique = True),
   Field('First Name'),
   Field('Last Name'),
   Field('Email', requires = IS_EMAIL()),
   Field('Phone Number', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('Address One'),
   Field('Address Two'),
   Field('Prescriber', 'reference Prescriber id'), # db.Prescribers
   Field('Insurer', 'reference Insurer id'), # db.Insurance
   Field('Prescriptions'),
   format = '%(name)s'  # what is this?
)

# This creates the Insurance Table
db.define_table(
   'Insurance',
   #Field('Insurer id', notnull = True, unique = True), 
   Field('Insurer Name', notnull = True),
   Field('Address'),
   Field('Phone Number', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('Webpage'),
   Field('Email', requires = IS_EMAIL())
)

#contacts table should be renamed to 'Patients'
    #table needs to include 'Policy Number' , 'Bin Number', 'Cardholder Name' , 'DOB', 'Alergies'
db.define_table(
   'Prescribers',
   Field('prescriber ID', notnull = True, unique = True),
   Field('First Name', notnull = True 'reference company'),
   Field('Last Name', notnull = True ),
   Field('DEA number', unique = True),
   Field('NPI number', notnull = True, unique = True),
   Field('Address' notnull = True),
   Field('Phone Number', requires = IS_MATCH('[\d\-\(\) ]+'))
   Filed('Fax Number', requires = IS_MATCH('[\d\-\(\) ]+'))
   format = '%(name)s'
)

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
   Field('Drug Schedule')


db.define_table(
   'Drug Schedules',
   Field('ID', notnull = True, unique = True),
   Field('Classification Name' notnull = True),
   format = '%(name)s'
)

db.define_table(
    'Allergy Profiles'
    Field('Status')
    Field('Entry Dates')
    Field('Severity')
    Field('Raction')
    

)
