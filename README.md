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
### 7.核函數(Kernel function)
#### 在GPU上並行執行
#### 以限定詞__global__修飾
#### 返回值必須是void
#### __global__與void的位置可互換
#### 注意事項:
#### a. 核函數只能訪問GPU的內存空間(設備內存)
#### b. 核函數不能使用變長參數
#### c. 核函數不能使用靜態變數
#### d. 核函數不能使用函數指針
#### e. 核函數具有異步性
#### CUDA程式中的核函數執行與主機程式碼執行是異步的。在CUDA程式設計中，通常使用異步操作來最大程度地利用GPU的並行計算能力。
### 8. CUDA編寫程序
#### a. 主機程式碼
#### b.核函數調用
#### c. 主機程式碼(將GPU運算結果回傳給CPU主機)
#### Note: 核函數不支持CPP的iostream
### 9. 線程模型結構
#### a. grid: 網格
#### b. block: 線程塊
#### 邏輯上的劃分、並非物理意義
#### 配置: <<<grid_size, block_size>>>
#### 最大線程塊: 1024
#### 最大網格大小: 2^31 - 1 (針對一維網格)
### 10. 一維線程模型
#### 每個線程在核函數中有唯一標示
#### 每個線程的維一表示由<<<grod_size, block_size>>>確定，二者為內建變數(built-in variable)
#### a. gridDim.x: 
#### b. blockDim.x: 
#### 線程索引保存成內建變數
#### a. blockIdx.x: 變數指定一個線程在一個網格中的線程塊索引值，0 ~ gridDim.x - 1
#### b. threadIdx.x: 變數指定一個線程在一個線程塊中的線程索引值，0 ~ blockDim - 1
#### ex. <<<2, 4>>>: 網格中有2個線程塊(0 1)，每個線程塊有4個線程(0 1 2 3)
#### =>gridDim.x == 2； blockDim.x == 4； blockIdx.x == 0~1； threadIdx.x == 0~3
#### 線程唯一標示: Idx = threadIdx.x + blockIdx.x * blockDim.x
### 11. 多維線程
#### CUDA可以組織三維的網格、線程塊
#### blockIdx、threadIdx是類型維uint3的變數，具有x、y、z三個無符號成員
#### 定義多維網格和線程塊
#### dim3 grid_size(Gx, Gy, Gz)
#### dim3 block_size(Bx, By, Bz)
### 12. 一維網格、一維線程塊
#### int id = blockIdx.x + blockDim.x * threadIdx.x;
#### (線程塊索引 + 線程數量 * 線程索引)
### 13. 二維網格、二維線程塊
#### int blockId = blockIdx.x + blockId.y * gridDim.x
#### int threadId = threadIdx.x + threadIdx.y * blockDim.x
#### int id = blockId * (blockDim.x * blockDim.y) + threadId
### 14. 三維網格、三維線程塊
#### int blockId = blockIdx.x + blockIdx.y * gridDim.x
#### int threadId = threadIdx.x + (threadx.y * blockDim.x) + (threadIdx.z * (blockDim.x * blockDim.y))
#### int id = threadId + blockId * (blockDim.x * blockDim.y * blockDim.z)
####
















