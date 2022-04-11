# Documentations for sort module

Các giải thuật sort được thư viện cung cấp

- [Bubble sort](#bubble-sort)
- [Heap sort](#heap-sort)
- [Insertion sort](#insertion-sort)
- [Merge sort](#merge-sort)
- [Quick sort](#quick-sort)
- [Selection sort](#selection-sort)
- [Shell sort](#shell-sort)

## Bubble sort

Sắp xếp nổi bọt (tiếng Anh: bubble sort) là một thuật toán sắp xếp đơn giản, với thao tác cơ bản là so sánh hai phần tử kề nhau, nếu chúng chưa đứng đúng thứ tự thì đổi chỗ (swap). Có thể tiến hành từ trên xuống (bên trái sang) hoặc từ dưới lên (bên phải sang). Sắp xếp nổi bọt còn có tên là sắp xếp bằng so sánh trực tiếp. Nó sử dụng phép so sánh các phần tử nên là một giải thuật sắp xếp kiểu so sánh.

Có hai cách thực hiện giải thuật là sắp xếp từ dưới lên hoặc sắp xếp từ trên xuống. Trong thư viện này ta sẽ sắp xếp từ dưới lên (so sánh cặp phần tử index 0 đầu tiên).

Hàm có cú pháp như sau:
```commandline
myarrayutils.sort.BubbleSort(arr)
```
Với arr là dữ liệu cần sắp xếp, có thể là một List hay một Dictionaries ...
Kiểu dữ liệu trả về là tương tự như biến arr.

Ngoài ra, hàm còn có hai đầu vào mở rộng để người dùng sử dụng cho nhiều mục đích khác:

cmp: nếu người dùng không chỉ định, hàm sẽ sử dụng phép so sánh đại số bình thường. Người dùng cần quan tâm tham số này khi thao tác trên các cấu trúc dữ liệu có nhiều thuộc tính. (VD tham số đầu vào là một dict có 3 thuộc tính, và cần một quy trình nhiều bước để xác định một giá trị có lớn hơn giá trị còn lại hay không, khi đó ta sẽ tạo một hàm so sánh và truyền vào thông qua tham số smp)

reverse: đầu vào mặc định là false, khi reverse là False, hàm sẽ sắp xếp các dữ liệu tăng dần, nếu là True, hàm sẽ sắp xếp dữ liệu giảm dần.

Lưu ý rằng giải thuật sort này là giải thuật không có tính ổn định.

Hàm được hiện thực có xem xét số lần hoán đổi phần tử trong một lần quét, nếu xuất hiện một lần quét mà không có phần tử nào được hoán đổi, hàm sẽ trả về kết quả ngay.
## Heap sort

## Insertion sort
Thuật toán sắp xếp chèn (Insertion Sort) là thuật toán sắp xếp hoạt động tương tự cách chúng ta sắp xếp các quân bài trên tay trong một trò chơi bài.

Để sắp xếp theo đúng trật tự, người chơi sẽ rút lần lượt từ quân bài thứ 2, sau đó so với các quân bài đứng trước nó để chèn vào vị trí thích hợp.

Tóm lại, sắp xếp chèn là thuật toán sắp xếp đặt một phần tử chưa được sắp xếp vào vị trí thích hợp của nó trong mỗi lần lặp.
Hàm có cú pháp như sau:
```commandline
myarrayutils.sort.InsertionSort(arr)
```
Với arr là dữ liệu cần sắp xếp, có thể là một List hay một Dictionaries ...
Kiểu dữ liệu trả về là tương tự như biến arr.

Ngoài ra, hàm còn có hai đầu vào mở rộng để người dùng sử dụng cho nhiều mục đích khác:

cmp: nếu người dùng không chỉ định, hàm sẽ sử dụng phép so sánh đại số bình thường. Người dùng cần quan tâm tham số này khi thao tác trên các cấu trúc dữ liệu có nhiều thuộc tính. (VD tham số đầu vào là một dict có 3 thuộc tính, và cần một quy trình nhiều bước để xác định một giá trị có lớn hơn giá trị còn lại hay không, khi đó ta sẽ tạo một hàm so sánh và truyền vào thông qua tham số smp)

reverse: đầu vào mặc định là false, khi reverse là False, hàm sẽ sắp xếp các dữ liệu tăng dần, nếu là True, hàm sẽ sắp xếp dữ liệu giảm dần.

Lưu ý rằng giải thuật sort này là giải thuật có tính ổn định.

Thuật toán sắp xếp chèn được sử dụng trong các trường hợp:
- Mảng có ít phần tử
- Mảng gần như đã được sắp xếp, chỉ một vài phần tử bị đặt sai chỗ

## Merge sort
Sắp xếp trộn (merge sort) là một thuật toán sắp xếp để sắp xếp các danh sách hoặc bất kỳ cấu trúc dữ liệu nào có thể truy cập tuần tự theo một trật tự nào đó. Thuật toán này là một ví dụ tương đối điển hình của lối thuật toán chia để trị.

Sắp xếp trộn hoạt động qua 2 bước : 
 1.Chia danh sách chưa được sắp xếp thành n danh sách con, mỗi danh sách chứa một phần tử (danh sách một phần tử được coi là đã sắp xếp).
 
 2.Liên tục hợp nhất các danh sách con để tạo ra các danh sách con được sắp xếp mới cho đến khi chỉ còn lại một danh sách con -> đây sẽ là danh sách được sắp xếp.
 
Hàm có cú pháp như sau:
```commandline
myarrayutils.sort.MergeSort(arr)
```
Với arr là dữ liệu cần sắp xếp, có thể là một List hay một Dictionaries ...
Kiểu dữ liệu trả về là tương tự như biến arr.
Ngoài ra, hàm còn có hai đầu vào mở rộng để người dùng sử dụng cho nhiều mục đích khác:

cmp: nếu người dùng không chỉ định, hàm sẽ sử dụng phép so sánh đại số bình thường. Người dùng cần quan tâm tham số này khi thao tác trên các cấu trúc dữ liệu có nhiều thuộc tính. (VD tham số đầu vào là một dict có 3 thuộc tính, và cần một quy trình nhiều bước để xác định một giá trị có lớn hơn giá trị còn lại hay không, khi đó ta sẽ tạo một hàm so sánh và truyền vào thông qua tham số smp)

reverse: đầu vào mặc định là false, khi reverse là False, hàm sẽ sắp xếp các dữ liệu tăng dần, nếu là True, hàm sẽ sắp xếp dữ liệu giảm dần.

Lưu ý rằng giải thuật sort này là giải thuật có tính ổn định nhưng đòi hỏi thêm không gian bộ nhớ để lưu các dãy phụ.
## Quick sort

## Selection sort

## Shell sort
**Shell Sort** là một giải thuật sắp xếp mang lại hiệu quả cao dựa trên giải thuật **sắp xếp chèn (Insertion Sort)**. Giải thuật này tránh các trường hợp phải tráo đổi vị trí của hai phần tử xa nhau trong giải thuật sắp xếp chọn (nếu như phần tử nhỏ hơn ở vị trí bên phải khá xa so với phần tử lớn hơn bên trái).

Đầu tiên, giải thuật này sử dụng giải thuật sắp xếp chọn trên các phần tử có khoảng cách xa nhau, sau đó sắp xếp các phần tử có khoảng cách hẹp hơn. Khoảng cách này còn được gọi là **khoảng (interval)**.

**interval** sẽ nhận giá trị lần lượt là n/2, n/4, n/8 cho đến khi interval = 1. (với n là độ dài của mảng)

Hàm có cú pháp như sau:
```commandline
myarrayutils.sort.ShellSort(arr)
```
Với arr là dữ liệu cần sắp xếp, có thể là một List hay một Dictionaries ...
Kiểu dữ liệu trả về là tương tự như biến arr.

Ngoài ra, hàm còn có hai đầu vào mở rộng để người dùng sử dụng cho nhiều mục đích khác:

cmp: nếu người dùng không chỉ định, hàm sẽ sử dụng phép so sánh đại số bình thường. Người dùng cần quan tâm tham số này khi thao tác trên các cấu trúc dữ liệu có nhiều thuộc tính. (VD tham số đầu vào là một dict có 3 thuộc tính, và cần một quy trình nhiều bước để xác định một giá trị có lớn hơn giá trị còn lại hay không, khi đó ta sẽ tạo một hàm so sánh và truyền vào thông qua tham số smp)

reverse: đầu vào mặc định là false, khi reverse là False, hàm sẽ sắp xếp các dữ liệu tăng dần, nếu là True, hàm sẽ sắp xếp dữ liệu giảm dần.

Lưu ý rằng giải thuật sort này là giải thuật không có tính ổn định.


