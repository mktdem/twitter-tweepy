# -*- coding: utf-8 -*-

import tweepy
import tkinter
import tkinter.filedialog as tf
import system.botsys.twisys as twitter

class TweetSys:

	def __init__(self):
		self.api = twitter.TwitterSys().api()
		self.root = tkinter.Tk()
		self.root.title('easy tweet')
		self.root.geometry('400x350')
		self.filepath = None
		self.strval = tkinter.StringVar()
		self.strval2 = tkinter.StringVar()
		self.strval3 = tkinter.StringVar()
		self.tweetbox = tkinter.Entry(self.root, width=50, textvariable=self.strval)
		self.delbox = tkinter.Entry(self.root, width=30, textvariable=self.strval3)
		self.imgselect = tkinter.Button(self.root, text='・・・', width=8, bg='#5d8cd8', fg='white')
		self.display = tkinter.Label(self.root, bg='#5d8cd8', fg='white', width=50, height=3, textvariable=self.strval2)
		self.tweetbtn = tkinter.Button(self.root, text='ツイート', width=13, bg='#5d8cd8', fg='white')
		self.delbtn = tkinter.Button(self.root, text='ツイート削除', width=13, bg='#5d8cd8', fg='white')
		self.setwid_event()
		self.widget_pack()

	def tweet(self, e):
		try:
			if self.strval.get() != '' and (self.filepath == None or self.filepath == ''):
				self.api.update_status(self.strval.get())
				self.strval.set('')

			elif self.strval.get() == '' and (self.filepath != None or self.filepath != ''):
				self.api.update_with_media(filename=self.filepath)
				self.filepath = None

			elif self.strval.get() != '' and (self.filepath != None or self.filepath != ''):
				self.api.update_with_media(filename=self.filepath, status=self.strval.get())
				self.filepath = None
				self.strval.set('')

		except Exception:
			self.strval2.set('ツイートできませんでした')
			self.strval.set('')
		else:
			self.strval2.set('ツイート成功しました')

	def del_tweet(self, e):
		cnt = 0
		lplen = self.strval3.get()

		if lplen.isdigit():
			lplen = int(lplen)

			def _innerdel(_self):
				nonlocal cnt
				status = _self.api.home_timeline()
				for _ in status:
					if cnt == lplen-1: return True
					_self.api.destroy_status(_.id)
					cnt += 1
			try:
				while True:
					if _innerdel(self) is True: break
					_innerdel(self)

			except Exception as e:
				print(e)
				self.strval2.set('ツイート削除失敗しました')
			else:
				self.strval2.set('ツイート削除完了')
		else:
			self.strval2.set('削除したいツイート数を設定してください')

	def inp_filepath(self, e):
		self.filepath = tf.askopenfilename()
		self.strval2.set(self.filepath)

	def setwid_event(self):
		self.imgselect.bind('<Button-1>', self.inp_filepath)
		self.tweetbtn.bind('<Button-1>', self.tweet)
		self.delbtn.bind('<Button-1>', self.del_tweet)

	def widget_pack(self):
		self.tweetbox.grid(row=0, columnspan=2, padx=20, pady=30)
		self.delbox.grid(row=1, column=0, pady=20)
		self.imgselect.grid(row=1, column=1)
		self.display.grid(row=2, columnspan=2, padx=20)
		self.tweetbtn.grid(row=3, column=0, pady=20)
		self.delbtn.grid(row=3, column=1)

	def start_app(self):
		self.root.mainloop()

if __name__ == '__main__':
	app = TweetSys()
	app.start_app()