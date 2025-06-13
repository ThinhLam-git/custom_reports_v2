# Module Báo cáo đơn hàng - tồn kho (v2)

## Giới thiệu
Module này cung cấp các tính năng báo cáo và thống kê cho đơn hàng và tồn kho trong hệ thống Odoo. Được phát triển bởi LamTuanThinh22521408, module này giúp người dùng dễ dàng theo dõi và phân tích dữ liệu kinh doanh.

## Tính năng chính

### 1. Thống kê Đơn hàng
- Xem và phân tích đơn hàng với nhiều bộ lọc:
  - Trạng thái đơn hàng
  - Khoảng thời gian
  - Sản phẩm
  - Khách hàng
  - Thành phố
- Hiển thị dữ liệu dưới dạng biểu đồ thống kê trực quan

### 2. Báo cáo Tồn kho
- Theo dõi số lượng sản phẩm còn lại trong kho
- Cung cấp cái nhìn tổng quan về tình trạng tồn kho

## Yêu cầu hệ thống
Module này phụ thuộc vào các module Odoo sau:
- sale_management
- stock
- board
- uom

## Cài đặt
1. Đảm bảo đã cài đặt các module phụ thuộc
2. Cài đặt module thông qua giao diện Odoo Apps
3. Khởi động lại server Odoo

## Cấu trúc thư mục
```
custom_reports_v2/
├── models/
│   ├── __init__.py
│   └── sale_order_custom_report_line.py
├── views/
│   ├── sale_order_statistics_views.xml
│   ├── inventory_report_views.xml
│   └── report_menus.xml
├── security/
│   └── ir.model.access.csv
├── static/
├── __init__.py
└── __manifest__.py
```

## Phiên bản
- Phiên bản hiện tại: 2.13

## Giấy phép
Module này được phát hành dưới giấy phép LGPL-3.

## Hỗ trợ
Để được hỗ trợ, vui lòng liên hệ với tác giả: LamTuanThinh22521408 
