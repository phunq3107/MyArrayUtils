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

## Merge sort

## Quick sort

## Selection sort

## Shell sort



