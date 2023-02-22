from conf.conf import Configuration

class conf:
	def __init__(self):
		self.numOfNumbers = 6
		self.weiredNumbers = False
		self.maxBigNumbers = 2
		self.maxSmallNumbers = 4
            
class numbersConfiguration(Configuration):

    def __init__(self):
        self._numOfNumbers = 6
        self._weiredNumbers = False
        self._maxBigNumbers = 4
        self._maxSmallNumbers = 6

    def printConf(self):
        return "well configuration of numbers game"
   
    def getConcreteConfiguration(self):
        _conf = conf()
        return _conf
       