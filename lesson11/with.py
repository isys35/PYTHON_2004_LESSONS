# hosts = open("hosts", 'r')
# try:
#     for line in hosts:
#         if line.startswith("#"):
#             continue
#         print(line)
# finally:
#     hosts.close()
#

with open('hosts', "r") as hosts:
    for line in hosts:
        if line.startswith("#"):
            continue
        print(line)


class ContextIllustrator:
    def __enter__(self):
        print('entering context')

    def __exit__(self, exc_type, exc_value, traceback):
        print('leaving context')
        if exc_type is None:
            print('with no error')
        else:
            print(f'with an error ({exc_value})')


