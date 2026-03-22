def check_user(fn):
    def inner():
        print("check user")
        fn()
    return inner

def check_code(fn):
    def inner():
        print("check code")
        fn()
    return inner

@check_user
@check_code
def comment():  #装饰流程，由内向外=> check_user(check_code(comment))
    print("commet")

comment() #执行的时候先从左到右，先check user再check code
# check user
# check code
# commet
