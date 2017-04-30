#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ftplib import FTP
import os

print ("""\n
			========== ================= ============
			||                 ||        ||        ||
			||                 ||        ||        ||
			||========         ||        ||=========
			||                 ||        ||
			||                 ||        ||
			||                 ||        ||
	""")

# CONNECTION
q1 = input("\n\t\t--> Make a connection to a public or private server? (PU/PV) > ")
if q1 == "PV" or q1 == "pv":
	countt = 0
	while (True):
		countt+=1
		try:
			ftpc = FTP(input("\n--> Enter the server address: "))
			break

		except KeyboardInterrupt:
			print ("\n\nYou stopped the program!")
			exit()
		except:
			print ("\nThere has been an error while connecting, check the host!\n")
			if countt >= 3:
				exitcon = input("Do you want to close the connection? (Y/N) > ")
				if exitcon == "y" or exitcon == "Y":
					exit()
				else:
					continue
	def login_pr():
		try:
			ftpc.login(input("--> Enter the user name: ") \
					, input("--> Enter the user password: "))

		except KeyboardInterrupt:
			print ("\n\nYou stopped the program!")
			exit()
		except:
			print ("\nThere has been an error, check the user or the password!\n")
			exitcon = input("Do you want to close the connection? (Y/N) > ")
			if exitcon == "Y" or exitcon == "y":
				exit()
			else:
				login_pr()
	login_pr()


elif q1 == "PU" or q1 == "pu":
	while (True):
		try:
			ftpc = FTP(input("\n--> Enter the server address: "))
			ftpc.login()
			break
		except KeyboardInterrupt:
			print ("\n\nYou stopped the program!")
			exit()
		except:
			print ("\nThere has been an error while connecting, check the host!\n")
			exitcon = input("Do you want to close the connection? (Y/N) > ")
			if exitcon == "y" or exitcon == "Y":
				exit()
			else:
				continue
else:
	print ("\n\n\t\t\tThe selected option doesn't exists!\n")
	exit()

print ("\n\n\t\t\t" + str(ftpc.getwelcome()) + "\n\n")
cwdf = ftpc.pwd()
print ("--> Actual directory: " + cwdf)
print ("--> Directory files: ")
ftpc.dir()

