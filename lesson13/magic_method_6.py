class CallableObject:
    def __call__(self, message):
        print(message)


if __name__ == '__main__':
    obj = CallableObject()
    obj("сообщение")
    obj("что то ещё")
    print(obj.__module__)
