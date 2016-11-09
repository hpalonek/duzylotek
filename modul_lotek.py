#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

def ustawienia():
	while 1:
		try:
			ileliczb = int(raw_input('Ile liczb chcesz losować? '))
			maxliczb = int(raw_input('Jaka ma być maksymalna losowana liczba? '))
			ilelos = int(raw_input('Ile razy chcesz typowac? '))
			if ileliczb>maxliczb:
				print 'bledne dane'
				exit()
			return (ileliczb, maxliczb, ilelos)
		except:
			print 'bledne dane'
			continue	

def losowanie(ileliczb, maxliczb):
	liczby = []
	i = 0
	while i < ileliczb:
		liczba = random.randint(0, maxliczb)
	
		if liczby.count(liczba)==0:
			liczby.append(liczba)
			i=i+1
	return liczby

def typowanie(ileliczb, maxliczb):
	print "Wytypuj", ileliczb, "z", maxliczb, "liczb:"

	typy = set()
	i = 0
	while i < ileliczb:
		try:
			typ = int(raw_input('wytypuj liczbę '  + str(i + 1) + ': '))
	
		except ValueError:
			print 'bledne dane'
			continue
		if 0<typ<maxliczb and typ not in typy:
			typy.add(typ)
			i = i + 1
		else:
			print 'cos nie tak jeszcz raz'
			continue
	return typy

def wyniki(liczby, typy):
	trafione = set(liczby) & typy

	print 'wytypowales', typy
	print 'trafione', trafione
	print 'trafiles', len(trafione), 'razy'

	return len(trafione)

