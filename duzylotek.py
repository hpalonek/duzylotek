#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

try:
	ileliczb = int(raw_input('ile liczb chcesz losować? '))
	maxliczb = int(raw_input('jaka ma być maksymalna losowana liczba? '))
	if ileliczb>maxliczb:
		print 'bledne dane'
		exit()
except:
	print 'bledne dane'
	exit()

print 'ustaliles ze chcesz losować', ileliczb, ' liczby ', 'a maksymalna liczba to ', maxliczb

liczby = []
i = 0
while i < ileliczb:
	liczba = random.randint(0, maxliczb)
	
	if liczby.count(liczba)==0:
		liczby.append(liczba);
		i=i+1
	else:
		continue


for i in range(3):
	print "Wytypuj", ileliczb, "z", maxliczb, "liczb:"

	typy = set()
	i = 0
	while i < ileliczb:
		try:
			typ = int(raw_input('wytypuj liczbę '  + str(i + 1) + ': '))
			if typ not in typy:
				typy.add(typ)
				i = i + 1
			else:
				print 'powtarza sie jeszcze raz'
				continue
		except ValueError:
			print 'bledne dane'
			continue

	trafione = set(liczby) & typy

	print 'wytypowales', typy
	print 'trafione', trafione
	print 'trafiles', len(trafione), 'razy'

print 'wylosowano', liczby

