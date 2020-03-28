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
1. Download the Pretrained model on RESIDE and Test set to `GFN/Hazy/models/3 `and `GFN/Hazy/folder`, respectively.

2. Run the `GFN/Hazy/test.py` with cuda on command line:

MSBDN-DFF/$python test.py --checkpoint path_to_pretrained_model
3 .The dehazed images will be saved in the directory of the test set.
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
