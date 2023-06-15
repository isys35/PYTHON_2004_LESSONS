class Fixture:
    pass


def create_object(obj):
    new_obj = obj.__class__()
    for attr, value in obj.__dict__.items():
        if isinstance(value, int):
            setattr(new_obj, attr, value)
    return new_obj


if __name__ == "__main__":
    obj1 = Fixture()
    obj1.arg1 = 12
    obj1.arg2 = "string"
    obj1.some_arg = 12.33

    new_obj = create_object(obj1)
    assert new_obj.arg1 == 12
    assert not hasattr(new_obj, "arg2")
    assert not hasattr(new_obj, "some_arg")
