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

### mã giả của giải thuật
```commandline
lặp lại công việc sau 
    i tăng dần từ 0 đến (n - số lần quét - 1)
        so sánh arr[i] và arr[i+1]
        nếu nó chưa đúng thứ tự thì đổi chỗ cho nhau 
    nếu lần quét này không có sự đổi chỗ nào thì kết thúc giải thuật
    tăng số lần quét lên 1
```

## Heap sort

## Insertion sort

## Merge sort

## Quick sort

## Selection sort

## Shell sort



