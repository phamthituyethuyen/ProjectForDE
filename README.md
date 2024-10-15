
# PROJECT: COMMAND LINE TO ANALYST MOVIE DATA (UBUNTU)

# DESCRIPTION FOR PROJECT

    Data: https://raw.githubusercontent.com/yinghaoz1/tmdb-movie-dataset-analysis/master/tmdb-movies.csv

Dữ liệu trên đang được đặt trên Linux server, cần team Data Engineer sử dụng command line Linux hỗ trợ các tác vụ sau để có các thông tin cơ bản về dữ liệu

1. Sắp xếp các bộ phim theo ngày phát hành giảm dần rồi lưu ra một file mới
2. Lọc ra các bộ phim có đánh giá trung bình trên 7.5 rồi lưu ra một file mới
3. Tìm ra phim nào có doanh thu cao nhất và doanh thu thấp nhất
4. Tính tổng doanh thu tất cả các bộ phim
5. Top 10 bộ phim đem về lợi nhuận cao nhất
6. Đạo diễn nào có nhiều bộ phim nhất và diễn viên nào đóng nhiều phim nhất
7. Thống kê số lượng phim theo các thể loại. Ví dụ có bao nhiêu phim thuộc thể loại Action, bao nhiêu thuộc thể loại Family, ….
8. Idea của bạn để có thêm những phân tích cho dữ liệu?

DOING:

# STEP 1: Tải file và kiểm ta cấu trúc file

        wget, head -n 1 <tên file>, nano <tên file>

# STEP 2: Sắp xếp các bộ phim theo ngày phát hành

        (head -n 1 movies.csv && tail -n +2 movies.csv | sort -t, -k2,2r) > sorted_movies.csv

Giải thích:
 - lấy dòng đầu tiên của file (head)
 - Nếu thành công thì lấy tất cả từ dòng thứ 2 trở xuống (tail)
 - Kết quả của hai cái trên sẽ được sử dụng sắp xếp : -t chỉ định dấu ',' dùng để phân tách cột, k2,2 chỉ định cột thử 2 là cột cần sắp xếp, r là ám chỉ reverse (giảm dần) và kết quả sẽ được lưu vào file>
Cách hoạt động của `&&`:

- Nếu lệnh bên trái của `&&` thực thi thành công (mã thoát là `0`), thì lệnh bên phải sẽ được thực thi.
        - Nếu lệnh bên trái thất bại (mã thoát khác `0`), thì lệnh bên phải sẽ không được thực thi

# STEP 3: Lọc phim có giá trị trung bình trên 7.5 (trong file bash)

# STEP 4: Fiml có doanh thu cao nhất và thấp nhất
TÌM MAX:
 
        <tên biến>=$(csvsort -c revenue <tên file fiml> | csvcut -c <tên cột muốn chọn> | tail -n 1)
        echo "<Thông báo tùy chọn>"; csvgrep -c <cột muốn tìm> -r "^$<tên biến>" <tên file fiml> |csvcut -c <tên cột tên fiml, tên cột doanh thu>
Giải thích:
  - sắp xếp theo cột
  - chọn cột muốn hiển thị
  - Lấy dòng cuối cùng
  - Lọc film có giá trị trùng với giá được tìm
  - GIải thích cú pháp: -r ám chỉ sử dụng regrex

# STEP 5:  10 bộ phim đạt doanh thu cao nhất
        mlr --csv put '$profits=$revenue - $budget' movies.csv | csvcut -c original_title,profits | csvsor>
Giải thích :
  - mrl: là lệnh của công cụ Miller (giống AWK)
  - -csv chỉ định đầu vào là csv
  - put: từ khóa dùng để cập nhật hoặc tạo trong dữ liệu
  -  thêm cột mới $profit tính bỏi cột $revenue - $budget từ trong file movies.csv (tên file fiml)

# STEP 6: Đạo diễn và diễn viễn có nhiều fiml nhất
        awk -F, '{print $9}' movies.csv | tr '|' '\n' | awk 'NF > 0' | sort | uniq -c | sort -n | tail -n 1
Giải thích
   - F đặt dấu phẩy làm dấu phân cách
   - print$9 in ra các dòng của cột $9
   - tr : translate | thành \n
   - NF biến nội tại trong awk lưu số lượng trường, >0 dòng nào có ít nhất một trường thì thỏa diều >
   - uniq -c: đếm số lần xuất hiện vủa các giá trị duy nhất (phải sắp xếp gần nhau)
   - TƯơng tự cho diễn viên

# STEP 7: Thống kê số lượng phim theo thể loại
        Làm như step 6

# STEP 8: idea những phân tích dữ liệu tiếp theo 
   - PHân tích những thể loại phim  được vote cao nhất
   - Những thể loại  fiml nào được ưa chọn nhất trong từng giai đoạn thời gian
   - THế mạnh của các đạo diễn là về thể loại phim gì và thế mạnh của diễn viên
   - Các công ty sản xuất phim nào  có doanh thu cao nhất 
