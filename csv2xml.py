#!/usr/bin/env python
# -*- coding: utf-8 -*-
# csv2xml.py
# First row of the csv file must be header!
 
import argparse
import csv , operator

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")

parser.add_argument("-f", "--file", help="Nombre de archivo a procesar")
args = parser.parse_args()
 
# Aquí procesamos lo que se tiene que hacer con cada argumento
if args.verbose:
    print "depuración activada!!!"

if args.file:
    print "El nombre de archivo a procesar es: ", args.file
    
# Aquí procesamos el ficherocsv separado por ,
csvFile = args.file
xmlFile = csvFile[:-4] + '.xml'
dtdFile = csvFile[:-4] + '.dtd'
xsdFile = csvFile[:-4] + '.xsd'

csvData = csv.reader(open(csvFile))

xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
xmlData.write('<titanic>' + "\n")

dtdData = open(dtdFile, 'w')
dtdData.write('<!DOCTYPE person [' + "\n")

xsdData = open(xsdFile, 'w') 
xsdData.write('<xs:element name="person">' + "\n")
xsdData.write("\n") 
xsdData.write('<xs:complexType>' + "\n")
xsdData.write(' <xs:sequence>' + "\n")


rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
            dtdData.write('    ' + '<!ENTITY ' + tags[i] + '>'+ "\n")
            
            xsdData.write('    ' + '<xs:element name="' + tags[i] + ' type="xs:string"/>'+ "\n")
            
        xsdData.write(' </xs:sequence>' + "\n")  
        xsdData.write('</xs:complexType>' + "\n")  
        xsdData.write("\n")  
        xsdData.write('</xs:element' + "\n")   
            
        dtdData.write(']>' + "\n")
    else: 
        xmlData.write('<person>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</person>' + "\n")
            
    rowNum +=1

xmlData.write('</titanic>' + "\n")
xmlData.close()
