# yolo_roboflow
roboflow기반 yolo활용

# 가상환경 만들기
```powershell
# 현재 PowerShell에서 스크립트 실행 허용
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

```
uv init --bare --python 3.12 --name yolo-ex
uv python pin 3.12
```

# 주피터 노트북 환경만들기
```
uv add ipykernel
uv run python -m ipykernel install --user --name .venv
```

# uv 가상환경에 torch cuda 버전 설치하기
- pyproject.toml 환경셋팅
```
[[tool.uv.index]]
name = "pytorch-cu126"
url = "https://download.pytorch.org/whl/cu126"
explicit = true

[tool.uv.sources]
torch = { index = "pytorch-cu126" }
torchvision = { index = "pytorch-cu126" }
```

- torch 설치하기
```
uv add torch torchvision
```

# 라이브러리 설치
```
uv add inference-sdk
uv add python-dotenv
uv add roboflow
uv add "opencv-python==4.12.0.88"
uv add ultralytics
```

# opencv-python-headless 충돌 해결
- `roboflow`가 `opencv-python-headless`를 의존성으로 끌어와 `opencv-python`(GUI 빌드)과
  같은 `cv2` 모듈을 덮어씀 → `cv2.imshow` 등 GUI 함수 호출 시 아래 에러 발생
```
error: (-2:Unspecified error) The function is not implemented.
Rebuild the library with Windows, GTK+ 2.x or Cocoa support.
```
- pyproject.toml 에 override 추가하여 headless 버전을 아예 설치하지 않도록 함
```
[tool.uv]
override-dependencies = ["opencv-python-headless ; sys_platform == 'never'"]
```
- 이후 재설치
```
uv sync
uv pip install --reinstall opencv-python==4.12.0.88
```
- 확인: `cv2.getBuildInformation()` 출력의 `GUI: WIN32UI`, `Win32 UI: YES`

# jupyter lab 사용
- jupyterlab 설치
```
uv add jupyterlab
```

- jupyterlab 실행
```
uv run jupyter lab
```
