
from networktables import NetworkTables
from time import sleep

NetworkTables.initialize()

sd = NetworkTables.getTable('SmartDashboard')




while True:
    print (sd.putNumber('penut', 45))
    print('running')
    
    sleep(1)




















"""import ntcore
from self import self

inst = ntcore.NetworkTablesInstance.getDefault()
table = inst.getTable("datatable")

#gete a topic from a NetworkTableInstance
#the topic name in this case is the full name

dblTopic = inst.DoubleTopic("/datatable/X")

#get a topic from a NetworkTable
#the topic name in this case is the name within the table
#this line and the one above referance the same topic

dblTopic = table.getDoubleTopic("X")

#get a type - specific topic from a generic Topic

genericTopic= inst.getTopic("/datatable/X")
dblTopic = DoubleTopic(genericTopic) #the word new was infront of DoubleT.. tried to run it, came up witha syntax error




class Table:
    def _init_(self, dblTopic: ntcore.DoubleTopic):

        #start publishing; the return value must be retained (in this case, via an instance variable

        self.dblPub = dblTopic.publish()

        #publish option may be specified using PubSubOption

        self.dblPub = dblTopic.publish(ntcore.PubSubOptions(keepDublicates=True)

        #publishEx provied addional options such as setting initial properties and using a custom
        #string type for types other than raw and string is not recommended
        #the properties string must be JSON map

        self.dblPub = dblTopic.publishEx("double", '{"myprop": 5}')


    def periodic(self):

        #publish a defualt value 

        self.dblPub.setdefault(0.0)

        #publish a value with current timestamp

        slef.dblPub.set(1.0)
        self.dblPub.ser(2.0, 0) #0 = use current timestamp

        #publish a value with a specific timestamp with microsecond resolution
        #on the roboRIO, this is the same as the FPGA timestamp

        sewlf.dblPub.set(3.0, ntcore._now())

    #often not required in robot code, unlesss this class doesn't exist for the lifetime of
    #the entire robot program, then close() needs to be called to stop publishing

    def close(self):

        self.dblPub.close()"""
