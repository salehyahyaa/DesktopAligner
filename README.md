# Desktop Aligner
- A macOS utility that vertically aligns selected files and folders using Finder automation.
---


## Feature
- Align selected files/folders vertically
- Works via right-click → Quick Actions
- Preserves topmost item as anchor


## Preview
### Before (Messy Organization)
<img src="assets/before.png" width="600"/>

### After (Auto Aligned)
<img src="assets/after.png" width="600"/>


## Limitations
- Alignment works only inside a folder
- Does not work on the main Desktop (home screen)


## Setup

### 1. Locate Python

Run in Terminal:
```bash
which python3
```

Example:
```
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
```
---

### 2. Open Automator
* Press `Cmd + Space`
* Search **Automator**
* Open it
---

### 3. Create Quick Action

* Click **New Document**
* Select **Quick Action**
* Click **Choose**
---

### 4. Configure
At the top:
* Workflow receives → **files or folders in Finder**
---

### 5. Add Script
* Add **Run Shell Script**

Set:
* Shell: `/bin/zsh`
* Pass input: `to stdin`
---

### 6. Command
Paste:
```bash
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 /Users/yourname/Desktop/DesktopAligner/src/align.py
```

Replace with your actual path.
---

### 7. Save
Name It:
```
Align Files
```
---

### 8. Permissions
On first run, allow:
* Finder access
* Desktop access

You may also need to enable Full Disk Access:
* Open **System Settings**
* Go to **Privacy & Security → Full Disk Access**
* Add and enable:
  * Automator
---

## Install
```bash
git clone <https://github.com/salehyahyaa/DesktopAligner.git>
cd DesktopAligner
```
---

## Usage
1. Open a Finder folder
2. Select multiple files or folders
3. Right click
4. Click **Quick Actions → Align Files**
---

## Project Structure
```
DesktopAligner/
│
├── src/
│   └── align.py
│
├── README.md
└── .gitignore
```
---

## License
See the `LICENSE` file for full details.
