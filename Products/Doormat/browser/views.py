from plone.memoize.instance import memoize

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from zope.component import getMultiAdapter
from pprint import pprint

class DoormatView(BrowserView):
    """
    """

    def getDoormatTitle(self):
        """
        """
        title = ''
        if self.context.getShowTitle():
            title = self.context.Title()
        return title
         
    def getDoormatData(self):
        """ Return a dictionary like this:
        data = [
            {   'column_title: 'Column One',
                'column_sections: [
                {   'section_title': 'De Oosterpoort',
                    'section_links': [
                        {   'link_title': 'Some Title',
                            'link_url': 'http://some.whe.re',
                            'link_class': 'external-link',
                            'content': 'html content',
                            },
                        ]
                    },
                ]
            },
        ]
        """
        doormat = self.context
        data = []
        # Fetch Columns
        for column in doormat.objectValues():
            column_dict = {
                'column_title': column.Title(),
                'show_title': column.getShowTitle(),
                }
            column_sections = []
            sections = column.objectValues()

            # Fetch Categories from Column
            for section in sections:
                section_dict = {
                    'section_title': section.Title(),
                    'show_title': section.getShowTitle(),
                    }
                section_links = []
                objs = section.objectValues()

                # Loop over all link object in category
                for item in objs:
                    # Use the link item's title, not that of the linked content
                    title = item.Title()
                    text = ''
                    url = ''
                    link_class = ''

                    if item.portal_type == 'DoormatReference':
                        linked_item = item.getInternal_link()
                        if not linked_item:
                            continue
                        url = linked_item.absolute_url()
                    elif item.portal_type == "Link":
                        # Link is an Archetypes link
                        url = item.getRemoteUrl
                        link_class = "external-link"
                    elif item.portal_type == "Document":
                        text = item.getText()
                    elif item.portal_type == "DoormatCollection":
                        if item.getCollection().portal_type == "Topic":
                          results = self.getCollection(item)
                      
                          # Add links from collections
                          for nitem in results:
                              obj = nitem.getObject() 
                            
                              if (item.showTime):
                                title = self.localizedTime(obj.modified()) + ' - ' + obj.title
                              else: 
                                title = obj.title
                            
                            
                              section_links.append({
                                  'content': '', 
                                  'link_url': obj.absolute_url(), 
                                  'link_title': title,
                                  'link_class': 'collection-item',
                                  })
                         
                          # Add the read more link if it is specified 
                          if item.getShowMoreLink():
                              section_links.append({
                                  'content': '',
                                  'link_url': item.getShowMoreLink().absolute_url(),
                                  'link_title': item.showMoreText,
                                  'link_class': 'read-more'
                              })  
                        
                          continue
                        else:
                          url = ''
                          text = item.id+': This is not a collection, but a ' + item.getCollection().portal_type + ' :-)'
                             
                    if not (text or url):
                        continue

                    link_dict = {
                        'content': text, 
                        'link_url': url, 
                        'link_title': title,
                        'link_class': link_class,
                        }
                    section_links.append(link_dict)
                section_dict['section_links'] = section_links
                column_sections.append(section_dict)
            column_dict['column_sections'] = column_sections
            data.append(column_dict)
        return data

    def getCollection(self, item):
      if item.limit > 0:
        results = item.getCollection().queryCatalog(sort_limit=item.limit)[:item.limit]
      else:
        results = item.getCollection().queryCatalog()
        
      return results
      
    def localizedTime(self, time):
      return getMultiAdapter((self.context, self.request), name="plone").toLocalizedTime(time)  
##code-section module-footer #fill in your manual code here
##/code-section module-footer


