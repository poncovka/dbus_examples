#!/usr/bin/python3

from pydbus import SessionBus
from pydbus.generic import signal
from gi.repository import GLib

class MyDBUSParent(object):
    """
        <node>
            <interface name='net.lew21.pydbus.ClientServerParent'>
                <method name='Echo'>
                    <arg type='s' name='a' direction='in'/>
                    <arg type='s' name='response' direction='out'/>
                </method>
            </interface>
        </node>
    """
    PropertiesChanged = signal()

    def __init__(self):
        self._someProperty = "Some initial value!"

    @property
    def SomeProperty(self):
        print("Get SomeProperty with value:", self._someProperty)
        return self._someProperty

    @SomeProperty.setter
    def SomeProperty(self, value):
        print("Set SomeProperty to value:", value)
        self._someProperty = value

        # Emit signal: Use the correct object path???
        self.PropertiesChanged.emit("net.lew21.pydbus.ClientServerExample", {"SomeProperty": self._someProperty}, [])

    def Echo(self, s):
        """Returns whatever is passed to it"""
        print("Echo was called.")
        return s

class MyDBUSService(MyDBUSParent):
    """
        <node>

            <interface name='net.lew21.pydbus.ClientServerParent'>
                <method name='Echo'>
                    <arg type='s' name='a' direction='in'/>
                    <arg type='s' name='response' direction='out'/>
                </method>
            </interface>

            <interface name='net.lew21.pydbus.ClientServerExample'>
                <method name='Quit'/>
                <property name="SomeProperty" type="s" access="readwrite">
                    <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
                </property>
            </interface>

        </node>
    """

    def __init__(self):
        super().__init__()
        self._someProperty = "Another initial value!"

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
