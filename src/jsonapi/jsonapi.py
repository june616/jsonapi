import json


class ExtendedEncoder(json.JSONEncoder):
    def default(self, obj):
        name = type(obj).__name__
        try:
            encoder = getattr(self, f"encode_{name}")
        except AttributeError:
            return super().default(obj)
        else:
            encoded = encoder(obj)
            encoded["__extended_json_type__"] = name
            return encoded

    def encode_complex(self, obj):
        return {"real": obj.real, "imag": obj.imag}

    def encode_range(self, obj):
        return {"start": obj.start, "stop": obj.stop, "step": obj.step}


class ExtendedDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        kwargs["object_hook"] = self.object_hook
        super().__init__(**kwargs)

    def object_hook(self, obj):
        try:
            name = obj["__extended_json_type__"]
            decoder = getattr(self, f"decode_{name}")
        except (KeyError, AttributeError):
            return obj
        else:
            return decoder(obj)

    def decode_complex(self, obj):
        return complex(obj["real"], obj["imag"])

    def decode_range(self, obj):
        return range(obj["start"], obj["stop"], obj.get("step", 1))


def dumps(data):
    return json.dumps(data, cls=ExtendedEncoder)


def loads(data):
    return json.loads(data, cls=ExtendedDecoder)