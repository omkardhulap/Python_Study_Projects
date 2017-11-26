'''
Created on Oct 24, 2017

@author: omkar.d
'''

class RequestDetails(object):
    '''
    Common base class for all requests
    '''
    requestCount = 0


    def __init__(self, cost, totalAvailableSeats, startPoint, endPoint, route):
        '''
        create carpool request
        '''
        self.requestId = 0;
        self.cost = cost
        self.totalAvailableSeats = totalAvailableSeats
        self.occupiedSeats = 0
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.route = route
        import time
        self.time = time.time()
        RequestDetails.requestCount+=1
        
        from dao.RequestDAO import saveRequest
        saveRequest(self)
        
        
