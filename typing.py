# -*- encoding: utf-8 -*-

import tkinter, inspect
import sys
import time

class Typing:

	def __init__(self, question):
		self.qcnt = 0
		self.qfcnt = 0
		self.question = question
		self.timecnt = None
		self.root = tkinter.Tk()
		self.root.title('Typing Game')
		self.root.geometry('400x300')
		self.strval = tkinter.StringVar()
		self.display = tkinter.Label(text=self.question[self.qcnt], bg='tomato', fg='white', width=50, height=3)
		self.inputbox = tkinter.Entry(width=50, textvariable=self.strval)
		self.button = tkinter.Button(text='確認', bg='tomato', fg='white', width=20)
		self.button.bind('<Button-1>', self.button_action);

	def button_action(self, e):
		if len(self.question)-1 <= self.qcnt:
			if self.strval.get() != self.question[self.qcnt]:
				self.strval.set('')
				self.qfcnt += 1
				return
			self.widget_del()
			return
		if self.strval.get() == self.question[self.qcnt]:
			self.qcnt += 1
			self.display.configure(text=self.question[self.qcnt])
		else:
			self.qfcnt += 1

		self.strval.set('')

	def widget_pack(self):
		self.display.pack(pady=20)
		self.inputbox.pack(pady=20)
		self.button.pack(pady=15)

	def widget_del(self):
		restime = round(time.time() - self.timecnt, 2)
		self.inputbox.pack_forget()
		self.button.pack_forget()
		self.display.pack_forget()
		self.display.configure(text='問題数:{}問 / 間違えた数:{}回 / 経過時間:{}秒'.format(len(self.question), self.qfcnt, restime), bg='blue')
		self.display.bind('<Button-1>', lambda e: sys.exit())
		self.display.pack(pady=80)

	def start_app(self):
		self.timecnt = time.time()
		self.root.mainloop()

if __name__ == '__main__':
	question = ['ほげ', 'ほげら', 'ほげほげ', 'ふーが']
	typing = Typing(question)
	typing.widget_pack()
	typing.start_app()