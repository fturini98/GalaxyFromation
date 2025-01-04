import h5py
import os

class Simulation_Snapshot():
    
    def __init__(self):
        self.Dark_Key='PartType0'
        self.Gas_Key='PartType1'
        self.Star_Key='PartType4'
        pass
    
    def load_snap_and_groups(self,snap_path,group_path):
        self.snap=h5py.File(snap_path,'r')
        self.group=h5py.File(group_path,'r')