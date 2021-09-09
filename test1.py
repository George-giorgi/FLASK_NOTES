

gio = {
    "name": "giorgi",
    "lastname": "kapanadze",
    "age": 27
}
# for i in gio.values():
#     print(i)
def func(x):
    if x != 27:
        return True
    else:
        return False

result = filter(func, gio.values())

for i in result:
    print(i)


