'''
Created on Oct 24, 2017

@author: omkar.d
'''

class CarpoolTransaction(object):
    '''
    All the operations available related to carpool request 
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
   
    def availCarpool(self, requestId, emailId):
        import dao.RequestDAO
        request = dao.RequestDAO.getRequestById(requestId)
        if request.occupiedSeats < request.totalAvailableSeats :
            request.occupiedSeats +=1
            request.passangerList[request.occupiedSeats - 1] = emailId # list index starts with 0
            dao.RequestDAO.saveRequest(request)
            return True
        else :
            print ("Sorry!! Carpool is not available")
            return False
        
    def deleteCarpoolRequest(self): 
        import dao.RequestDAO
        return dao.RequestDAO.deleteRequestById(self)
    
    def cancelAvailedRequest(self, requestId, emailId):
        import dao.RequestDAO, time
        request = dao.RequestDAO.getRequestById(requestId)
        if time.time() < self.time :
            request.passangerList.remove(emailId)
            request.occupiedSeats -=1
            dao.RequestDAO.saveRequest(request)
            return True
        else :
            print ("Sorry!! It's too late to cancel the Carpool")
            return False
            
            
        