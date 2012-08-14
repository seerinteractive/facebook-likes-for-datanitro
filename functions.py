""" Facebook likes for Excel using DataNitro
    chrisl@seerinteractive.com
    http://www.seeinteractive.com/blog/get-facebook-likes-in-excel-using-datanitro
"""
import urllib2
import json

def facebook_likes(url):
    facebook_url = "https://graph.facebook.com/?ids=" + url
    raw_data = urllib2.urlopen(facebook_url).read()
    formatted_data = json.loads(raw_data)
    likes = formatted_data[url].get('shares', 0)
    return likes

