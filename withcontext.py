#coding=utf-8
#__author__='liufeismart'
class ContextManager(object):
    def __enter__(self):
        print("[in __enter__] acquiring resources")
    def __exit__(self, exception_type, exception_value, traceback):
        print("[in __exit__] releasing resources")
        if exception_type is None:
            print("[in __exit__] Exited without exception")
        else:
            print("[in __exit__] Exited with exception: %s" % exception_value)
            return False
with ContextManager():
    print("[in with-body] Testing")
    raise(Exception("something wrong"))