while (True):
	# CHANGE DIRECTORY
	def changd():
		try:
			while (True):
				cwd = input ("\n--> Change directory? (Y/N) > ")
				if cwd == "Y" or cwd == "y":
					ncwd = input("\nEnter the name of the new directory: ")
					ftpc.cwd(ncwd)
					print ("--> Directory files: ")
					ftpc.dir()
				else:
					print ("\nWill work in this directory!\n")
					break

		except KeyboardInterrupt:
			print ("\n\nYou stopped the program!")
			exit()
		except:
			print ("\nFailed to change directory, it may not exist!")
			changd()
	changd()

	gopt = input("""--> What do you want to do?: 

		[R]ead
		[C]reate
		[D]elete
		[DO]wnload
		[U]pload
		[RE]name
		[E]xit

> """)
	# READ OPTION
	if gopt == "R" or gopt == "r":
		def read0():
			countt = 0
			while (True):
				countt+=1
				try:
					nf = input("\n--> Introduce the name of the file to read: ")
					ftpc.retrlines("RETR " + nf)
					break

				except KeyboardInterrupt:
					print ("\n\nYou stopped the program!")
					exit()
				except:
					print ("Error attempting to read file, may not exist!")
					if countt >= 3:
						bropt = input("\nDo you want to 'not' read something? (Y/N) > ")
						if bropt == "Y" or bropt == "y":
							break
						else:
							continue
							read0()
					read0()
		read0()


		# READ MORE
		def rmore():
			while (True):
				aread = input("--> Do you want to read something more? (Y/N) > ")
				if aread == "Y" or aread == "y":
					try:
						nnfil = input("\n--> Introduce the name of the file to read: ")
						ftpc.retrlines("RETR " + nnfil)

					except KeyboardInterrupt:
						print ("\n\nYou stopped the program!")
						exit()
					except:
						print ("Error attempting to read file, may not exist!")
						rmore()
				else:
					break
		rmore()

	# CREATE DIRECTORY OPTION
	elif gopt == "C" or gopt == "c":
		def create():
			while (True):
				try:
					nnfold = input("\n--> Introduce the name of the new folder: ")
					ftpc.mkd(nnfold)
					caf = input("\nDo you want to create another folder? (Y/N) > ")
					if caf == "Y" or caf == "y":
						nnfold = input("\n--> Introduce the name of the new folder: ")
						ftpc.mkd(nnfold)
					else:
						break

				except KeyboardInterrupt:
					print ("\n\nYou stopped the program!")
					exit()
				except:
					print ("\nMistake on having created the folder, verifies your permissions in the servant!")
					bropt = input("\nDo you want to 'not' create something? (Y/N) > ")
					if bropt == "Y" or bropt == "y":
						break
					else:
						continue
						create()
					#create()
		create()


	# DELETE OPTION
	elif gopt == "D" or gopt == "d":
		opte = input("\n--> Do you want to delete a directory or a file? (D/F) > \n")
		if opte == "d" or opte == "D":
			def delete_dir():
				countt = 0
				while (True):
					countt+=1
					try:
						nfilel = input("\n--> Introduce the name of the directory to delete: ")
						ftpc.rmd(nfilel)

						dnd = input("\n--> Do you want to delete another directory? (Y/N) > ")
						if dnd == "Y" or dnd == "y":
							nfilel = input("\n--> Introduce the name of the directory to delete: ")
							ftpc.rmd(nfilel)
							continue
						else:
							break

					except KeyboardInterrupt:
						print ("\n\nYou stopped the program!")
						exit()
					except:
						print ("\nMistake on having deleted the folder, verifies your permissions in the servant!")
						if countt >= 3:
							optne = input("Do you want to 'not' delete a directory? (Y/N) > ")
							if optne == "Y" or optne == "y":
								break
							else:
								delete_dir()
			delete_dir()


		elif opte == "f" or opte == "F":
			def delete_file():
				countt = 0
				while (True):
					countt+=1
					try:
						nfilel = input("\n--> Introduce the name of the file to delete: ")
						ftpc.delete(nfilel)

						nfilelq = input("-->\n Do you want to delete another file? (Y/N) > ")
						if nfilelq == "Y" or nfilelq == "y":
							nfilel = input("\n--> Introduce the name of the file to delete: ")
							ftpc.delete(nfilel)
							continue
						else:
							break

					except KeyboardInterrupt:
						print ("\n\nYou stopped the program!")
						exit()
					except:
						print ("\nMistake on having deleted the file, verifies your permissions in the servant!")
						if countt >= 3:
							optne = input("Do you want to 'not' delete a file? (Y/N) > ")
							if optne == "Y" or optne == "y":
								break
							else:
								delete_file()
			delete_file()


	# DOWNLOAD OPTION
	elif gopt == "DO" or gopt == "do":
		def download0():
			countt = 0
			while (True):
				countt+=1
				try:
					nfile = input("\nIntroduce the file name to download: ")
					downf = open(nfile, 'wb')
					ftpc.retrbinary('RETR ' + nfile, downf.write)
					break

				except KeyboardInterrupt:
					print ("\n\nYou stopped the program!")
					exit()
				except:
					ftpc.abort()
					print ("Error while downloading!, try again .. ")
					if countt >= 3:
						optne = input("Do you want to 'not' download a file? (Y/N) > ")
						if optne == "Y" or optne == "y":
							break
						else:
							download0()
		download0()


	# UPLOAD OPTION
	elif gopt == "U" or gopt == "u":

		def upload0():
			nfile = input("\nIntroduce the file name: ")
			# CHECK IF FILE EXISTS OR NOT
			if os.path.isfile(nfile) == True:
				print ("...")
			elif os.path.isfile(nfile) == False:
				while os.path.isfile(nfile) == False:
					nfile = input("The indicated file does not exist!, try again: ")

					if os.path.isfile(nfile) == True:
						print ("The file exists, it will continue ...")
						continue

			try:
				file0 = open(nfile, 'rb')
				ftpc.storbinary('STOR ' + nfile, file0)

			except KeyboardInterrupt:
					print ("\n\nYou stopped the program!")
					exit()
			except:
				ftpc.abort()
				print ("Error while uploading!, try again ...")
				upload0()
		upload0()


	# RENAME OPTION
	elif gopt == "RE" or gopt == "re":
		try:
			nfile = input("Introduce the file to rename: ")
			nname = input("Introduce the new name: ")
			ftpc.rename(nfile, nname)

		except KeyboardInterrupt:
			print ("\n\nYou stopped the program!")
			exit()
		except:
			print ("There was a problem while renaming!")

	# EXIT OPTION
	elif gopt == "E" or gopt == "e":
		print ("\n\nClosing...")
		ftpc.quit()
		exit()

	# ANYTHING
	else:
		print ("\n\n\t\t\tThe selected option doesn't exists!\n")
