# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
Berechtigungen
"""

__author__ = "Tobias Herp <tobias.herp@visaplan.com>"
VERSION = (0,
           4,   # weitere Konstanten, vorrangig: importiert
           )
__version__ = '.'.join(map(str, VERSION))

try:
    from Products.CMFCore.permissions import (
            ManagePortal,         # 'Manage portal'
            AccessInactivePortalContent,  # 'Access inactive portal content'
            AddPortalContent,     # 'Add portal content'
            ModifyPortalContent,  # 'Modify portal content'
            ChangeLocalRoles,     # 'Change local roles'
            )
    # 'Access contents information':
    from Products.Sessions.SessionPermissions import (
            ACCESS_CONTENTS_PERM as Access_contents_information,
            )

    # Gruppenberechtigungen:
    from Products.PlonePAS.permissions import (ManageGroups, ViewGroups,
            AddGroups, DeleteGroups, SetGroupOwnership,
            )
    # sonstiges:
    from AccessControl.Permissions import (
            copy_or_move,    # Copy or Move
            delete_objects,  # Delete objects
            manage_properties,  # Manage properties
            manage_users,    # Manage users
            take_ownership,  # Take ownership
            view,            # View
            view_management_screens,  # View management screens
            )
except ImportError as e:
    print '%s:WARN %s' %(__package__, e)
# Benutzer:
ManageUsers = manage_users
# Die Berechtigungen 'Manage users', 'Manage Groups' (siehe Import oben)
# und 'unitracc: Manage courses' werden in einer vereinheitlichten
# Variablen-Konvention bereitgestellt

# Kurse (Module):
ManageCourses = intern('unitracc: Manage courses')
Access_course_documents = 'unitracc: Access course documents'

# Werbung:
Manage_Ads = 'unitracc: Manage ads'  # in @@advertisement als PERM_MANAGE

Manage_Subportals = 'unitracc: Manage subportals'
# Informationen des aktuellen Subportals auslesen:
Get_Subportal_Info = 'unitracc: Get subportal info'
# creator setzen; Plone-Berechtigungen mit 'ownership': 'Take ownership', 'Set Group Ownership'

# ------------------------------ [ Unitracc-Datentypen ... [
ADD_CONTENT_PERMISSIONS = {
    'UnitraccArticle':    'unitracc: Add UnitraccArticle',
    'UnitraccAuthor':     'unitracc: Add UnitraccAuthor',
    'UnitraccBinary':     'unitracc: Add UnitraccBinary',
    'UnitraccContact':    'unitracc: Add UnitraccContact',
    'UnitraccCourse':     'unitracc: Add UnitraccCourse',
    'UnitraccEntity':     'unitracc: Add UnitraccEntity',
    'UnitraccEvent':      'unitracc: Add UnitraccEvent',
    'UnitraccFile':       'unitracc: Add UnitraccFile',
    'UnitraccFormula':    'unitracc: Add UnitraccFormula',
    'UnitraccGlossary':   'unitracc: Add UnitraccGlossary',
    'UnitraccImage':      'unitracc: Add UnitraccImage',
    'UnitraccLiterature': 'unitracc: Add UnitraccLiterature',
    'UnitraccNews':       'unitracc: Add UnitraccNews',
    'UnitraccStandard':   'unitracc: Add UnitraccStandard',
    'UnitraccTable':      'unitracc: Add UnitraccTable',
    'UnitraccAnimation':  'unitracc: Add UnitraccAnimation',
    'UnitraccAudio':      'unitracc: Add UnitraccAudio',
    'UnitraccVideo':      'unitracc: Add UnitraccVideo',
}
IMPORT_CONTENT_PERMISSIONS = {
    'UnitraccArticle':    'unitracc: Import UnitraccArticle',
    'UnitraccAuthor':     'unitracc: Import UnitraccAuthor',
    'UnitraccBinary':     'unitracc: Import UnitraccBinary',
    'UnitraccContact':    'unitracc: Import UnitraccContact',
    'UnitraccCourse':     'unitracc: Import UnitraccCourse',
    'UnitraccEntity':     'unitracc: Import UnitraccEntity',
    'UnitraccEvent':      'unitracc: Import UnitraccEvent',
    'UnitraccFile':       'unitracc: Import UnitraccFile',
    'UnitraccFormula':    'unitracc: Import UnitraccFormula',
    'UnitraccGlossary':   'unitracc: Import UnitraccGlossary',
    'UnitraccImage':      'unitracc: Import UnitraccImage',
    'UnitraccLiterature': 'unitracc: Import UnitraccLiterature',
    'UnitraccNews':       'unitracc: Import UnitraccNews',
    'UnitraccStandard':   'unitracc: Import UnitraccStandard',
    'UnitraccTable':      'unitracc: Import UnitraccTable',
    'UnitraccAnimation':  'unitracc: Import UnitraccAnimation',
    'UnitraccAudio':      'unitracc: Import UnitraccAudio',
    'UnitraccVideo':      'unitracc: Import UnitraccVideo',
}
# ------------------------------ ] ... Unitracc-Datentypen ]

# -------------------------------------- [ aus .config ... [
Modify_Ownership_Settings = 'unitracc: Modify ownership settings'
Modify_Editorial_Settings = 'unitracc: Modify editorial settings'
MODIFY_EXPIRES='unitracc: Modify expires'     # Ablaufdatum ändern
MODIFY_EFFECTIVE='unitracc: Modify effective' # Veröffentlichungsdatum ändern
ADD_LEXICON='unitracc: Add lexicon'

# Brauchen wir wirklich eine eigene Berechtigung?!
ADD_COMMENT = 'unitracc: Add UnitraccComment'

EDIT_SOURCE = 'unitracc: Edit HTML Source'
# Verwendungszweck? Verwendung, wo?
EDIT_PUBLISHED_SIMPLE = 'unitracc: Edit published simple content'

DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
# -------------------------------------- ] ... aus .config ]

# ------------------------------------- [ Zugangscodes ... [
CREATE_TAN =  'unitracc: Create TAN'
MANAGE_TANS = 'unitracc: Manage TANs'
VIEW_TANS =   'unitracc: View TANs'
# ------------------------------------- ] ... Zugangscodes ]

# ------------------------ [ visaplan.plone.structures ... [
ADD_TO_TEMP = 'unitracc: Add to temp'
MANAGE_STRUCTURE_TYPES = 'unitracc: Manage structure types'
ADD_STRUCTURE_TYPES = 'unitracc: Add structure types'
COPY_STRUCTURE_TYPES = 'unitracc: Copy structure types'
DELETE_STRUCTURE_TYPES = 'unitracc: Delete structure types'
PUBLISH_STRUCTURE_TYPES = 'unitracc: Publish structure types'
# ------------------------ ] ... visaplan.plone.structures ]

# ----------- [ @@management (visaplan.plone.browsers) ... [
MANAGE_KEYWORDS = 'unitracc: Manage Keywords'
MANAGE_SUBMITTED_AND_ACCEPTED_CONTENT = 'unitracc: Manage submitted and accepted content'
MANAGE_ORDERS = 'unitracc: Manage Orders'
# ----------- ] ... @@management (visaplan.plone.browsers) ]

# --------------- [ @@export (visaplan.plone.pdfexport ... [
EXPORT_PDF = 'unitracc: Export PDF'
EXPORT_XML = 'unitracc: Export XML'
EXPORT_HTML = 'unitracc: Export HTML'
EXPORT_SCORM = 'unitracc: Export SCORM'
VIEW_PDF = 'unitracc: View PDF'
VIEW_XML = 'unitracc: View XML'
VIEW_SCORM = 'unitracc: View SCORM'
MANAGE_EXPORT_PROFILES = 'unitracc: Manage Export Profiles'
# --------------- ] ... @@export (visaplan.plone.pdfexport ]

# Entwicklung:
View_Development_Information = 'unitracc: View Development Information'
View_Test_Information = TEST_PERMISSION = 'unitracc: Test'
