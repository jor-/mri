import subprocess

import util.io.hdf5


def get_sample_value(file):
    from .constants import SAMPLE_KEY_NAME
    return util.io.hdf5.load(file, SAMPLE_KEY_NAME)

def set_sample_value(file, value):
    from .constants import SAMPLE_KEY_NAME
    util.io.hdf5.save(file, SAMPLE_KEY_NAME, value)

def get_signal_value(file):
    from .constants import SIGNAL_KEY_NAME
    return util.io.hdf5.load(file, SIGNAL_KEY_NAME)

def set_signal_value(file, value):
    from .constants import SIGNAL_KEY_NAME
    util.io.hdf5.save(file, SIGNAL_KEY_NAME, value)



class Model():
    
    def __init__(self, number_of_processes=4):
        self.number_of_processes = number_of_processes
    
    def f(self, sample_data):
        from .constants import SAMPLE_FILE, SIGNALS_FILE, JEMRIS_COMMAND
        assert sample_data.ndim == 3
        assert sample_data.shape[2] == 5
        
        ## save sample data
        set_sample_value(SAMPLE_FILE, sample_data)  #TODO create (new) sample file (dim mismatch for different sample dims)
        
        ## run jemris
        command = JEMRIS_COMMAND.format(number_of_processes=self.number_of_processes)
        subprocess.check_call(command, shell=True)
        
        ## load signal data
        signal_data = get_signal_value(SIGNALS_FILE)
        
        return signal_data