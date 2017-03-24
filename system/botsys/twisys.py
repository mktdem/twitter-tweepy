# -*- coding: utf-8 -*-

import tweepy
from ..key.keys import TwitterKeys

class TwitterSys(TwitterKeys):

	def __init__(self):
		TwitterKeys.__init__(self)
		self.__auth = tweepy.OAuthHandler(self.con_key, self.con_sec)
		self.__auth.set_access_token(self.acc_token, self.acc_tokensec)
		self.__api = tweepy.API(self.__auth)

	def api(self):
		return self.__api
	
