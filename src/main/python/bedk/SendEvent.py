'''
Created on Mar 6, 2014

@author: davidg
'''

from boundary.api.event import Event
from boundary.api.event import EventConnection

        
def main():
    con = EventConnection()
    e = Event()
    
    con.sendEvent(event)

if __name__ == '__main__':
    main()
