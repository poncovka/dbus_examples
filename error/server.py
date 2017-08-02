#!/usr/bin/python3
from gi.repository import GLib

from pydbus import SessionBus
from errors import ServerError


class MyDBUSService(object):
    """
        <node>
            <interface name='net.lew21.pydbus.ClientServerExample'>
                <method name='Echo'>
                    <arg type='s' name='a' direction='in'/>
                    <arg type='s' name='response' direction='out'/>
                </method>
            </interface>
        </node>
    """
    def Echo(self, s):
        """Returns whatever is passed to it"""
        print("Echo was called, raising Exception.")
        raise ServerError("Some error!")

    def Quit(self):
        """Removes this object from the DBUS connection and exits"""
        print("Quit was called.")
        loop.quit()

if __name__ == "__main__":

    # Connect to the bus..
    bus = SessionBus()

    # Expose object one bus: bus_name, *objects
    bus.publish("net.lew21.pydbus.ClientServerExample", MyDBUSService())

    # To handle signals emitted by exported objects, or to export your own objects,
    # you need to setup an event loop.
    loop = GLib.MainLoop()
    loop.run()
