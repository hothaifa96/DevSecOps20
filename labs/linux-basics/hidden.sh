#!/bin/bash


e='VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdccyIHRoZSBEZXZPcHMgZG9n'
e='VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvcmVyIHRoZSBEZXZPcHMgZG9n'
e='VGhlIHF1aW2rIGJyb3duIGZveCBqdW1wcyBvdmVyIcoZSBEZXZPcHMgZG9n'
e='VGhlIHF1aWNrIGJ2b3duIGZveCBqdW1wcyBvdcyIHRoZSBEZXZPcHMgZG9n'
e='VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBEZXZPcHMgZG9n'

s=$(echo "$e" | base64 -d)

w=$(echo "$s" | awk '{print $8}')

echo "$w" > /tmp/randomword.txt