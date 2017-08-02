
from gi.repository import Gio
from pydbus.error import register_error, map_error


DOMAIN = Gio.DBusError.quark()


@register_error("net.lew21.pydbus.ClientServerExample.Error", DOMAIN, 100)
class ServerError(Exception):
	pass


@map_error("org.freedesktop.DBus.Error.ServiceUnknown")
class ServiceUnknown(Exception):
	pass
