import argparse
import os.path

import numpy as np

import mri.model.eval
import mri.optimization.cost_function

from mri.model.constants import INTERCONNECTION_DIR
from mri.constants import BRAIN_DIR

from util.logging import Logger


log_file = os.path.join(INTERCONNECTION_DIR, 'log_file.txt')
res_file = os.path.join(INTERCONNECTION_DIR, 'x_res.npy')
brain_file = os.path.join(BRAIN_DIR, '22x18', 'sample.h5')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number_of_processes', type=int, default=4)
    parser.add_argument('-d', '--debug', action='store_true', help='Print debug infos.')
    args = parser.parse_args()
    
    with Logger(log_file=log_file, disp_stdout=args.debug):
        cf = mri.optimization.cost_function.Cost_Function()
        
        x_opt = mri.model.eval.get_sample_value(brain_file)
        
        x_0 = np.empty_like(x_opt)
        x_0[:,:] = x_opt.mean(axis=(0,1))
        
        x_res = cf.optimize(x_0)
        np.save(res_file, x_res)