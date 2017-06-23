#!/usr/bin/python3

from pydbus.bus import SessionBus

if __name__ == "__main__":

    # Connect to the bus.
    bus = SessionBus()

    # Get the proxy object: bus_name, object_path
    proxy_object = bus.get("net.lew21.pydbus.ClientServerExample")

    # Show help.
    # help(proxy_object)

    # Introspection.
    # reply = proxy_object.Introspect()
    # print(reply)

    # Call the method and print the result.
    reply = proxy_object.Echo("Hello!")
    print("Method Echo returns ", reply)

    # Read the property.
    print("SomeProperty =", proxy_object.SomeProperty)

    # Set the property.
    proxy_object.SomeProperty = "World!"
    print("SomeProperty =", proxy_object.SomeProperty)

    # Quit the server.
    #reply = proxy_object.Quit()
