# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

@auth.requires_login()
def States():
    grid = SQLFORM.grid(db.States)
    return dict(grid=grid)

@auth.requires_login()
def Prescribers():
    grid = SQLFORM.grid(db.Prescribers)
    return dict(grid=grid)

@auth.requires_login()
def Insurances():
    grid = SQLFORM.grid(db.Insurances)
    return dict(grid=grid)

@auth.requires_login()
def allergyProfiles():
    grid = SQLFORM.grid(db.allergyProfiles)
    return dict(grid=grid)

@auth.requires_login()
def drugSchedules():
    grid = SQLFORM.grid(db.drugSchedules)
    return dict(grid=grid)

@auth.requires_login()
def Prescriptions():
    grid = SQLFORM.grid(db.Prescriptions)
    return dict(grid=grid)

@auth.requires_login()
def leadSource():
    grid = SQLFORM.grid(db.leadSource)
    return dict(grid=grid)

@auth.requires_login() 
def Patients():
    grid = SQLFORM.grid(db.Patients)
    return dict(grid=grid)

@auth.requires_login() 
def Medications():
    grid = SQLFORM.grid(db.Medications)
    return dict(grid=grid)

@auth.requires_login() 
def Users():
    grid = SQLFORM.grid(db.Users)
    return dict(grid=grid)

@auth.requires_login() 
def fillStations():
    grid = SQLFORM.grid(db.fillStations)
    return dict(grid=grid)

def testdb():
    response.view = "testdb.html";
    return locals();

def prescriberLookup():
    response.view = "prescriberLookup.html";
    return locals();

def inventoryLookup():
    response.view = "inventoryLookup.html";
    return locals();

def userProfile():
    response.view = "userProfile.html";
    return locals();

def userList():
    response.view = "userList.html";
    return locals();

def about():
    response.view = 'about.html';
    return locals();

def email():
    response.view = 'email.html';
    return locals();

def faq():
    response.view = 'faq.html';
    return locals();

def userLogin():
    response.view = 'userLogin.html';
    return locals();

def contEd():
    response.view = 'contEd.html';
    return locals();

def resetPassword():
    response.view = 'resetPassword.html';
    return locals();


