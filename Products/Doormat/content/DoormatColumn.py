# -*- coding: utf-8 -*-
#
# File: DoormatColumn.py
#
# Copyright (c) 2011 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.Doormat.content.DoormatMixin import DoormatMixin
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.folder import ATFolderSchema
from Products.Doormat.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

DoormatColumn_schema = ATFolderSchema.copy() + \
    getattr(DoormatMixin, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class DoormatColumn(ATFolder, DoormatMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IDoormatColumn)

    meta_type = 'DoormatColumn'
    _at_rename_after_creation = True

    schema = DoormatColumn_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(DoormatColumn, PROJECTNAME)
# end of class DoormatColumn

##code-section module-footer #fill in your manual code here
##/code-section module-footer

