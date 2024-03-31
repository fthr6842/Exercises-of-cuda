# test-of-cuda
### 1. GPU
#### GPU為圖形處理器用於數據運算(大量、重複性的計算任務)，相對地，CPU適合複雜的邏輯運算
### 2.GPU性能指標
#### a. 核心數
#### b. 顯存容量 (相當於內存)
#### c. 計算峰值
#### d. 顯存帶寬 (通信速率)
### 3. GPU+CPU架構
#### 首先，GPU無法單獨運算
#### CPU做為控制，稱為主機(host)
#### GPU作為CPU的協助處理器，稱為設備(device)
#### 主機和設備間的內存放間通過PCIe總線連接(較慢)
### 4. CUDA
#### Nvidia於2006年發布
#### 建立在Nvidia之GPU上的一個通用計算平台和編程模型
#### 支援C、C++、python、fortran
### 5. API
#### CUDA提供兩層API接口 (運行Runtime、驅動Driver)
#### 兩者調用性能無異
### 6. 編譯
#### C++編譯: gcc ...cpp -o ...
#### CUDA編譯: nvcc ...cu -o ...


