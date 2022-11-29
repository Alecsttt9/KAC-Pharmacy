# -*- coding: utf-8 -*-

# This creates the Contacts Table
db.define_table(
   'Prescribers',
   #Field('Prescriber ID', notnull = True, unique = True),
   Field('firstName', 'reference company', notnull = True),
   Field('lastName', notnull = True ),
   Field('deaNumber', unique = True, requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('npiNumber', notnull = True, unique = True, requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('Address' notnull = True),
   Field('phoneNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   Filed('faxNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   format = '%(name)s')

db.define_table(
   'Insurances',
   #Field('Insurer id', notnull = True, unique = True), 
   Field('companyName', notnull = True),
   Field('policyNumber', notnull = True),
   Field ('binNumber', requires = IS_MATCH('[\d\-\(\) ]+')), 
   Field('phoneNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('primaryCardholder'))
   
db.define_table(
    'Allergy Profiles',
    Field('Status', notnull = True),
    Field('medicationName'),
    Field('entryDate',type='datetime', default=datetime.datetime.now(), notnull = True),
    Field('Severity'),
    Field('Reaction'))

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
   Field('drugSchedule', 'refrence Schedule ID')
)
db.define_table(
   'Drug Schedules',
   #Field('ID', notnull = True, unique = True),
   Field('Schedule', notnull = True),
   Field('Classification', notnull = True)
   format = '%(name)s'
)

db.define_table(
   'Patients',
   #Field('Contact ID', notnull = True, unique = True),
   Field('firstName'),
   Field('lastName'),
   Field('DOB')
   Field('phoneNumber', requires = IS_MATCH('[\d\-\(\) ]+')),
   Field('Address1', 'refrence States'),
   Field('Address2'),
   Field('Prescriber', 'reference Prescribers'), # db.Prescribers
   Field('Insurer', 'reference Insurances'), # db.Insurance
   Field('Allergies', 'refrence Allergy Profiles')
   Field('Prescriptions', 'refrence Perscriptions'),
   format = '%(name)s'  
)

# This creates the Insurance Table

   


#contacts table should be renamed to 'Patients'
    #table needs to include 'Policy Number' , 'Bin Number', 'Cardholder Name' , 'DOB', 'Alergies'









