# Myarrayutils: Utility library for Python array

Myarrayutils là một mã nguồn mở được viết trên ngôn ngữ Python. Mục tiêu của thư viện là cung cấp một số hàm phụ trợ làm
việc với mảng. Ngoài ra, thư viện còn cung cấp sẵn một số giải thuật phục vụ cho mục đích học tập.

Là một mã nguồn mở với mục đích phục vụ học tập, mã nguồn được xây dựng theo cấu trúc cho phép người dùng mở rộng tùy
theo mục đích sử dụng.

## Hướng dẫn cài đặt

Sau khi tải mã nguồn của thư viện, tiến hành build thư viện bằng lệnh

```commandline
python setup.py bdist_wheel
```

Sử dụng pip để cài đặt

```commandline
pip install ./dist/myarrayutils-0.0.1-py3-none-any.whl
```

Trong trường hợp muốn ghi đè thư viện đã được cài đặt, sử dụng lệnh

```commandline
pip install  --force-reinstall ./dist/myarrayutils-0.0.1-py3-none-any.whl
```

## Ví dụ

```python
import myarrayutils

arr = [1, 4, 65, 2, 5]
myarrayutils.sort.QuickSort(arr, reverse=True)
```

## Documentations

Xem chi tiết trong thư mục docs

## Mở rộng

Cài đặt các thư viện cần thiết để phát triển

```commandline
pip install -r requirements.txt
```

Sau khi cài đặt các thư viên cần thiết, các module muốn thêm vào thư viện sẽ phải lưu trong thư mục myarrayutils. Để
test các module, các file test sẽ phải lưu trong thư mục tests.

Để chạy các testcase, dùng lệnh

```commandline
python setup.py pytest
```

Để build thư viện, dùng lệnh

```commandline
python setup.py bdist_wheel
```