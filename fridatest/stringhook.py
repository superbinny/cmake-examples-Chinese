from __future__ import print_function
import frida
import sys

session = frida.attach("hi.exe")
script = session.create_script("""
//创建字符串对象
var st = Memory.allocUtf8String("TESTMEPLZ!");
var f = new NativeFunction(ptr("%s"), 'int', ['pointer']);
//调用函数
f(st);
""" % int(sys.argv[1], 16))
def on_message(message, data):
    print(message)
script.on('message', on_message)
script.load()
