# -*- coding: utf-8 -*-
#
# File: DoormatMixin.py
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

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Doormat.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    BooleanField(
        name='showTitle',
        default="True",
        widget=BooleanField._properties['widget'](
            label="Show title in viewlet",
            description="If checked, this Doormat / Column / Section's title will be displayed in the doormat viewlet.",
            label_msgid='Doormat_label_showTitle',
            description_msgid='Doormat_help_showTitle',
            i18n_domain='Doormat',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

DoormatMixin_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class DoormatMixin(BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IDoormatMixin)

    meta_type = 'DoormatMixin'
    _at_rename_after_creation = True

    schema = DoormatMixin_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


# end of class DoormatMixin

##code-section module-footer #fill in your manual code here
##/code-section module-footer

