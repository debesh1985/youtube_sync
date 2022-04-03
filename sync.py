#!/usr/bin/env python3
from dirsync import sync
source_path = '/home/debesh/Music'
target_path = '/media/debesh/DEBESH'
sync(source_path, target_path, 'sync',  purge=True) #for syncing one way
#sync(target_path, source_path, 'sync') #for syncing the opposite way