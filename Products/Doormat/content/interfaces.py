# -*- coding: utf-8 -*-

from zope.interface import Interface

##code-section HEAD
##/code-section HEAD

class IDoormat(Interface):
    """Marker interface for .Doormat.Doormat
    """

class IDoormatColumn(Interface):
    """Marker interface for .DoormatColumn.DoormatColumn
    """

class IDoormatSection(Interface):
    """Marker interface for .DoormatSection.DoormatSection
    """

class IDoormatReference(Interface):
    """Marker interface for .DoormatReference.DoormatReference
    """

class IDoormatMixin(Interface):
    """Marker interface for .DoormatMixin.DoormatMixin
    """

##code-section FOOT
##/code-section FOOT