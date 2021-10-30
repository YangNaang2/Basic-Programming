class NotVerified(Exception): pass

def verify(sid, name):
    if type(sid) != int:
        print("[ERROR] type of sid is not int")
        raise NotVerified
    if len(str(sid)) != 10:
        print("[ERROR] length of sid is not 10")
        raise NotVerified
    if type(name) != str:
        print("[ERROR] type of name is not str")
        raise NotVerified
    try:
        n = str(sid)[-4:].replace("0","")[0]
    except IndexError:
        print("[ERROR] value of sid is wrong")
        raise NotVerified
    n = int(n) * 2 % 10
    if n == 0: n = 4
    print("verified, your N is", n)


book_samples = [
    {"title":"A Title", "author":"Johnson", "year":1998},
    {"title":"AnotherTitle", "author":"Sonny", "year":2003},
]
