import numpy as np
import scipy.optimize
import h5py

import mri.model.eval
import util.logging
logger = util.logging.get_logger()


class Cost_Function():
    
    def __init__(self):
        from .constants import MEASUREMENT_DATA_FILE, MEASUREMENT_DATA_KEY_NAME, MEASUREMENT_DATA_SHAPE, VOXEL_PARAMETER_BOUNDS
        
        with h5py.File(MEASUREMENT_DATA_FILE, mode='r') as file:
            self.measurement_data = file[MEASUREMENT_DATA_KEY_NAME].value.flatten()
        
        self.model = mri.model.eval.Model()
        self.MEASUREMENT_DATA_SHAPE = MEASUREMENT_DATA_SHAPE
        self.VOXEL_PARAMETER_BOUNDS = VOXEL_PARAMETER_BOUNDS
    
    
    @property
    def number_of_measurements(self):
        return len(self.measurement_data)
    
    
    def f(self, sample_data):
        return np.linalg.norm(self.measurement_data - self.model.f(sample_data.reshape(self.MEASUREMENT_DATA_SHAPE)).flat)
    
    
    def optimize(self, guessed_sample_data):
        ## check number of total parameters and number of measurements
        sample_data_shape_array = np.array(guessed_sample_data.shape)
        number_of_voxels = sample_data_shape_array[:-1].prod()
        number_of_voxel_parameters = sample_data_shape_array[-1]
        number_of_total_parameters = number_of_voxels * number_of_voxel_parameters
        
        if number_of_total_parameters > self.number_of_measurements:
            raise ValueError('The number of total parameters {} has to be less or equal to the number of signals {}. Maybe reduce the sample resolution'.format(number_of_total_parameters, self.number_of_measurements))
        
        ## run optimization
        logger.debug('Optimization started for {} voxels each with {} parameters.'.format(number_of_voxels, number_of_voxel_parameters))
        bounds = self.VOXEL_PARAMETER_BOUNDS * number_of_voxels
        # result = scipy.optimize.minimize(self.f, guessed_sample_data, method='L-BFGS-B', bounds=bounds, options={'disp':True})
        result = scipy.optimize.differential_evolution(self.f, bounds, maxiter=100, popsize=2, init='random', polish=False, disp=True)
        logger.debug('Optimization finished with result {}.'.format(result))
        
        return result.x