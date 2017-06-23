#!/usr/bin/python3

from pydbus import SessionBus
from gi.repository import GLib


def callback(*args):
    print("Properties were changed: ", args)

if __name__ == "__main__":

    # Connect to the bus.
    bus = SessionBus()

    # Get the proxy object: bus_name, object_path
    proxy_object = bus.get("net.lew21.pydbus.ClientServerExample")

    # Connect to the signal.
    proxy_object.PropertiesChanged.connect(callback)

    # Start the loop.
    loop = GLib.MainLoop()
    loop.run()
