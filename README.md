# TelloVectoFly

A simulation environment for testing and visualizing Tello drone flight paths before deploying commands to a real drone.

## Features

- Real-time visualization of drone movement and altitude
- Interactive command-line interface for drone control
- Save and load flight paths as JSON files
- Supports all basic Tello drone commands:
  - Movement: forward, back, left, right, up, down
  - Rotation: clockwise (cw), counter-clockwise (ccw)
  - Special: takeoff, land, flip
- Error checking for valid commands and parameters
- Simulated flight path plotting with error margins
- Real drone deployment capability via [easytello](https://github.com/Virodroid/easyTello)

## Installation

1. Clone this repository
2. Install required dependencies:
```python
pip install matplotlib numpy pandas easytello
python test.py
```