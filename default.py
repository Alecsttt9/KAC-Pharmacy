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
