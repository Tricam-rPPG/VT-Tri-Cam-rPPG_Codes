import ctypes
libgcc_s = ctypes.CDLL('libgcc_s.so.1')

import glob
import os
import re
from multiprocessing import Pool, Process, Value, Array, Manager

import cv2
import numpy as np
from dataset.data_loader.BaseLoader import BaseLoader
from tqdm import tqdm
import csv
import pandas as pd

class NSF_940_Loader(BaseLoader):
    """The data loader for the NSF dataset."""

    def __init__(self, name, data_path, config_data, device=None):
        """Initializes an NSF dataloader.
            Args:
                data_path(str): path of a folder which stores raw video and bvp data.
                e.g. data_path should be "RawData" for below dataset structure:
                
        """
        self.filtering = config_data.FILTERING 
        
        super().__init__(name, data_path, config_data)

    def get_raw_data(self, data_path):
        """Returns data directories under the path(For NSF dataset)."""
        ## PARTICIPANT301_S1_T1_940.npy
        # data_dirs = glob.glob(data_path + os.sep + "PARTICIPANT*" + os.sep + "*_RGB.mp4")
        # find all video files that starting with "PARTICIPANT" and ending with "_RGB.mp4"
        data_dirs = glob.glob(data_path + os.sep + "PARTICIPANT*_940.mp4")
        
        
        print("these are the data direcotries: \n")
        print(data_dirs)
        if not data_dirs:
            print (data_path)
            dir_list = os.listdir(data_path)
            raise ValueError(self.dataset_name + " data paths empty!")
            
            

        modalityy = '940'

        # for non-chunked -- ## PARTICIPANT301_S1_T1_RGB.mp4
        dirs = [{"index": re.search(
            f'PARTICIPANT(.*)_{modalityy}.mp4', data_dir).group(1), "path": data_dir} for data_dir in data_dirs]
        
    #   ## for files e.g. PARTICIPANT301_S1_T1_RGB.mp4 -- group(1) extracts 301_S1_T1, and these create the dict key 301_S1_T1
    #     ## group(1) will actually capture everything between PARTICIPANT and the first underscore before _{modalityy} (which is RGB in this case). Therefore, group(1) will capture 301_S1_T1, not just 301.
    #     # group(1) will capture 301_S1_T1. 

            
        print(f"we have these many files {len(dirs)}")
        return dirs

    def split_raw_data(self, data_dirs, begin, end):
        """Returns a subset of data dirs, split with begin and end values."""
        if begin == 0 and end == 1:  # return the full directory if begin == 0 and end == 1
            
            return data_dirs

        file_num = len(data_dirs)
        choose_range = range(int(begin * file_num), int(end * file_num))
        data_dirs_new = []

        for i in choose_range:
            data_dirs_new.append(data_dirs[i])

        return data_dirs_new

    def preprocess_dataset_subprocess(self, data_dirs, config_preprocess, i, file_list_dict):
        """   invoked by preprocess_dataset for multi_process.   """
        filename = os.path.split(data_dirs[i]['path'])[-1]
        saved_filename = data_dirs[i]['index']
        
        # Read Frames
        frames = self.read_video(
            os.path.join(data_dirs[i]['path']))
        
        print(frames.shape)

        # Read Labels
        if config_preprocess.USE_PSUEDO_PPG_LABEL:
            bvps = self.generate_pos_psuedo_labels(frames, fs=self.config_data.FS)
        else:
            # bvps = self.read_wave(
            #     os.path.join(os.path.dirname(data_dirs[i]['path']),"bvp_{0}.csv".format(saved_filename)))
            
            # if the csv files are in the same folder as the rgb videos
            parent_path = os.path.dirname(data_dirs[i]['path'])
            # if the csv files are in a specific folder
            # parent_path = "/projects/abbott_lab/BVP/BVP/rPPG-Toolbox-main/newFolder_all_vids/all2/csv_all" ###### change!!!!!!
            parent_path = "/projects/abbott_lab/BVP/BVP/rPPG-Toolbox-main/newFolder_all_vids/all/csv_normalized" ###### change!!!!!! used this for paper tables-main
            
            # parent_path = "/projects/abbott_lab/CCI_data/Training_ECCV_RGB/BVPFiles"
            
            bvps = self.read_wave(
                os.path.join(parent_path,"PARTICIPANT{0}.csv".format(saved_filename)))
            # PARTICIPANT301_S1_T1.csv
            # bvp_s1_T2.csv


        bvps = BaseLoader.resample_ppg(bvps, frames.shape[0])
        
            
        frames, bvps_clips = self.preprocess(frames, bvps, config_preprocess)
        input_name_list, label_name_list = self.save_multi_process(frames, bvps_clips, saved_filename)

        file_list_dict[i] = input_name_list

        # return file_list_dict

    def load_preprocessed_data(self):
        """ Loads the preprocessed data listed in the file list.

        Args:
            None
        Returns:
            None
        """
        file_list_path = self.file_list_path  # get list of files in
        file_list_df = pd.read_csv(file_list_path)
        base_inputs = file_list_df['input_files'].tolist()
        filtered_inputs = []

        for input in base_inputs:
            input_name = input.split(os.sep)[-1].split('.')[0].rsplit('_', 1)[0]

            filtered_inputs.append(input)

        if not filtered_inputs:
            raise ValueError(self.dataset_name + ' dataset loading data error!')
        
        filtered_inputs = sorted(filtered_inputs)  # sort input file name list
        labels = [input_file.replace("input", "label") for input_file in filtered_inputs]
        self.inputs = filtered_inputs
        self.labels = labels
        self.preprocessed_data_len = len(filtered_inputs)

    @staticmethod
    def read_video(video_file):
        """Reads a video file, returns frames(T,H,W,3) """
        """Reads a video file, returns frames(T,H,W,3) """
        i = 0
        VidObj = cv2.VideoCapture(video_file)
       
        # changed here
        target_fps = 60
        original_fps = VidObj.get(cv2.CAP_PROP_FPS)
        repeat = int(target_fps / original_fps)
        print(f"repeat: {repeat}")

        VidObj.set(cv2.CAP_PROP_POS_MSEC, 0)
        success, frame = VidObj.read()
        frames = list()
        while success:
            frame = cv2.cvtColor(np.array(frame), cv2.COLOR_BGR2RGB)
            frame = np.asarray(frame)
            frame = cv2.resize(frame, (1024, 1024), interpolation=cv2.INTER_AREA)

            # changed here
            for j in range(repeat):
                frames.append(frame)
                print("duplicating frames")
                
            success, frame = VidObj.read()
            if (i%1000 == 0):
                print(f'i = {i}')
            i=i+1
        frames = np.asarray(frames)
        print (f"Video File Processed: {video_file}")
        
        print (f"Shape of Array: {frames.shape}")
        return frames

        

    @staticmethod
    def read_wave(bvp_file):
        """Reads a bvp signal file."""
        bvp = []
        print('bvp file is: ' + bvp_file + '\n')
        with open(bvp_file, "r") as f:
            d = csv.reader(f)
            for row in d:
                bvp.append(float(row[0]))  # Access the first column
        return np.asarray(bvp)
