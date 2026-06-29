# Tri-Cam-rPPG [ECCV 2026]

## 📖 Abstract

**Here is [Tri-Cam-rPPG Dataset](<https://tricam-rppg.github.io/>) collected by Virginia Tech.**  
This paper introduces Tricam-rPPG, a multimodal dataset designed to support systematic studies of remote photoplethysmography (rPPG) using multispectral imaging. Remote (noncontact) monitoring offers the potential for unobtrusive measurement of physiological signals related to health, cognitive load, and affect. However, most existing rPPG datasets rely primarily on RGB imaging, limiting the study of spectral effects, illumination variability, and sensing biases associated with differences in  optical properties of the skin. Tricam-rPPG provides synchronized recordings of 31 human subjects from three co-located cameras: a standard RGB camera and two near-infrared (NIR) cameras operating at 850 nm and 940 nm, all captured under controlled illumination conditions. For fourteen participants, simultaneous recordings from Meta Aria glasses are also included. All cases are supplemented by reference waveforms of blood volume pulses (BVP) measured using a fingertip PPG sensor. In addition to presenting the dataset, we establish baseline benchmarks with widely used rPPG algorithms to evaluate heart-rate estimation performance across different combinations of spectral channels. By providing synchronized RGB and NIR video together with physiological ground truth, Tricam-rPPG enables new research directions in multispectral physiological sensing, fairness-aware rPPG algorithms, and robust remote cardiovascular monitoring.

Tri-Cam-rPPG can be used in conjunction with the [rPPG-toolbox](https://github.com/ubicomplab/rPPG-Toolbox).  

# :file_folder: Dataset Structure
    -----------------
         data/Tri-Cam-rPPG/
         |   |-- PARTICIPANT301_S1_T1_850.mp4/
         |   |-- PARTICIPANT301_S1_T1_940.mp4/
         |   |-- PARTICIPANT301_S1_T1_RGB.mp4/
         |   |-- PARTICIPANT301_S1_T1.csv/
         |   |-- PARTICIPANT301_S1_T2_850.mp4/
         |   |-- PARTICIPANT301_S1_T2_940.mp4/
         |   |-- PARTICIPANT301_S1_T2_RGB.mp4/
         |   |-- PARTICIPANT301_S1_T2.csv/

    -----------------


## 🗝️ Access and Usage
Tricam-rPPG is intended for research use under a data use license. The release includes synchronized camera recordings, PPG waveforms, Aria subset data, landmarks, skin maps, pulse landmarks, and patch intensity signals. Because the dataset contains human-subject data, access is provided only after execution of a Data Use License (DUL). To request access, please email Abhijit Sarkar and Lynn Abbott. The DUL and access instructions will be sent to approved research requesters.
Please send an email to these email IDs: asarkar@vtti.vt.edu and abbott@vt.edu.

:computer: Please look in the `rppg-Toolbox_VTTriCam` directory for examples on how to use the dataset via the rPPG-Toolbox.


## 📄 Citation

# Acknowledgement 
We thank Ryan Mowri and Ryan Talbot from VTTI for helping with the hardware setup. We thank Gayatri Bhatambarekar, Joe Bekaronov, Jin Woo Baik, and Zeeshan Muhammad Karamat for additional help with data collection. Finally, we thank all the wonderful participants for taking part in the study.
This work was partially funded by National Science Foundation, and Commonwealth of Cyber Initiative at Virginia, USA. 
