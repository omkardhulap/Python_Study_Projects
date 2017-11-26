'''
Created on Oct 24, 2017

@author: omkar.d
'''

class UserDetails(object):
    '''
    Common base class for all users
    '''
    userCount = 0

    def __init__(self, name, vehicleNumber, addressLocality, mobileNo, email):
        '''
        RegisterUser User
        '''
        self.userid = 0
        self.name = name
        self.vehicleNumber = vehicleNumber
        self.addressLocality = addressLocality
        self.mobileNo = mobileNo
        self.email = email
        UserDetails.empCount += 1
        
        from dao.UserDAO import saveUserDetails
        saveUserDetails(self)
    