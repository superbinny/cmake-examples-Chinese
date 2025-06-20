from __future__ import print_function
import frida
import sys

#device = frida.get_device_manager().enumerate_devices()
local = frida.get_local_device()
# a = local.get_process('test_frida.exe')
# print(a)
session = local.attach("test_frida.exe")
script = session.create_script("""
Interceptor.attach(ptr("%s"), {
    onEnter: function(args) {
        send(args[0].toInt32());
    }
});
""" % int(sys.argv[1], 16))
def on_message(message, data):
    print(message)
script.on('message', on_message)
script.load()
sys.stdin.read()
