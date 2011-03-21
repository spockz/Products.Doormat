from Products.CMFCore.utils import getToolByName

def install(portal):
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-Products.Doormat:default')
    return "Ran all import steps."

def uninstall(portal):
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-Products.Doormat:uninstall')
    return "Ran all uninstall steps."

