'''
Created on Mar 4, 2014

@author: davidg
'''


from enum import Enum, unique

@unique
class EventSeverity(Enum):
    '''
    Define the Boundary Event severity values
    
    TODO: These could be driven by configuration by using pickling??
    '''

    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'


def main():
    print(list(EventSeverity))
    for name, member in EventSeverity.__members__.items():
        print(name, member)
    print(type(EventSeverity))
    print(type(EventSeverity['CRITICAL']))

    
if __name__ == '__main__':
    main()

        