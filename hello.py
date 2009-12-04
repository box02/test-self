#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def hello():
    u = raw_input("what planet you would like to live on? ")
    print "You are now on %s.\n" % u

def curiosity():
    g = raw_input("what is your favorite programming language? ")
    print "Oh, you like %s, but mine is Python.\n" % g

if __name__ == '__main__':
	hello()
    curiosity()
    print "Have a nice day, Bye!\n"
