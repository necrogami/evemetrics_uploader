import sys, os, time, traceback, platform

from .generic import FileMonitor
from threading import Thread
import logging
class MonitorFactory( object ):
    
    def __init__( self, monitorClass, valid_paths, options ):
        #Thread.__init__( self )
        self.processor = None
        self.valid_paths = valid_paths
        self.monitorClass = monitorClass
        self.children = []

        for path in self.valid_paths:
            # the children emit signals to this factor to communicate back changes
            self.children.append( self.monitorClass( self, path, options ) )
    def stop( self ):
      for monitor in self.children:
        monitor.__del__()
        monitor.join()
        
    def Run( self ):
        for child in self.children:
            child.Run()

    def setProcessor( self, processor ):
        self.processor = processor