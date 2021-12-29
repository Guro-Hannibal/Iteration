import sys

demo, per_hour, hours, bonus = sys.argv


def foo(per_h, hs, bs):
    return per_h * hs + bs


print(foo(int(per_hour), int(hours), int(bonus)))
