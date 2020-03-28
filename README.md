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
## Train For Dehazing
## Test For Dehazing
1. Git clone this repository.
```
$git clone https://github.com/BookerDeWitt/GFN-IJCV.git
$cd GFN
```
2. Download the SOTS dataset from Google Drive.
3. Generate the validation images of SOTS dataset: Run matlab function `GFN/Hazy/h5_generator/LR_RESIDE_Test.m`. The generated test images will be stored in your_downloads_directory/Validation_4x.
(If you don't have access to MATLAB, we offer a validation dataset for testing. You can download it from GoogleDrive or Pan Baidu.)
```
>> folder = 'your_downloads_directory/SOTS'; # You should replace the your_downloads_directory by your SOTS's directory.
>> LR_RESIDE_Test(folder)
```
4. Download the trained model `GFN_epoch_60.pkl` from here, then unzip and move the `GFN_epoch_60.pkl` to `GFN/Hazy/models` folder.

5. Run the `GFN/Hazy/test.py` with cuda on command line:
```
GFN/$python test.py --dataset your_downloads_directory/SOTS/Validation_4x
```
Then the dehazing and super-solving images ending with GFN_4x.png are in the directory of SOTS/Validation/Results.

6. Calculate the PSNR using Matlab function GFN/evaluation/evaluate_SR.m. The output of the average PSNR is 25.77 dB. 
>> folder = 'your_downloads_directory/SOTS';
>> evaluate_SR(folder)
## Citation
If you use these models in your research, please cite:
```
@conference{Zhang2018,
	author = {Xinyi Zhang and Hang Dong and Zhe Hu and Wei-Sheng Lai and Fei Wang and Ming-Hsuan Yang},
	title = {Gated Fusion Network for Degraded Image Super Resolution},
	booktitle = {IJCV},
	year = {2019}
}
```
