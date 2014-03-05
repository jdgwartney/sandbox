#
# events.py
#
""" API for creating Boundary Events
"""
from enum import Enum

"""
Define severity values
"""
class SEVERITY(Enum):
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

"""
Define status values
"""
class STATUS(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    ACKNOWLEDGED = 'ACKNOWLEDGED'
    OK = 'OK' 

"""
Define fields of our RawEvents
"""
class RawEvent(Enum):
    ID = 'id'
    ORGANIZATION_ID = 'organizationID'
    SEVERITY = 'severity'
    SOURCE = 'source'
    SENDER = 'sender'
    


#
# Define default values
#
__DEFAULT_SEVERITY = SEVERITY.INFO
__DEFAULT_SOURCE = 'boundary.api'
__DEFAULT_STATUS = STATUS.OK
__DEFAULT_SENDER = ''


def createEvent(organizationID,
                apiKey,
                severity=__DEFAULT_SEVERITY,
                source=__DEFAULT_SOURCE,
                status=__DEFAULT_STATUS,
                sender=__DEFAULT_SENDER):
    print(organizationID,apiKey)

