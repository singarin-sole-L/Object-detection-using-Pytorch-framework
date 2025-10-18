# 🟢 Tumor Detection and MGMT Status Classification from MRI

This project implements and evaluates an **object detection pipeline** (based on **Faster R-CNN / PyTorch**)  
for **brain tumor localization and MGMT promoter status classification** using **MRI axial slices**.
Dataset source: https://www.kaggle.com/datasets/davidbroberts/brain-tumor-object-detection-datasets

The model simultaneously:
- Detects tumor **bounding boxes**,  
- Classifies their **MGMT status** (`MGMT+` or `MGMT−`).

The focus of this work is to evaluate **spatial vs. label precision** —  
how well the model knows *where* a tumor is versus *what* type it is.

---

## Overview

MRI data are processed slice-by-slice (axial orientation) and passed to a **Faster R-CNN** model trained to predict:
- Bounding boxes around tumors
- Class labels indicating MGMT methylation status

Main evaluation metrics:
- **Spatial Precision / Recall** : IoU-based detection accuracy (positioning of boxes)  
- **Label Precision / Recall** : correctness of predicted tumor class (MGMT+ / MGMT−)

A custom evaluation module computes:
- PR curves vs. **score threshold**  
- Separate metrics for **spatial** and **label** performance  
- Confusion matrices for both types of predictions  

---

## Project Structure

```
├── data/                    # MRI dataset and annotations
├── notebooks/               # Jupyter notebooks for visualization and experiments
├── src/                     
├── requirements.txt         # Dependencies
├── .gitignore
└── README.md
```

---

## Key Results (Axial-only)

| Metric Type | Precision | Recall | Interpretation |
|:-------------|:----------:|:---------:|:-----------------------------|
| **Spatial (IoU ≥ 0.5)** | 0.935 | 0.889 | Excellent tumor localization |
| **Label (MGMT+/−)** | 0.468 | 0.444 | Moderate label accuracy bc limited by single-axis input |

> These results are consistent with expectations:  
> Using only **axial slices** limits the available 3D and textural information  
> necessary to accurately distinguish MGMT methylation status.

---

## Visualization

### Ground Truth vs Model Predictions (Example of bad predictions)
*(Green: MGMT+ / Red: MGMT−)*  
> Each sample displays both the ground truth (left) and the model prediction (right).  

<p align="center">
  <img width="1348" height="691" alt="bad_pred" src="https://github.com/user-attachments/assets/c0d01689-5169-4626-ad24-0eec453e3e0c" />
</p>

### Precision–Recall Curves (Spatial vs Label)
<p align="center">
<img width="691" height="547" alt="curve" src="https://github.com/user-attachments/assets/9ebbb77e-feae-4724-821a-29fa551ea368" />
</p>

---

## Usage

### 1. Clone the repository
```bash
git clone https://github.com/singarin-sole-L/Object-detection-using-Pytorch-framework-for-tumor-detection.git
cd Object-detection-using-Pytorch-framework-for-tumor-detection
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run evaluation and visualization
```bash
jupyter notebook notebooks/training_and_evaluation.ipynb
```
---

## Notes

- **NMS (Non-Maximum Suppression)** is applied before evaluation to ensure reliable detection metrics.  
- Precision and recall are reported **separately for spatial and label correctness**.  
- The visualization utility allows direct comparison between **ground truth** and **predicted** boxes.  
- Dataset loading and transformations follow the **TorchVision detection pipeline** standards.

---

## Future Work

The next step of this project is to **extend the model to 3D-aware inference**,  
combining **axial, coronal, and sagittal** planes simultaneously.  
This multi-axis approach is expected to significantly improve **label precision** by  
providing richer spatial and textural context for tumor characterization.


### Visualization:
<p align="center">
<img width="1525" height="593" alt="example_tumor_detection_3planes" src="https://github.com/user-attachments/assets/c77bcb55-0a63-4ef0-9ab5-5f4cd9d96171" />
</p>

### Distribution of the classes
<p align="center">
<img width="790" height="590" alt="class_distribution" src="https://github.com/user-attachments/assets/93a7a472-c4e7-49c1-9d53-f6015d4f6aa3" />
</p>

---

## Author

**SINGARIN-SOLE Livio**  
2025   
