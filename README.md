# Voxelnet-Dectector: TJ '23 W-CAB

Cloned from [David Stephane](https://github.com/steph1793), ([project](https://github.com/steph1793/Voxelnet)) who implemented [VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection](https://arxiv.org/abs/1711.06396) in tensorflow 2.0.0. This project is based on the work of [Qiangui Huang](https://github.com/qianguih), ([project](https://github.com/qianguih/voxelnet)) and [Xiaojian Ma](https://github.com/jeasinema).

# Development Environment
* Visual Studio Code
* Python 3.10

# Installation
1. Clone repository and install packages
```bash
$ pip install -r requirements.txt
```

2. Install [MSYS2](https://www.msys2.org/), following the site's tutorial up to step 5. After, with the MSYS2 terminal open, install the GCC compiler
```bash
$ pacman -Syuu
$ pacman -S mingw-w64-ucrt-x86_64-gcc
$ pacman -S --needed base-devel mingw-w64-x86_64-toolchain
``` 
3. In system environment variables, add ```C:\msys64\mingw64\bin``` and ```C:\msys64\usr\bin``` to PATH

4. Install [Microsoft's C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

5. In Visual Studio Code's terminal, compile the Cython modules
```bash
$ python setup build_ext --inplace
```

# Network Training
1. Download the pre-cropped and pre-split 3D KITTI detection dataset from [Google Drive](https://drive.google.com/drive/folders/1T77gDTwe-h6T2MGfvmoarGYqUIYCPRQU?usp=sharing) (only viewable through FCPS). Install the files labeled "training.zip," "validation.zip," and "testing.zip." _To prepare the data from scratch, follow [this Medium tutorial](https://towardsdatascience.com/lidar-point-cloud-based-3d-object-detection-implementation-with-colab-part-2-of-2-f3ad55c3f38c) without Google Collab_
    
2. Unzip all three folders and place them in the project directory as shown
```plain
Voxelnet-Detector
└── crop_data
    ├── testing
    ├── training
    └── validation
```

3. Run the training command in terminal
```bash
$ python train.py --strategy="all" --n_epochs=160 --batch_size=2 --learning_rate=0.001 --small_addon_for_BCE=1e-6 --max_gradient_norm=5 --alpha_bce=1.5 --beta_bce=1 --huber_delta=3 --dump_vis="no" --data_root_dir="../DATA_DIR/T_DATA" --model_dir="model" --model_name="model6" --dump_test_interval=40 --summary_interval=10 --summary_val_interval=10 --summary_flush_interval=20 --ckpt_max_keep=10
```