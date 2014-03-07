'''
Created on Mar 5, 2014

@author: davidg
'''

from boundary.api.event import EventField

class EventSource(EventField):
    '''
    Implements the Source data type in Boundary Events
    
    NOTE: The varible is called _type since type is a reserved word in Python
    ''' 
    def __init__(self,ref,_type,name):
        '''
        Constructor
        
        TODO: Better type checking when constructing the object
        '''
        self.__ref = ref
        self.__type = _type
        self.__name = name
        
    @property
    def ref(self):
        return self.__ref
    
    @property
    def type(self):
        return self.__type
    
    @property
    def name(self):
        return self.__name
    
    def toJson(self):
        pass
        
        
        
    
        
    