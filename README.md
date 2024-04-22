# Privacy-First Video Blur Algorithm

## Description

We plan to develop an algorithm to blur or anonymize individuals in the footage through encryption, thus protecting their privacy. The blurred footage will be the only footage accessible if hacked, since the original video will be encrypted. To unblur the video, only people with the proper cryptographic key will be able to unblur the image and access the original video files. We will surround our discussion on the choices made in designing our algorithm, touching on topics such as privacy, fairness, and surveillance.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)

## Installation

Instructions on how to install the Privacy-First Video Blur Algorithm.

```bash
# Clone this repository
git clone https://github.com/caitlinhenning/eecs298.git

# Navigate to the repository
cd eecs298

# Install dependencies
pip install -r requirements.txt
```
## Usage

To use the PrivacyBlur algorithm on your video files, follow these instructions:

1. Make sure your video file is in the correct directory eecs298
2. Run the following command:
```bash
python3 pixelate.py [your_video_file.mp4 or .mov]
```
Your blurred video will be saved at output.mp4. To avoid overwriting output.mp4, rename the file before rerunning the program.

Shuffled faces will be written to `shuffled_faces.txt` and private keys will be written to `private_keys.txt`. Add these files to your `.gitignore`.

## Contributors

This project is developed by a team of dedicated EECS 298 students:

- Allie Yuan
- Caitlin Henning
- Aarti Phatke
- Dennis Yang

---
