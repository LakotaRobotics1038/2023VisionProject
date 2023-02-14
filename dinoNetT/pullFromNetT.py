
from networktables import NetworkTables
from time import sleep


NetworkTables.initialize(server='172.16.185.112')
sd = NetworkTables.getTable('SmartDashboard')


while True:
    print ("penut", sd.getNumber('penut', 45))
    sleep(1)
    

























"""import ntcore

class Subscriber:
    def _init_(self, dblTopic: ntcore.DoubleTopic):

        #startsubscribing: the return value must be retained
        #the parameter is the defualt vale if no value os avalibe when get() is called

        self.dblSub = dbTopic.subscribe(0.0)

        #subscribe options may be specified using PubSubOption

        self.dblSub = dblTopic.subscribe(
            0.0, ntcore.PubSubOptions(keepDuplicates=True, pollStorage=10)
            )
        
        #subscribeEx provieds teh options of using a custon type string
        #using a custon type string for types other than raw and strin is not reccomended

        dblsub = dblTopic.subscribeEx("double", 0.0)

        def periodic(self):
            #simple get of most recent value; if no value has been published, returns
            #the teh defualt value passed to the subcribe() function

            val = self.dblsub.get()

            #get the most recent value; if no value has been published, returns the
            #passed -in defualt value

            val = self.dblSub.get(-1.0)

            #get teh most reason value, alkong with its timestamp

            tsVal = self.dblSub.getAtomic()

            #read all value changes since the lst call to readQueue
            #readQueue() returns timestamps

            tsUpdates = self.dblSub.readQueue

            
    #often not required in robot code, unlesss this class doesn't exist for the lifetime of
    #the entire robot program, then close() needs to be called to stop subscribing

    def close(self):

        self.dblSub.close()"""
        











