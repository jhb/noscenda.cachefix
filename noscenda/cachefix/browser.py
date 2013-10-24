from zope.publisher.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.annotation.interfaces import IAnnotations

class CacheFix(BrowserView):

    def publishTraverse(self,request,name):
        #import ipdb; ipdb.set_trace()
        if not hasattr(self,'subpath'):
            self.subpath = []
        self.subpath.append(name)            
        #print 'in publishTraverse in ATDownload'
   
        return self        

    def at_download(self):
       # print 'atdownload in browserview'
        #import ipdb; ipdb.set_trace()
        context = self.context
        if self.subpath:
            field = context.getWrappedField(self.subpath[0])
        else:
            field= context.getPrimaryField()
        if not hasattr(field,'download'):
            from zExceptions import NotFound
            raise NotFound

        return field.download(context)      
