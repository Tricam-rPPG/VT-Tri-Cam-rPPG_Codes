<p align="center">
:fire: If you have any questions or concerns, please create an <a href="https://github.com/ubicomplab/rPPG-Toolbox/issues">issue</a> :memo:! :fire:
</p>

# :wave: Introduction

**rPPG-Toolbox** is an open-source platform designed for camera-based physiological sensing, also known as remote photoplethysmography (rPPG). 

rPPG-Toolbox not only benchmarks the **existing state-of-the-art neural and unsupervised methods**, but it also supports flexible and rapid development of your own algorithms.
![Overview of the toolbox](./figures/toolbox_overview.png)


# :file_folder: Datasets
The toolbox supports eight datasets, namely VT-Tri-Cam-rPPG, SCAMPS, UBFC-rPPG, PURE, BP4D+, UBFC-Phys, MMPD and iBVP. Please cite the corresponding papers when using these datasets. For now, we recommend training with UBFC-rPPG, PURE, iBVP or SCAMPS due to the level of synchronization and volume of the datasets. **To use these datasets in a deep learning model, you should organize the files as follows.**
* [MMPD](https://github.com/McJackTang/MMPD_rPPG_dataset)
    * Jiankai Tang, Kequan Chen, Yuntao Wang, Yuanchun Shi, Shwetak Patel, Daniel McDuff, Xin Liu, "MMPD: Multi-Domain Mobile Video Physiology Dataset", IEEE EMBC, 2023
    -----------------
         data/MMPD/
         |   |-- subject1/
         |       |-- p1_0.mat
         |       |-- p1_1.mat
         |       |...
         |       |-- p1_19.mat
         |   |-- subject2/
         |       |-- p2_0.mat
         |       |-- p2_1.mat
         |       |...
         |...
         |   |-- subjectn/
         |       |-- pn_0.mat
         |       |-- pn_1.mat
         |       |...
    -----------------
    
* [SCAMPS](https://arxiv.org/abs/2206.04197)
    * D. McDuff, M. Wander, X. Liu, B. Hill, J. Hernandez, J. Lester, T. Baltrusaitis, "SCAMPS: Synthetics for Camera Measurement of Physiological Signals", NeurIPS, 2022
    -----------------
         data/SCAMPS/Train/
            |-- P00001.mat
            |-- P00002.mat
         |...
         data/SCAMPS/Val/
            |-- P00001.mat
            |-- P00002.mat
         |...
         data/SCAMPS/Test/
            |-- P00001.mat
            |-- P00002.mat
         |...
    -----------------

* [UBFC-rPPG](https://sites.google.com/view/ybenezeth/ubfcrppg)
    * S. Bobbia, R. Macwan, Y. Benezeth, A. Mansouri, J. Dubois, "Unsupervised skin tissue segmentation for remote photoplethysmography", Pattern Recognition Letters, 2017.
    -----------------
         data/UBFC-rPPG/
         |   |-- subject1/
         |       |-- vid.avi
         |       |-- ground_truth.txt
         |   |-- subject2/
         |       |-- vid.avi
         |       |-- ground_truth.txt
         |...
         |   |-- subjectn/
         |       |-- vid.avi
         |       |-- ground_truth.txt
    -----------------
   
* [PURE](https://www.tu-ilmenau.de/universitaet/fakultaeten/fakultaet-informatik-und-automatisierung/profil/institute-und-fachgebiete/institut-fuer-technische-informatik-und-ingenieurinformatik/fachgebiet-neuroinformatik-und-kognitive-robotik/data-sets-code/pulse-rate-detection-dataset-pure)
    * Stricker, R., Müller, S., Gross, H.-M.Non-contact "Video-based Pulse Rate Measurement on a Mobile Service Robot"
in: Proc. 23st IEEE Int. Symposium on Robot and Human Interactive Communication (Ro-Man 2014), Edinburgh, Scotland, UK, pp. 1056 - 1062, IEEE 2014
    -----------------
         data/PURE/
         |   |-- 01-01/
         |      |-- 01-01/
         |      |-- 01-01.json
         |   |-- 01-02/
         |      |-- 01-02/
         |      |-- 01-02.json
         |...
         |   |-- ii-jj/
         |      |-- ii-jj/
         |      |-- ii-jj.json
    -----------------
    
* [BP4D+](https://www.cs.binghamton.edu/~lijun/Research/3DFE/3DFE_Analysis.html)
    * Zhang, Z., Girard, J., Wu, Y., Zhang, X., Liu, P., Ciftci, U., Canavan, S., Reale, M., Horowitz, A., Yang, H., Cohn, J., Ji, Q., Yin, L. "Multimodal Spontaneous Emotion Corpus for Human Behavior Analysis", IEEE International Conference on Computer Vision and Pattern Recognition (CVPR) 2016.   
    -----------------
        RawData/
         |   |-- 2D+3D/
         |       |-- F001.zip/
         |       |-- F002.zip
         |       |...
         |   |-- 2DFeatures/
         |       |-- F001_T1.mat
         |       |-- F001_T2.mat
         |       |...
         |   |-- 3DFeatures/
         |       |-- F001_T1.mat
         |       |-- F001_T2.mat
         |       |...
         |   |-- AUCoding/
         |       |-- AU_INT/
         |            |-- AU06/
         |               |-- F001_T1_AU06.csv
         |               |...
         |           |...
         |       |-- AU_OCC/
         |           |-- F00_T1.csv 
         |           |...
         |   |-- IRFeatures/
         |       |-- F001_T1.txt
         |       |...
         |   |-- Physiology/
         |       |-- F001/
         |           |-- T1/
         |               |-- BP_mmHg.txt
         |               |-- microsiemens.txt
         |               |--LA Mean BP_mmHg.txt
         |               |--LA Systolic BP_mmHg.txt
         |               |-- BP Dia_mmHg.txt
         |               |-- Pulse Rate_BPM.txt
         |               |-- Resp_Volts.txt
         |               |-- Respiration Rate_BPM.txt
         |       |...
         |   |-- Thermal/
         |       |-- F001/
         |           |-- T1.mv
         |           |...
         |       |...
         |   |-- BP4D+UserGuide_v0.2.pdf
    -----------------

* [UBFC-Phys](https://sites.google.com/view/ybenezeth/ubfc-phys)
    * Sabour, R. M., Benezeth, Y., De Oliveira, P., Chappe, J., & Yang, F. (2021). Ubfc-phys: A multimodal database for psychophysiological studies of social stress. IEEE Transactions on Affective Computing.  
    -----------------
          RawData/
          |   |-- s1/
          |       |-- vid_s1_T1.avi
          |       |-- vid_s1_T2.avi
          |       |...
          |       |-- bvp_s1_T1.csv
          |       |-- bvp_s1_T2.csv
          |   |-- s2/
          |       |-- vid_s2_T1.avi
          |       |-- vid_s2_T2.avi
          |       |...
          |       |-- bvp_s2_T1.csv
          |       |-- bvp_s2_T2.csv
          |...
          |   |-- sn/
          |       |-- vid_sn_T1.avi
          |       |-- vid_sn_T2.avi
          |       |...
          |       |-- bvp_sn_T1.csv
          |       |-- bvp_sn_T2.csv
    -----------------

* [iBVP](https://github.com/PhysiologicAILab/iBVP-Dataset)
    * Joshi, J.; Cho, Y. iBVP Dataset: RGB-Thermal rPPG Dataset with High Resolution Signal Quality Labels. Electronics 2024, 13, 1334.
    -----------------
          iBVP_Dataset/
          |   |-- p01_a/
          |      |-- p01_a_rgb/
          |      |-- p01_a_t/
          |      |-- p01_a_bvp.csv
          |   |-- p01_b/
          |      |-- p01_b_rgb/
          |      |-- p01_b_t/
          |      |-- p01_b_bvp.csv
          |...
          |   |-- pii_x/
          |      |-- pii_x_rgb/
          |      |-- pii_x_t/
          |      |-- pii_x_bvp.csv
    -----------------

  * [PhysDrive](https://github.com/WJULYW/PhysDrive-Dataset)
    * Jiyao Wang, Xiao Yang, Qingyong Hu, Jiankai Tang, Can Liu, Dengbo He, Yuntao Wang, Ying-Cong Chen, Kaishun Wu. （2025） PhysDrive: A Multimodal Remote Physiological Measurement Dataset for In-vehicle Driver Monitoring
    -----------------
         On-Road-rPPG/
         |   |-- AFH1/
         |      |-- A1/
         |          |-- Align/
         |              |-- ...png
         |          |-- Label/
         |              |-- BVP.mat
         |              |-- ECG.mat
         |              |-- RESP.mat
         |              |-- SPO2.mat
         |      |-- A2/...
         |      |-- B1/...
         |      |-- B2/...
         |      |-- C1/...
         |      |-- C2/...
         |   |-- AFH2/
         |...
         |   |-- CMZ2/
    -----------------

* [SUMS](https://github.com/thuhci/SUMS/)
    * Ke Liu*, Jiankai Tang*(*Co-first Author), Zhang Jiang, Yuntao Wang, Xiaojing Liu, Dong Li, Yuanchun Shi, "Summit Vitals: Multi-Camera and Multi-Signal Biosensing at High Altitudes", IEEE UIC, 2024
    -----------------
        data/SUMS/
        |   |-- 060200/
        |       |-- v01
        |           |-- BVP.csv
        |           |-- frames_timestamp.csv
        |           |-- HR.csv
        |           |-- RR.csv
        |           |-- video_ZIP_H264_face.avi
        |           |-- video_ZIP_H264_finger.avi
        |       |-- v02
        |       |-- v03
        |       |-- v04
        |   |-- 060201/
        |       |-- v01
        |       |-- v02
        |       |...
        |...
        |   |-- 0602mn/
        |       |-- v01
        |       |-- v02
        |       |...
    -----------------

* [LADH](https://github.com/McJackTang/FusionVitals/)
    * Xulin Ma, Jiankai Tang, Zhang Jiang, Songqin Cheng, Yuanchun Shi, Dong Li, Xin Liu, Daniel Mcduff, Xiaojing Liu, Yuntao Wang, "Non-Contact Health Monitoring During Daily Personal Care Routines", IEEE-EMBS BSN, 2025
    -----------------
        data/LADH/
        |   |-- 12_05/
        |       |-- p_12_05_caip
        |           |-- v01
        |               |-- BVP.csv
        |               |-- HR.csv
        |               |-- RR.csv
        |               |-- SpO2.csv
        |               |-- frames_timestamp_IR.csv
        |               |-- frames_timestamp_RGB.csv
        |               |-- video_RGB_H264.avi
        |               |-- video_IR_H264.avi
        |           |-- v02
        |           |-- v03
        |           |-- v04
        |           |-- v05
        |       |-- p_12_05_huangxj
        |           |-- v01
        |               |-- ...
        |           |-- v02
        |           |-- v03
        |           |-- v04
        |           |-- v05
        |       |-- p_12_05_liutj
        |       |-- p_12_05_lujg
        |       |-- ...
        |   |-- 12_06/
        |       |-- p_12_06_caip
        |       |-- p_12_06_huangxj
        |       |-- p_12_06_liutj
        |       |-- p_12_06_lujg
        |       |...
        |   |-- ...
        |   
        |  
    -----------------

## :bar_chart: Benchmarks

The table shows  Mean Absolute Error (MAE) and Mean Absolute Percent Error (MAPE) performance across all the algorithms and datasets:

![The overview of the results](./figures/results.png)

# :wrench: Setup

You can use either [`conda`](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) or [`uv`](https://docs.astral.sh/uv/getting-started/installation/) with this toolbox. Most users are already familiar with `conda`, but `uv` may be a bit less familiar - check out some highlights about `uv` [here](https://docs.astral.sh/uv/#highlights). If you use `uv`, it's highly recommended you do so independently of `conda`, meaning you should make sure you're not installing anything in the base `conda` environment or any other `conda` environment. If you're having trouble making sure you're not in your base `conda` environment, try setting `conda config --set auto_activate_base false`.

STEP 1: `bash setup.sh conda` or `bash setup.sh uv` 

STEP 2: `conda activate rppg-toolbox` or, when using `uv`, `source .venv/bin/activate`

NOTE: the above setup should work without any issues on machines using Linux or MacOS. If you run into compiler-related issues using `uv` when installing tools related to mamba, try checking to see if `clang++` is in your path using `which clang++`. If nothing shows up, you can install `clang++` using `sudo apt-get install clang` on Linux or `xcode-select --install` on MacOS.

If you use Windows or other operating systems, consider using [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) and following the steps within `setup.sh` independently.

# :computer: Example of Using Pre-trained Models 

Please use config files under `./configs/infer_configs`

For example, if you want to run The model trained on PURE and tested on UBFC-rPPG, use `python main.py --config_file ./configs/infer_configs/PURE_UBFC-rPPG_TSCAN_BASIC.yaml`

If you want to test unsupervised signal processing  methods, you can use `python main.py --config_file ./configs/infer_configs/UBFC-rPPG_UNSUPERVISED.yaml`

# :computer: Examples of Neural Network Training

Please use config files under `./configs/train_configs`

## Training on PURE and Testing on UBFC-rPPG With TSCAN 

STEP 1: Download the PURE raw data by asking the [paper authors](https://www.tu-ilmenau.de/universitaet/fakultaeten/fakultaet-informatik-und-automatisierung/profil/institute-und-fachgebiete/institut-fuer-technische-informatik-und-ingenieurinformatik/fachgebiet-neuroinformatik-und-kognitive-robotik/data-sets-code/pulse-rate-detection-dataset-pure).

STEP 2: Download the UBFC-rPPG raw data via [link](https://sites.google.com/view/ybenezeth/ubfcrppg)

STEP 3: Modify `./configs/train_configs/PURE_PURE_UBFC-rPPG_TSCAN_BASIC.yaml` 

STEP 4: Run `python main.py --config_file ./configs/train_configs/PURE_PURE_UBFC-rPPG_TSCAN_BASIC.yaml` 

Note 1: Preprocessing requires only once; thus turn it off on the yaml file when you train the network after the first time. 

Note 2: The example yaml setting will allow 80% of PURE to train and 20% of PURE to valid. 
After training, it will use the best model(with the least validation loss) to test on UBFC-rPPG.

## Training on SCAMPS and testing on UBFC-rPPG With DeepPhys

STEP 1: Download the SCAMPS via this [link](https://github.com/danmcduff/scampsdataset) and split it into train/val/test folders.

STEP 2: Download the UBFC-rPPG via [link](https://sites.google.com/view/ybenezeth/ubfcrppg)

STEP 3: Modify `./configs/train_configs/SCAMPS_SCAMPS_UBFC-rPPG_DEEPPHYS_BASIC.yaml` 

STEP 4: Run `python main.py --config_file ./configs/train_configs/SCAMPS_SCAMPS_UBFC-rPPG_DEEPPHYS_BASIC.yaml`

Note 1: Preprocessing requires only once; thus turn it off on the yaml file when you train the network after the first time. 

Note 2: The example yaml setting will allow 80% of SCAMPS to train and 20% of SCAMPS to valid. 
After training, it will use the best model(with the least validation loss) to test on UBFC-rPPG.

# :zap: Inference With Unsupervised Methods 

STEP 1: Download the UBFC-rPPG via [link](https://sites.google.com/view/ybenezeth/ubfcrppg)

STEP 2: Modify `./configs/infer_configs/UBFC_UNSUPERVISED.yaml` 

STEP 3: Run `python main.py --config_file ./configs/infer_configs/UBFC_UNSUPERVISED.yaml`

# :eyes: Visualization of Preprocessed Data
A python notebook for visualizing preprocessed data can be found in `tools/preprocessing_viz` along with an associated README. The notebook, `viz_preprocessed_data.ipynb`, automatically detects the preprocessed data format and then plots input image examples and waveforms. 
![Data Visualization Example](./tools/preprocessing_viz/preprocessing_viz_example.png)

# :chart_with_downwards_trend: Plots of Training Losses and LR

This toolbox saves plots of training, and if applicable, validation losses automatically. Plots are saved in `LOG.PATH` (`runs/exp` by default). An example of these plots when training and validating with the UBFC-rPPG dataset and testing on the PURE dataset are shown below.

<img src="./figures/example_losses_plot.png" alt="drawing" width="600"/>
<img src="./figures/example_lr_schedule_plot.png" alt="drawing" width="400"/>

# :straight_ruler: Bland-Altman Plots

By default, this toolbox produces Bland-Altman plots as a part of its metrics evaluation process for both supervised and unsupervised methods. These plots are saved in the `LOG.PATH` (`runs/exp` by default). An example of these plots after training and validating with the UBFC-rPPG dataset and testing on the PURE dataset are shown below.

<img src="./figures/example_scatter_plot.png" alt="drawing" width="450"/> <img src="./figures/example_difference_plot.png" alt="drawing" width="450"/>

# :eyes: Visualization of Neural Method Predictions

A python notebook for visualizing test-set neural method output predictions and labels can be found in `tools/output_signal_viz` along with an associated README. The notebook, `data_out_viz.ipynb`, given a `.pickle` output file, generated by setting `TEST.OUTPUT_SAVE_DIR` assists in plotting predicted PPG signals against ground-truth PPG signals.
![Prediction Visualization Example](./tools/output_signal_viz/sample_model_output_viz.png)

# :scroll: YAML File Setting
The rPPG-Toolbox uses yaml file to control all parameters for training and evaluation. 
You can modify the existing yaml files to meet your own training and testing requirements.

Here are some explanation of parameters:
* #### TOOLBOX_MODE: 
  * `train_and_test`: train on the dataset and use the newly trained model to test.
  * `only_test`: you need to set INFERENCE-MODEL_PATH, and it will use pre-trained model initialized with the MODEL_PATH to test.
* #### TRAIN / VALID / TEST / UNSUPERVISED DATA:
  * `PLOT_LOSSES_AND_LR`: If `True`, save plots of the training loss and validation loss, as well as the learning rate, to `LOG.PATH` (`runs/exp` by default). Currently, only a basic training loss and validation loss are plotted, but in the future additional losses utilized in certain trainer files (e.g., PhysFormer and BigSmall) will also be captured.
  * `USE_EXCLUSION_LIST`: If `True`, utilize a provided list to exclude preprocessed videos
  * `SELECT_TASKS`: If `True`, explicitly select tasks to load 
  * `DATA_PATH`: The input path of raw data
  * `CACHED_PATH`: The output path to preprocessed data. This path also houses a directory of .csv files containing data paths to files loaded by the dataloader. This filelist (found in default at CACHED_PATH/DataFileLists). These can be viewed for users to understand which files are used in each data split (train/val/test)
  * `EXP_DATA_NAME` If it is "", the toolbox generates a EXP_DATA_NAME based on other defined parameters. Otherwise, it uses the user-defined EXP_DATA_NAME.  
  * `BEGIN" & "END`: The portion of the dataset used for training/validation/testing. For example, if the `DATASET` is PURE, `BEGIN` is 0.0 and `END` is 0.8 under the TRAIN, the first 80% PURE is used for training the network. If the `DATASET` is PURE, `BEGIN` is 0.8 and `END` is 1.0 under the VALID, the last 20% PURE is used as the validation set. It is worth noting that validation and training sets don't have overlapping subjects.  
  * `DATA_TYPE`: How to preprocess the video data
  * `DATA_AUG`: If present, the type of generative data augmentation applied to video data
  * `LABEL_TYPE`: How to preprocess the label data
  *  `USE_PSUEDO_PPG_LABEL`: If `True` use POS generated PPG psuedo labels instead of dataset ground truth heart singal waveform
  * `DO_CHUNK`: Whether to split the raw data into smaller chunks
  * `CHUNK_LENGTH`: The length of each chunk (number of frames)
  * `DO_CROP_FACE`: Whether to perform face detection
  * `BACKEND`: Select which backend to use for face detection. Currently, the options are HC (Haar Cascade) or Y5F (YOLO5Face). We recommend using Haar Cascade (the config default) in order to reproduce results from the [NeurIPS 2023 Datasets and Benchmarks paper](https://arxiv.org/abs/2210.00716) that corresponds to this toolbox. If you want to use YOLO5Face in your own custom config, we recommend that you reference configs that use it as a default (e.g., FactorizePhys).
  * `DYNAMIC_DETECTION`: If `False`, face detection is only performed at the first frame and the detected box is used to crop the video for all of the subsequent frames. If `True`, face detection is performed at a specific frequency which is defined by `DYNAMIC_DETECTION_FREQUENCY`. 
  * `DYNAMIC_DETECTION_FREQUENCY`: The frequency of face detection (number of frames) if DYNAMIC_DETECTION is `True`
  * `USE_MEDIAN_FACE_BOX`: If `True` and `DYNAMIC_DETECTION` is `True`, use the detected face boxs throughout each video to create a single, median face box per video.
  * `LARGE_FACE_BOX`: Whether to enlarge the rectangle of the detected face region in case the detected box is not large enough for some special cases (e.g., motion videos)
  * `LARGE_BOX_COEF`: The coefficient to scale the face box if `LARGE_FACE_BOX` is `True`.
  * `INFO`: This is a collection of parameters based on attributes of a dataset, such as gender, motion types, and skin color, that help select videos for inclusion in training, validation, or testing. Currently, only the [MMPD](https://github.com/McJackTang/MMPD_rPPG_dataset) dataset is supported for parameter-based video inclusion. Please refer to one of the config files involving the [MMPD](https://github.com/McJackTang/MMPD_rPPG_dataset) dataset for an example of using these parameters.
  * `EXCLUSION_LIST`: A list that specifies videos to exclude, typically based on a unique identifier to a video such as the combination of a subject ID and a task ID. This is only used if `USE_EXCLUSION_LIST` is set to `True`. Currently this parameter is only tested with the [UBFC-Phys](https://sites.google.com/view/ybenezeth/ubfc-phys) dataset. Please refer to one of the config files involving the [UBFC-Phys](https://sites.google.com/view/ybenezeth/ubfc-phys) dataset for an example of using this parameter.
  * `TASK_LIST`: A list to specify tasks to include when loading a dataset, allowing for selective inclusion of a subset of tasks or a single task in a dataset if desired. This is only used if `SELECT_TASKS` is set to `True`. Currently this parameter is only tested with the [UBFC-Phys](https://sites.google.com/view/ybenezeth/ubfc-phys) dataset. Please refer to one of the config files involving the [UBFC-Phys](https://sites.google.com/view/ybenezeth/ubfc-phys) dataset for an example of using this parameter.

  
* #### MODEL : Set used model (Deepphys, TSCAN, Physnet, EfficientPhys, BigSmall, and PhysFormer and their paramaters are supported).
* #### UNSUPERVISED METHOD: Set used unsupervised method. Example: ["ICA", "POS", "CHROM", "GREEN", "LGI", "PBV"]
* #### METRICS: Set used metrics. Example: ['MAE','RMSE','MAPE','Pearson','SNR','BA']
  * 'BA' metric corresponds to the generation of a Bland-Altman plot to graphically compare two measurement techniques (e.g., differences between measured and ground truth heart rates versus mean of measured and ground truth heart rates). This metric saves the plot in the `LOG.PATH` (`runs/exp` by default).
* #### INFERENCE:
  * `USE_SMALLER_WINDOW`: If `True`, use an evaluation window smaller than the video length for evaluation.

    
# :open_file_folder: Adding a New Dataset

* STEP 1: Create a new python file in `dataset/data_loader`, e.g. MyLoader.py

* STEP 2: Implement the required functions, including:

  ```python
  def preprocess_dataset(self, config_preprocess):
  ```
  ```python
  @staticmethod
  def read_video(video_file):
  ```
  ```python
  @staticmethod
  def read_wave(bvp_file):
  ```

* STEP 3:[Optional] Override optional functions. In principle, all functions in BaseLoader can be override, but we **do not** recommend you to override *\_\_len\_\_, \_\_get\_item\_\_,save,load*.
* STEP 4:Set or add configuration parameters.  To set paramteters, create new yaml files in configs/ .  Adding parameters requires modifying config.py, adding new parameters' definition and initial values.

# :robot: Adding a New Neural Algorithms

* STEP 1: Define a model in a new python file in `neural_methods/model`, e.g. NewModel.py.

* STEP 2: Implement the corresponding training/testing routines in a file `neural_methods/trainer`, e.g. NewModelTrainer.py. Ensure to implement the following functions:

  ```python
  def __init__(self, config, data_loader):
  ```
  ```python
  def train(self, data_loader):
  ```
  ```python
  def valid(self, data_loader):
  ```

  ```python
  def test(self, data_loader)
  ```

  ```python
  def save_model(index)
  ```

* STEP 3: Add logic to `main.py` to use the models in the following `train_and_test` and `test` functions. 

* STEP 4: Create new yaml files in configs/ corresponding to the new algorithm.

# :chart_with_upwards_trend: Adding a New Unsupervised Algorithms

* STEP 1: Define a algorithm in a new python file in `unsupervised_methods/methods`, e.g. NewMethod.py.

* STEP 2: Add logic to `main.py` to use the models in the following `unsupervised_method_inference` function. 

* STEP 4: Create new yaml files in configs/ corresponding to the new algorithm.

# :page_with_curl: Using Custom Data Splits and Custom File Lists

Best practice for rPPG model evaluation involves training and validating a model on one dataset and then evaluating (testing) the performance on additional datasets (Eg. training on PURE and testing on UBFC). Data splits used for training, validation, and testing are saved as .csv filelists with the default directory path set as `CACHED_PATH/DataFileLists` (this are generally auto generated). In cases where users would like to define their own data splits (Eg. for intra-dataset cross validation), the following steps can be used to achieve this.  

* STEP 1: Collect all file paths for the data splits's input files (An example file path would be of format `CACHED_PATH/PREPROCESSED_DATASET/*input*.npy`, eg. `405_input9.npy`). Ensure the corresponding `*label*.npy` files exists in the same directory as the input files.

* STEP 2: Add all file paths to a .csv with column name `input_files`. We suggest creating a pandas dataframe and then saving this out to the csv. This .csv file is the file list for your custom data split. The file can be named anything as long as it has an .csv extension.

* STEP 3: In the desired experiment config file, enter the file path of the .csv file list using keyword `FILE_LIST_PATH` in the `DATA` field of the desired train/valid/test split. The dataloader will load input and label files specified in this file path. 

# :scroll: Citation
If you find our [paper](https://arxiv.org/abs/2210.00716) or this toolbox useful for your research, please cite our work.

```
@article{liu2022rppg,
  title={rPPG-Toolbox: Deep Remote PPG Toolbox},
  author={Liu, Xin and Narayanswamy, Girish and Paruchuri, Akshay and Zhang, Xiaoyu and Tang, Jiankai and Zhang, Yuzhe and Wang, Yuntao and Sengupta, Soumyadip and Patel, Shwetak and McDuff, Daniel},
  journal={arXiv preprint arXiv:2210.00716},
  year={2022}
}
```

# License
<a href="https://www.licenses.ai/source-code-license">
  <img src="https://images.squarespace-cdn.com/content/v1/5c2a6d5c45776e85d1482a7e/1546750722018-T7QVBTM15DQMBJF6A62M/RAIL+Final.png" alt="License: Responsible AI" width="30%">
</a>

# Acknowledgement 

This research project is supported by a Google PhD Fellowship for Xin Liu and a research grant from Cisco for the University of Washington as well as a career start-up funding grant from the Department of Computer Science at UNC Chapel Hill. This research is also supported by Tsinghua University Initiative Scientific Research Program, Beijing Natural Science Foundation,  and the Natural Science Foundation of China (NSFC). We also would like to acknowledge all the contributors from the open-source community. 

