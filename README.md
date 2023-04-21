# MousePlayer
Enables you to record and play mouse clicks and mouse movements.
## How to use
### Setup
1. Install [Python](https://www.python.org/downloads/) (3.6 or later)
2. Create a virtual environment (optionnal, but strongly recommended)
```bash
python3 -m venv venv
```
3. Activate the virtual environment
```bash
.\venv\Scripts\activate
```
4. Install the dependencies
```bash
pip install -r requirements.txt
```
### Recording 
To record a set of 'clicks' (mouse clicks and mouse movements), run the following command:
```bash
python record.py
```
To start recording clicks, press any mouse button for 3 seconds. 
To stop recording, press any mouse button for 3 seconds again.
Any mouse movement and click done between these long presses will be recorded.

### Playing
To play a set of 'clicks', run the following command:
```bash
python play.py
```
