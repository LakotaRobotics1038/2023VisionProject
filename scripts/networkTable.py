from networkTables import NetworkTables
from time import sleep 




class visionNetAgent:
  def __init__(self, testMode):
    #to acces during test from reader program 172.16.185.181
    NetworkTables.initialize()#server = "10.10.38.2"-comp IP
    if testMode:
      NetworkTables.initialize()
    else:
      NetworkTables.initialize("10.10.38.2")

    sd = NetworkTables.getTable('SmartDashboard')

  """def putframe(self, frame):
    sd."""
  def putBox(self, box):
    print("passes box in")
#this should be put not in the network table
  def getparams(self, box):
    print("this will give us the box parameters that are technically already there")
      
