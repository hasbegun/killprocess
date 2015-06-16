import psutil
from _msi import PID_APPNAME
import os
from robot.running.signalhandler import signal

DEBUG = False

def listProcess(prog=None):
    """ prog: Program names. List type
        None - list all processes
        Program name - query pid by the given program name
    """
    pid=[]
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
        except psutil.NoSuchProcess:
            pass
        else:
            if prog==None:
                print(pinfo)
            else:
                for p in prog:
                    if(pinfo['name'] == p):
                        pid.append(pinfo['pid'])
    
            if DEBUG: 
                print(pinfo)

    if DEBUG: 
        print "Found {} processes: {}".format(len(pid), pid)
    
    killProcess(pid)

def killProcess(pid):
    for p in pid:
        os.kill(p, signal.SIGTERM)
        
# def on_terminate(proc):
#     print("Process {} terminated with exit code {}.".format(proc, proc.returncode))



if __name__=="__main__":
    from optparse import OptionParser
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-p", "--prog", dest="prog", help="Program name to query")

    (options, args) = parser.parse_args()
    
    if DEBUG:
        print "options.prog: {}".format(options.prog)
        print "args: {}".format(args)
    
    listProcess(args)
    