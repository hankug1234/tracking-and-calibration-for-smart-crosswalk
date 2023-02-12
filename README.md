# 엣지 컴퓨팅 영상 인식 기반의 지능형 보행 감지 시스템 

## tracking
![tracking-image.png](./venv/trackalg.png)
저희 custom tracking 알고리즘은 xavior에서 낮은 delay를 달성 하기 위해 iou 기반이 아닌 거리 기반의 mapping 방식을 체택 하였습니다.
그 이유는 sort 알고리즘에서 iou 즉 과거 frame 과 현 frame 에서 감지된 물체의를 감싸는 bounding box의 겹치는 정도를 기준 으로 mappin을 진행 하게 되며
이 iou 값의 정확도를 높이기 위해 칼만 필터를 이용하여 detecting 된 물체의 bounding box 크기를 조정 하여 사람이 들어 있지 않은 불필요한 부분은 제거 하는 것이기 때문에 overhead가 높은 칼만 필터를 제거 하면서 정확도 손실을 줄이기 위해 현재 탐색된 object 들의 아이디가 과거 주변에 가장 가까이 위치했던 object에 mapping 되도록 tracking
알고리즘을 디자인 하였습니다 또한 mapping을 위한 후보 군들의 숫자를 줄이기 위해 물체의 이동 방향과 속도를 고려 하여 한프레임 내에 이동 가능한 영역을 설정 한 후
이동 가능 영역에 존재하는 object 만인 mapping 후보군이 되게 하였으며 이동 방향을 고려 하여 주 이동 방향에 더 넓은 이동 가능 영역을 할당하고 나머지 부분의 이동영역을 좁혀
다른 object의 간섭을 최소화 하였습니다 이와 같은 경량화를 통해 칼만 필터의 보정 overhead를 감소 시키  면서 정확도 손실을 최소화 하였으며 0.1~0.5 정도의 delay를 달성하여 sort 대비 2배 정도의 tracking 속도를 달성 하였습니다 

### MOTA
![mota1.png](./venv/mota1.png)
![mota2.png](./venv/mota2.png)
![mota3.png](./venv/mota3.png)
![mota4.png](./venv/mota4.png)
![mota5.png](./venv/mota5.png)
![mota6.png](./venv/mota6.png)
![mota7.png](./venv/mota7.png)
![mota8.png](./venv/mota8.png)
![mota9.png](./venv/mota9.png)
![mota10.png](./venv/mota10.png)
![mota11.png](./venv/mota11.png)


## calibration
2차원 이미지 상의 좌표를 3차원 좌표로 mapping 시켜주는 과정을 calibration 이라고 한다. 이번 프로젝트에서 사용한 calbration 알고리즘은 opencv에서 제공해 주는 기능을 활용 하여
구성하였다. opencv의 chess board 코너를 추출하는 알고리즘을 사용하여 이미지상에서 현실 세상과 mapping할 좌표를 추출 한후 opencv의 calibration 기능과 추출한 real world 좌표를 사용해 카메라 내부 factor와 촬영 방향 정보를 추출 하고 추출한 값들을 카메라 렌즈 왜곡율을 고려하여 보정한후 좌표 변환 공식을 활용하여 2d 좌표를 3d 좌표로 mapping 하였다
![c1.png](./venv/c1.png)
![c2.png](./venv/c2.png)
![c3.png](./venv/c3.png)
