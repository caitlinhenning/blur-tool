# Privacy-First Video Blur Algorithm

## Description

Our project focuses on ensuring the privacy of people being surveilled by CCTV cameras by blurring their faces so that if data is released to the public, their identities will remain protected. We first apply bounding boxes to faces in footage. Then, for the bounding boxes we generate a blur to obscure faces. Each of those blurs come with a corresponding private key that is locally stored and can be sent to other individuals. This blur can be decrypted with the private key, and the original facial features can be accessed. This is useful for situations where original data is needed, such as for court evidence.

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
