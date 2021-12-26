import subprocess as sub
import sys
from time import sleep
from pynput import keyboard as kb


sub.call('bash Macro/macroBackspace.sh', shell=True)
sub.call('python3 main.py', shell=True)
sub.call('bash Macro/macroBackspace.sh', shell=True)