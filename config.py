
import sys
import os
import datetime
import time
import copy

from ctypes import *
import pyauto
from keyhac import *
from ctypes import *

#
# keyhac_config_Jis_Muhenkan2 config.py
# Simple版より変更,増えたキーカスタマイズ
# 
# ; : [ ] @ これら5つのキーを特殊な用途で使う為に他のキーにリマップした
# 
# ;単独でime_off
# :単独でime_on
# ]単独でEnter
# 
# 無変換+
# 2="
# 8=[{
# 9=]}
# 0=@`
# @=Tab
# ,=;+
# .=:*
# /=Apps
# T=Launcher1
# [=Launcher2
#

def configure(keymap):

	# User modifier key definition
	keymap.defineModifier( 29, "User0" ) # 無変換をモディファイアキーUser0にする


	def switch_ime(flag):
		if flag:
			ime_status = 1
		else:
			ime_status = 0

		# IMEのON/OFFをセット
		keymap.wnd.setImeStatus(ime_status)

	def ime_on():
		switch_ime(True)

	def ime_off():
		switch_ime(False)

	if 1:
		#User0（無変換） との組み合わせでカーソル移動や文字の削除やコピペを実現する
		#1-254
		#ABCDEFGHIJKLMNOPQRSTUVWXYZ@1234567890
		#       HIJKL NOP    U   Y @            カーソル移動用キー
		#A CDEFG          RS  V X Z 1 34567     Ctrl+で使うキー
		# B          M   Q  T  W     2     890 その他の機能で使うキー
		keymap_global = keymap.defineWindowKeymap()
		for i in range(253):
			keymap_global["User0-(" + str(i+1) + ")"] = "RCtrl-("+ str(i+1)+ ")"
		for i in range(253):
			keymap_global["LShift-User0-(" + str(i+1) + ")"] = "LShift-RCtrl-("+ str(i+1)+ ")"
		for i in range(253):
			keymap_global["RShift-User0-(" + str(i+1) + ")"] = "RShift-RCtrl-("+ str(i+1)+ ")"
		#
		keymap_global["User0-" + "Atmark"] = "Tab"	# 無+@ Tab
		keymap_global["User0-" + "I"] = "Up"
		keymap_global["User0-" + "J"] = "Left"
		keymap_global["User0-" + "K"] = "Down"
		keymap_global["User0-" + "L"] = "Right"
		keymap_global["User0-" + "U"] = "Home"
		keymap_global["User0-" + "O"] = "End"
		keymap_global["User0-" + "Y"] = "PageUp"
		keymap_global["User0-" + "P"] = "PageDown"
		keymap_global["User0-" + "H"] = "Back"
		keymap_global["User0-" + "N"] = "Enter"
		#
		keymap_global["LShift-User0-" + "Atmark"] = "LShift-Tab"	# S+無+@ S+Tab
		keymap_global["LShift-User0-" + "I"] = "LShift-Up"
		keymap_global["LShift-User0-" + "J"] = "LShift-Left"
		keymap_global["LShift-User0-" + "K"] = "LShift-Down"
		keymap_global["LShift-User0-" + "L"] = "LShift-Right"
		keymap_global["LShift-User0-" + "U"] = "LShift-Home"
		keymap_global["LShift-User0-" + "O"] = "LShift-End"
		keymap_global["LShift-User0-" + "Y"] = "LShift-PageUp"
		keymap_global["LShift-User0-" + "P"] = "LShift-PageDown"
		keymap_global["LShift-User0-" + "H"] = "LShift-Back"
		keymap_global["LShift-User0-" + "N"] = "LShift-Enter"
		#
		keymap_global["RShift-User0-" + "Atmark"] = "RShift-Tab"	# S+無+@ S+Tab
		keymap_global["RShift-User0-" + "I"] = "RShift-Up"
		keymap_global["RShift-User0-" + "J"] = "RShift-Left"
		keymap_global["RShift-User0-" + "K"] = "RShift-Down"
		keymap_global["RShift-User0-" + "L"] = "RShift-Right"
		keymap_global["RShift-User0-" + "U"] = "RShift-Home"
		keymap_global["RShift-User0-" + "O"] = "RShift-End"
		keymap_global["RShift-User0-" + "Y"] = "RShift-PageUp"
		keymap_global["RShift-User0-" + "P"] = "RShift-PageDown"
		keymap_global["RShift-User0-" + "H"] = "RShift-Back"
		keymap_global["RShift-User0-" + "N"] = "RShift-Enter"
		#
		keymap_global["User0-" + "B"] = keymap.command_ClipboardList
		keymap_global["User0-" + "M"] = "RWin-Tab"
		keymap_global["User0-" + "Q"] = "Esc"
		keymap_global["User0-" + "W"] = "Alt","Down"
		#
		keymap_global["User0-" + "0"] = "Atmark"				# 無+0   Atmark
		keymap_global["LShift-User0-" + "0"] = "RShift-Atmark"	# S+無+0 `
		keymap_global["User0-" + "2"] = "RShift-2"				# 無+2 "
		keymap_global["User0-" + "8"] = "(219)"					# 無+8 bracket 角括弧 [
		keymap_global["User0-" + "9"] = "(221)"					# 無+9 bracket 角括弧 ]
		keymap_global["LShift-User0-" + "8"] = "RShift-(219)"	# 無+8 brace波括弧 {
		keymap_global["LShift-User0-" + "9"] = "RShift-(221)"	# 無+9 brace波括弧 }
		keymap_global["User0-" + "(188)"] = "SemiColon"			# 無+, ;
		keymap_global["User0-" + "(190)"] = "Colon"				# 無+. :
		keymap_global["LShift-User0-" + "(188)"] = "RShift-SemiColon"	# S+無+, +
		keymap_global["LShift-User0-" + "(190)"] = "RShift-Colon"		# S+無+. *
		keymap_global["SemiColon"] = ime_off		# ; ime_off
		keymap_global["Colon"] = ime_on 			# : ime_on
		keymap_global["(221)"] = "Enter"	# 無+] Enter
		keymap_global["LShift-" + "(221)"] = "RShift-Enter"	# S+無+] S+Enter
		keymap_global["User0-" + "Slash"] = "Apps"	# 無+/ APPS
		keymap_global["LShift-User0-" + "Slash"] = "Apps"	# 無+/ APPS
		# 無+T Launcher起動
		#keymap_global["User0-" + "T"] = keymap.ShellExecuteCommand(None,"V:\Autoit3\install\AutoIt3_x64.exe","V:\ScriptAsrocLauncher\menulist20221203Simple.au3","")
		# 無+[ Launcher起動 ぷちらんちゃー "無+@"でタブ移動し"無+K"でリストを選び"]"で実行
		#keymap_global["User0-" + "(219)"] = keymap.ShellExecuteCommand(None,"V:\_Launcher_ptlnc67i\ptlnc.exe","","")
		