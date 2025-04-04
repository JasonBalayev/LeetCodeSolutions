class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")
        
#QED
#Problem 1108 (Easy Of Defanging An IP Address) - Jason Balayev (python)