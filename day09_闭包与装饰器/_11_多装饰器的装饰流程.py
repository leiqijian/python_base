'''
离函数最近的装饰器先装饰，由内到外的装饰过程，执行过程从外到内
'''
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

# ######离得近的先装饰 ########

def drink_water():
    def inner(fn):
        print("drink_water")
        fn()
        return inner

def eat_meal():
    def inner(fn):
        print("eat_meal")
        fn()
        return inner

def have_fun():
    print("have_fun")

