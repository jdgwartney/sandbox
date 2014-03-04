'''
Created on Mar 4, 2014

@author: davidg
'''

class Event(object):
    '''
    classdocs
    '''
    
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

    def __init__(self, params):
        '''
        '''
        self._severity = Event.INFO
        # TODO: If the source is not provided what should value should be used.
        self._source = 'TODO'
        self._sender = 'TODO'

        
    def organizationID(self,organizationID):
        """
        Set the organization ID of the event
        Can we set this by alias which maps to a specific organization ID and organization name
        TODO: What happens if the API key does not give access to that organization
        
        The associated organization id for this event. If not specified, organization id will be populated from the URI.
        """
        self._organizationID=organizationID
        
    def severity(self,severity):
        """
        One of INFO, WARN, ERROR, CRITICAL. Default is INFO.
        """
        self._severity = severity
        
    
    def source(self,source):
        self._source = source
        
    def sender(self,sender):
        """
        One of OPEN, CLOSED, ACKNOWLEDGED, or OK. Default is OK. Events with status
        OPEN, CLOSED, or ACKNOWLEDGED are able to be modified by the user,
        while OK status events are purely informational.
        """
        self._sender = sender
        
    def status(self,status):
        """
        One of OPEN, CLOSED, ACKNOWLEDGED, or OK. Default is OK.
        Events with status OPEN, CLOSED,or ACKNOWLEDGED are able
        to be modified by the user, while OK status events are purely informational.
        """
        self._status = status
        
    def fingerprintFields(self,fingerprintFields):
        """
        The fields of the event used to calculate the event fingerprint.
        In this field, @title refers to RawEvent.title,
        @message refers to RawEvent.message, and all other field values come
        from the properties object. Each field must have a non-null,
        non-empty field value with a basic type (string, number, or bool).
        """
        self._fingerprintFields = fingerprintFields
        
    @property
    def tags(self):
        return self._tags
        
    @tags.setter
    def tags(self, tags):
        self._tags = tags
    
        
        
    