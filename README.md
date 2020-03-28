# GFN
"Gated Fusion Network for Degraded Image Super Resolution" by Xinyi Zhang, Hang Dong, Zhe Hu, Wei-Sheng Lai, Fei Wang, Ming-Hsuan Yang(IJCV2019).

[arXiv][Slide]

## Dependencies
* Python 3.6
* PyTorch >= 1.1.0
* torchvision
* numpy
* skimage
* h5py
* MATLAB
## Inproved the training process
In order to obtain a more stable training process, now we adopt a three-step training strategy, which differs from our paper and improves PSNR from 27.74dB to 27.81dB on LR-GOPRO 4x dataset.

Model	LR-GOPRO 4x PSNR(dB)	Time(s)
SCGAN	22.74	0.66
SRResNet	24.40	0.07
ED-DSRN	26.44	0.10
DeepDeblur + EDSR	25.09	2.70
EDSR + DeepDeblur	26.35	8.10
GFN(BMVC paper)	27.74	0.07
GFN(Now)	27.81	0.07
Dependencies
Python 3.6
PyTorch >= 0.4.0
torchvision
numpy
skimage
h5py
MATLAB
How to test:
Test on LR-GOPRO Validation
Test on the latest trained model
This model is the result of the third step with 55 epoch.

Git clone this repository.
$git clone https://github.com/jacquelinelala/GFN.git
$cd GFN
Download the original GOPRO_Large dataset from Google Drive.
Generate the validation images of LR-GOPRO dataset: Run matlab function GFN/h5_generator/gopro_val_generator.m. The generated test images will be stored in your_downloads_directory/GOPRO_Large/Validation_4x.
(If you don't have access to MATLAB, we offer a validation dataset for testing. You can download it from GoogleDrive or Pan Baidu.)

>> folder = 'your_downloads_directory/GOPRO_Large'; # You should replace the your_downloads_directory by your GOPRO_Large's directory.
>> gopro_val_generator(folder)
Download the trained model GFN_epoch_55.pkl from here, then unzip and move the GFN_epoch_55.pkl to GFN/models folder.

Run the GFN/test_GFN_x4.py with cuda on command line:

GFN/$python test_GFN_x4.py --dataset your_downloads_directory/GOPRO_Large/Validation_4x
Then the deblurring and super-solving images ending with GFN_4x.png are in the directory of GOPRO_Large/Validation/Results.

Calculate the PSNR using Matlab function GFN/evaluation/test_RGB.m. The output of the average PSNR is 27.810232 dB. You can also use the GFN/evaluation/test_bicubic.m to calculate the bicubic method.
>> folder = 'your_downloads_directory/GOPRO_Large';
>> test_RGB(folder)
How to train
Train on LR-GOPRO dataset
You should accomplish the first two steps in Test on LR-GOPRO Validation before the following steps.

Train from scratch
Generate the train hdf5 files of LR-GOPRO dataset: Run the matlab function gopro_hdf5_generator.m which is in the directory of GFN/h5_generator. The generated hdf5 files are stored in the your_downloads_directory/GOPRO_Large/GOPRO_train256_4x_HDF5.
>> folder = 'your_downloads_directory/GOPRO_Large';
>> gopro_hdf5_generator(folder)
Run the GFN/train_GFN_4x.py with cuda on command line:
GFN/$python train_GFN_4x.py --dataset your_downloads_directory/GOPRO_Large/GOPRO_train256_4x_HDF5
The three step intermediate models will be respectively saved in models/1/ models/2 and models/3. You can also use the following command to test the intermediate results during the training process. Run the GFN/test_GFN_x4.py with cuda on command line:
GFN/$python test_GFN_x4.py --dataset your_downloads_directory/GOPRO_Large/Validation_4x --intermediate_process models/1/GFN_epoch_30.pkl # We give an example of step1 epoch30. You can replace another pkl file in models/.
Resume training from breakpoints
Since the training process will take 3 or 4 days, you can use the following command to resume the training process from any breakpoints. Run the GFN/train_GFN_4x.py with cuda on command line:

GFN/$python train_GFN_4x.py --dataset your_downloads_directory/GOPRO_Large/GOPRO_train256_4x_HDF5 --resume models/1/GFN_epoch_30.pkl # Just an example of step1 epoch30.
Citation
If you use these models in your research, please cite:

@conference{Zhang2018,
	author = {Xinyi Zhang and Hang Dong and Zhe Hu and Wei-Sheng Lai and Fei Wang and Ming-Hsuan Yang},
	title = {Gated Fusion Network for Joint Image Deblurring and Super-Resolution},
	booktitle = {BMVC},
	year = {2018}
}
