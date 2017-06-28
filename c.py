import sys
import pjsua as pj

Log_Value=3
on_call = None

def log_callback(level, str, len):
    print str,


class CallbckforAccount(pj.AccountCallback):

    def __init__(self, account_Count=None):
        pj.AccountCallback.__init__(self, account_Count)

    # Notification on incoming call
    def on_incoming_call(self, call):
        global on_call 
        if on_call:
            call.answer(486, "Busy")
            return

        print "Incoming call from ", call.info().remote_uri
        print "Press 'a' to answer"

        on_call = call

        call_cb = CallBackforCurrCall(on_call)
        on_call.set_callback(call_cb)

        on_call.answer(180)


# Callback to receive events from Call
class CallBackforCurrCall(pj.CallCallback):

    def __init__(self, call=None):
        pj.CallCallback.__init__(self, call)

    def on_state(self):
        global on_call
        print "Call connected with",self.call.info().remote_uri,"is",self.call.info().state_text,"last code =",self.call.info().last_code,self.call.info().last_reason

        if self.call.info().state == pj.CallState.DISCONNECTED:
            on_call = None
            print 'Current call is', on_call

 

# Function to make call
def connect_call(uri):
    try:
        print "call is connecting to", uri
        return account_C.connect_call(uri, cb=CallBackforCurrCall())
    except pj.Error, e:
        print "Details of encountered exception in making call: " + str(e)
        return None

#Main : Program starts here
#Library instance is created for lib class
lib = pj.Lib()

try:
    lib.init(log_cfg = pj.LogConfig(level=Log_Value, callback=log_callback))
    transport = lib.create_transport(pj.TransportType.UDP,pj.TransportConfig(0))
    lib.start()

    account_C = lib.create_account(pj.AccountConfig("192.168.137.1", "2020", "password"))
    acc_cb = CallbckforAccount(account_C)
    account_C.set_callback(acc_cb)
    print "\n"
    print "Status of the completed Registration =", account_C.info().reg_status, "(" + account_C.info().reg_reason + ")"    

    if len(sys.argv) > 1:
        lck = lib.auto_lock()
        on_call = connect_call(sys.argv[1])
        print 'Current call is', on_call
        del lck

    uri_sip_curr = "Current SIP URI:" + transport.info().host + ":" + str(transport.info().port)

    # Menu loop
    while True:
        print "My SIP URI is", uri_sip_curr
        print "Menu:  C=To make call type 'C', H=To hangup type 'H', A=To answer call type 'A', Q=Type 'Q' to quit"

        option = sys.stdin.readline().rstrip("\r\n")
        if option == "C":
            if on_call:
                print "User is in another call"
                continue
            print "Enter destination URI to call: ", 
            dest = sys.stdin.readline().rstrip("\r\n")
            if dest == "":
                continue
            lck = lib.auto_lock()
            on_call = connect_call(option)
            del lck

        elif option == "H":
            if not on_call:
                print "No active call"
                continue
            on_call.hangup()

        elif option == "A":
            if not on_call:
                print "No active call"
                continue
            on_call.answer(200)

        elif option == "Q":
            print "Quitting the call"
            break

    # Shutdown the library
    transport = None
    account_C.delete()
    account_C = None
    lib.destroy()
    lib = None

except pj.Error, e:
    print "Details of exception: " + str(e)
    lib.destroy()
    lib = None
