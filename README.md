# PacMan
#1
CHúng ta dùng thuật toán DFS.
dùng 1 stack để lưu các state, dùng 1  mảng visit để lưu những đỉnh đã đi qua, 1 mảng path để lưu trữ dữ liệu tạm trong mỗi lần lập
mỗi 1 state( phần tử của stack) chúng ta lưu vị trí của pacman, và đường hiện tại đến đó
Tiếp theo là dùng 1 vòng lặp while lặp cho đến khi tìm được đích hoặc tất cả các nút đã đi qua
Trong mỗi lần lặp nếu nút hiện tại ta chesck các điều kiện dừng. và lấy tất cả con của nó, những nút chưa có mặt trong mảng visit thì cho vào stack


#2
CHúng ta dùng thuật toán BFS
Lm tương tự câu 1 chỉ khắc thay Stack thành Queue
Ngoài việc đó chúng ta cần thêm một mảng add để check xem phần tử này đã được add vào queue hay chưa để tránh trùng lặp.


#3
UCS   pacman sẽ con đường từ điểm hiện tại tới 1 vị trí với chi phí ngắn nhất
V ý tưởng vẫn tương tự 2 câu trên 
Cúng ta dùng priority queue
Mi state chúng ta sẽ lưu vị trí đường đi đến vị trí đó và số biểu thị độ ưu tiên. Độ ưu tiên ở đây là số bước đi ở path
Về việc check điều kiện dừng cũng tương tự
Khi chúng ta thêm 1 state vào PriQue chúng ta cần phải check xem state đó có ở đó sẵn hay chưa, có rồi thì add thêm, chưa có thì update

#4
A* search
thuật toán này cũng như UCS chỉ khác về độ ưu tiên chúng ta  + thêm hàm heuristic(ở đây là Mahatan), Pacman trông có vẻ đi đúng hướng.
Độ ưu tiên = số bước đi trong path + h(manattan) từ vị trí đầu đến vị trí hiện tại 

#5
Finding All the Corners
thuật toán BFS
Mỗi state ta lưu  vị trí, đường đi , cost (ở đây là 1 hết)
Tại hàm isGoalState: chúng ta cần phải lấy ra listvisited rồi check xem nếu nó bằng 4 trả về true, ngược lại trả về false

#6
Tại đây chúng ta thiết kế hàm H cho bài toán 4 thức ăn 4 góc
Giải thuật là:
Tham lam, pacman lấy mảng các cornner và chọn cornner gần nhất đầu tiên. tiếp theo từ vị trí đó chọn cornner gần nhất thử 2, cứ vậy đến khi hết mảng corner chưa visit. tổng manhattan đó là hàm h()

#7
Ở phần này chúng ta cũng chỉ code hàm h
Giải thuật là:
mỗi một state lấy ra mảng foodlist chưa đi qua.
Trong mảng đó chúng ta tìm ra 2 phần tử food xa nhau nhất,bằng hàm mazedistance()
kết quả trả về là khoảng cách đường đi từ vị trí hiện tại đến nút gần hơn trong 1 trong 2 nút trên + với khoảng cách 2 nút trên.

#8
Chúng ta chỉ đơn giản là tím thức ăn gần nhất.
hàm isgoalstate chỉ cần check state có nằm trong food list là trả về true.


