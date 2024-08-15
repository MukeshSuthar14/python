def give(args, cb):
    cb(args)


@give("hello", callable)
def callback():
    print("sfdfsf")