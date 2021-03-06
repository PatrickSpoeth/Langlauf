import datetime
from enum import Enum
import uuid

'''
Created on 04.05.2015

@author: Patrick Spoeth
'''

class eGender(Enum):
    undefined = 0
    female = 1
    male = 2

class cParticipant(object):
    '''
    classdocs
    '''

    uuid = property(getUuid, None, None, None)
    firstName = property(getFirstName, setFirstName, None, None)
    gender = property(getGender, setGender, None, None)
    lastName = property(getLastName, setLastName, None, None)
    team = property(getTeam, setTeam, None, None)

    def __init__(self, 
                 sFirstName="", 
                 sLastName="", 
                 sTeam="", 
                 sGender="",
                 iBirthYear=1900, 
                 iBirthMonth=1, 
                 iBirthDay=1
                 ):
        '''
        Constructor
        '''
        
        self.__uuid = uuid.uuid4()
        
        self.firstName = sFirstName
        self.lastName = sLastName
        self.team = sTeam
        self.gender = sGender
        self.birthday = datetime.date()

    def getGender(self):
        return self.__gender


    def getUuid(self):
        return self.__uuid


    def getFirstName(self):
        return self.__firstName
    
    
    def getFullName(self):
        return '%s %s'%(self.firstName, self.lastName)


    def getLastName(self):
        return self.__lastName


    def getTeam(self):
        return self.__team


    def setFirstName(self, value):
        self.__firstName = value


    def setGender(self, value):
        # dictionary firstCharakter->genderEnum
        dCharToGender = {'m': eGender.male,
                         'w': eGender.female,
                         'f': eGender.female
                         }
        
        # convert to lower characters
        #   and append space, so that string has at least length 1
        value = value.lower() + ''


        self.__gender = dCharToGender.get(value[0])


    def setLastName(self, value):
        self.__lastName = value
        

    def setTeam(self, value):
        self.__team = value
    
    
        
    