def importStates():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    try:
        fp_in = open(os.path.join(request.folder, 'static', "MockStateTable.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            stateName = line[0]
            abbreviation = line[1]           
            db.States.update_or_insert(stateName=stateName, abbreviation=abbreviation)
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = "import_results.html"
    return dict()

def importPrescribers():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    try:
        fp_in = open(os.path.join(request.folder, 'static', "MockPrescribersTable.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            firstName = line[0]
            lastName = line [1]
            deaNumber = line[2]
            npiNumber = line[3]
            Address = line[4]
            phoneNumber = line[5]
            faxNumber = line[6]
            db.Prescribers.update_or_insert(firstName=firstName, lastName=lastName, deaNumber=deaNumber, Address=Address, 
			phoneNumber=phoneNumber, faxNumber=faxNumber)
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = "import_results.html"
    return dict()

def importInsurances():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    try:
        fp_in = open(os.path.join(request.folder, 'static', "MockInsurancesTable.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            companyName = line[0]
            print(companyName)
            policyNumber = line [1]
            binNumber = line[2]
            phoneNumber = line[3]
            primaryCardholder = line[4]
            db.Insurances.update_or_insert(companyName=companyName, policyNumber=policyNumber, binNumber=binNumber, phoneNumber=phoneNumber,
			primaryCardholder=primaryCardholder
			)
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = "import_results.html"
    return dict()

def importallergyProfiles():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    db.allergyProfiles.truncate()
    try:
        fp_in = open(os.path.join(request.folder, 'static', "MockallergyProfilesTable.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            medicationName = line[0]
            entryDate = line [1]
            Severity = line[2]
            Reaction = line[3]
            db.allergyProfiles.update_or_insert(medicationName=medicationName, entryDate=entryDate, Severity=Severity, Reaction=Reaction)
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = "import_results.html"
    return dict()

def importdrugSchedules():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    try:
        fp_in = open(os.path.join(request.folder, 'static', "MockdrugSchedulesTable.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            Schedule = line[0]
            Classification = line [1]
            db.drugSchedules.update_or_insert(Schedule=Schedule, Classification=Classification,)
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = "import_results.html"
    return dict()

def importPrescriptions():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    db.Prescriptions.truncate()
    try:
        fp_in = open(os.path.join(request.folder, 'static', "MockPrescriptionsTable.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            rxNumber = line[0]
            brandName = line [1]
            genericName = line[2]
            npiNumber = line[3]
            DAW = line[4]
            ndcNumber = line[5]
            Quantity = line[6]
            SIG = line[7]
            Prescriber = line[8]
            Refills = line[9]
            drugSchedule = line[10]
            db.Prescriptions.update_or_insert(rxNumber=rxNumber, brandName=brandName, genericName=genericName, npiNumber=npiNumber, 
			DAW=DAW, ndcNumber=ndcNumber, Quantity=Quantity, SIG=SIG, Prescriber=Prescriber, Refills=Refills, drugSchedule=drugSchedule )
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = "import_results.html"
    return dict()

def importMedications():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    try:
        fp_in = open(os.path.join(request.folder, 'static', "Medications.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            ndcNumber = line [0]
            brandName = line[1]
            genericName = line[2]
            Quantity = line[3]
            drugSchedule = line[4]
            db.Medications.update_or_insert(ndcNumber=ndcNumber, brandName=brandName, genericName=genericName,
			Quantity=Quantity, drugSchedule=drugSchedule)
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = "import_results.html"
    return dict()

def importleadSource():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    try:
        fp_in = open(os.path.join(request.folder, 'static', "Lead_Source.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            leadSource = line[0]
            db.leadSource.update_or_insert(leadSource=leadSource)
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = "import_results.html"
    return dict()

def importPatients():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    db.Patients.truncate()
    try:
        fp_in = open(os.path.join(request.folder, 'static', "Patients.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            firstName = line[0]
            lastName = line[1]
            DOB = line[2]
            phoneNumber = line[3]
            Address_1 = line[4]
            Address_2 = line[5]
            City = line[6]
            stateName = line[7]
            zipCode = line[8]
            Prescriber = line[9]
            Insurer = line[10]
            Allergies = line[11]
            Prescriptions = line[12]
            leadSource = line[13]
            db.Patients.update_or_insert(firstName=firstName, lastName=lastName, DOB=DOB, phoneNumber=phoneNumber, Address_1=Address_1, Address_2=Address_2, City=City, stateName=stateName, zipCode=zipCode, Prescriber=Prescriber, Insurer=Insurer, Allergies=Allergies, Prescriptions=Prescriptions, leadSource=leadSource)
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read HELLO WAYNE"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = "import_results.html"
    return dict()

def importUsers():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    db.Users.truncate()
    try:
        fp_in = open(os.path.join(request.folder, 'static', "Users.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            employeeID = line[0]
            first_name = line[1]
            last_name = line[2]
            email = line[3]
            title = line[4]
            credentials = line[5]
            userName = line[6]
            password = line[7]
            db.Users.update_or_insert(employeeID=employeeID, firstName=first_name, lastName=last_name, email=email, title=title, credentials=credentials, userName=userName, password=password)
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read HELLO WAYNE"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = "import_results.html"
    return dict()

def importfillStations():
    import csv   #for python to understand you're using csv file
    import sys
    import os
    lines = 0
    db.fillStations.truncate()
    try:
        fp_in = open(os.path.join(request.folder, 'static', "Fill_Stations.csv"),"r")
        reader =  csv.reader(fp_in)
        for line in reader:         # each line is read into a list
            firstName = line[0]
            lastName = line[1]
            rxNumber = [2]
            ndcNumber = line[3]
            brandName = line[4]
            genericName = line[5]
            SIG = line[6]
            Prescriber = line[7]
            Refill = line[8]
            DAW = line[9]
            db.fillStations.update_or_insert(firstName=firstName, lastName=lastName, rxNumber=rxNumber, ndcNumber=ndcNumber, brandName=brandName, genericName=genericName, SIG=SIG, Prescriber=Prescriber, Refill=Refill, DAW=DAW)
            lines += 1
        session.lines = lines
        response.flash = str(lines) + " lines read HELLO WAYNE"
    except Exception  as e:
        response.flash = "ERROR: " + str(e)
    #redirect(URL(r=request, f='registrationsb'))
    response.view = "import_results.html"
    return dict()


# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
