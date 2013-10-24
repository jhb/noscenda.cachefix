from Products.CMFCore.utils import getToolByName

def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('noscenda.cachefix_various.txt') is None:
        return
    site = context.getSite()        
    registry = getToolByName(site,'portal_registry')
    #import ipdb; ipdb.set_trace()
    value = registry.records['plone.app.caching.interfaces.IPloneCacheSettings.templateRulesetMapping'].value
    if not value.has_key('at_download'):
        value['at_download']='plone.content.file'

