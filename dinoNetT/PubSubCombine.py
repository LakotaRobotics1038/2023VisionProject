import ntcore

class NetworkTable:
    def _init_(self, dblTopic: ntcore.DoubleTopic):

        #start subscribing: the return value must be retained
        #the parameter is teh defualt vale if no value is avalible when get() is called

        slef.dblEntry - dblTopic.getEntry(0.0)

        #publish and subscribe options may be specified using PupSubOption

        self.dblEntry = dblTopic.getEntry(
            0.0, ntcore.PubSubOptions(keepDuplicates=True, pollStorage=10)
            )

        #getentryEx provides the options of using 

        self.dblEntry = dblTopic.getEntryEx("double", 0.0)


    def periodic(self):

        val = self.dblEntry.get()
        val = self.dblEntry.get(-1.0)
        val = self.dblEntry.getAsDouble()
        tsVal = self.dblEntry.getAtomic()
        tsUpdates = self.dblEntry.readQueue()


        self.dblEntry.setDefault(0.0)
        self.dblEntry.set(1.0)
        self.dblEntry.set(2.0, 0)
        time = ntcore._now()
        self.dblEntry.set(3.0, time)
