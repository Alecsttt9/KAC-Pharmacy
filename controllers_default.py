def States():
    grid = SQLFORM.grid(db.States)
    return dict(grid=grid)

def Prescribers():
    grid = SQLFORM.grid(db.Prescribers)
    return dict(grid=grid)

def Insurances():
    grid = SQLFORM.grid(db.Insurances)
    return dict(grid=grid)

def allergyProfiles():
    grid = SQLFORM.grid(db.allergyProfiles)
    return dict(grid=grid)

def drugSchedules():
    grid = SQLFORM.grid(db.drugSchedules)
    return dict(grid=grid)

def Prescriptions():
    grid = SQLFORM.grid(db.Prescriptions)
    return dict(grid=grid)

def leadSource():
    grid = SQLFORM.grid(db.leadSource)
    return dict(grid=grid)

def Patients():
    grid = SQLFORM.grid(db.Patients)
    return dict(grid=grid)


