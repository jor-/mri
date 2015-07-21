import os.path

from ..constants import JEMRIS_DIR

MEASUREMENT_DATA_FILE = os.path.join(JEMRIS_DIR, 'brain/22x18/signals.h5')
MEASUREMENT_DATA_SHAPE = (22, 18, 5)
from mri.model.constants import SIGNAL_KEY_NAME as MEASUREMENT_DATA_KEY_NAME
from mri.model.constants import VOXEL_PARAMETER_BOUNDS
