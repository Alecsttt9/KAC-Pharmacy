# -*- coding: utf-8 -*-

# Connect to database
db = DAL('sqlite://storage.sqlite')

# This creates the Patients Table
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
