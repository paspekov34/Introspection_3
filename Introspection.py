import pprint


def introspection_info(obj):
    info = {
        "type": type(obj).__name__,
        "attributes": [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        "methods": [attr for attr in dir(obj) if callable(getattr(obj, attr))],
        "module": getattr(obj, '__module__', None)
    }
    return info


number_info = introspection_info(42)
pprint.pprint(number_info)
