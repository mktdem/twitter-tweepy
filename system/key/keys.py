# -*- coding: utf-8 -*-

class TwitterKeys:
	
	def __init__(self):		
		self.__consumer_key = 'Your consumer key'
		self.__consumer_secret = 'Your consumer secret'
		self.__access_token = 'Your access token'
		self.__access_token_secret = 'Your access token'

	@property
	def con_key(self):
		return self.__consumer_key

	@property
	def con_sec(self):
		return self.__consumer_secret

	@property
	def acc_token(self):
		return self.__access_token

	@property
	def acc_tokensec(self):
		return self.__access_token_secret
