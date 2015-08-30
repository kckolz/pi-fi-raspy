# main.py -- this is what gets run, bruh
from app import PifiApp

# executed when device starts up
def main():

    print("Starting up.") #debug

    #instantiate new RiskbandApp obj & start it
    app = PifiApp()

    app.login()
    app.getUserByBluetooth('JSOINDFLISHDFLJSLIDF')
    trackUrl = app.getTrack('2daZovie6pc2ZK7StayD1K')
    app.playTrack(trackUrl)

if __name__ == "__main__": 
  main()