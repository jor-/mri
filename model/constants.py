import os.path

import numpy as np


from ..constants import JEMRIS_DIR
INTERCONNECTION_DIR = os.path.join (JEMRIS_DIR, 'interconnection')

SAMPLE_FILENAME = 'sample.h5'
SIGNALES_FILENAME = 'signals.h5'
SIMULATION_FILENAME = 'simulation.xml'

SAMPLE_FILE = os.path.join(INTERCONNECTION_DIR, SAMPLE_FILENAME)
SIGNALS_FILE = os.path.join(INTERCONNECTION_DIR, SIGNALES_FILENAME)
SIMULATION_FILE = os.path.join(INTERCONNECTION_DIR, SIMULATION_FILENAME)

SAMPLE_KEY_NAME = '/sample/data'
SIGNAL_KEY_NAME = '/signal/channels/00' #TODO iterate channels

JEMRIS_COMMAND = 'cd ' + INTERCONNECTION_DIR + '; echo "Running jemris in "$PWD.; mpirun -np {number_of_processes} pjemris ' + SIMULATION_FILENAME

VOXEL_PARAMETER_BOUNDS = ((0, 3000), (0, 400), (0, 200), (0, 1), (0, 220*2*np.pi))

VOXEL_PARAMETER_ARRAY = np.array([[2569, 329, 158, 1, 0], [833, 83, 69, 0.86, 0], [500, 70, 61, 0.77, 0],[350, 70, 58, 1, 220*2*np.pi], [900, 47, 30, 1, 0], [2569, 329, 58, 1.00, 0], [0, 0, 0, 0, 0]])
