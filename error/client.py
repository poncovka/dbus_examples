#!/usr/bin/python3
from gi.repository import GLib

from pydbus.bus import SessionBus
from error.errors import ServerError, ServiceUnknown

if __name__ == "__main__":

    # Connect to the bus.
    bus = SessionBus()

    # Get the proxy object: bus_name, object_path
    proxy_object = bus.get("net.lew21.pydbus.ClientServerExample")

    # Show help.
    # help(proxy_object)

    try:
        reply = proxy_object.Echo("Hello!")
        print("Method Echo returns ", reply)
    except ServerError as e:
        print("Handled exception ServerError with message '%s'" % e)
    except ServiceUnknown as e:
        print("Handled exception ServiceUnknown with message '%s'" % e)
    except GLib.Error as e:
        print("Handled GLib.Error with message '%s'" % e)

    # Quit the server.
    #reply = proxy_object.Quit()
