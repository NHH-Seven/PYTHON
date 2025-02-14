from PyQt6 import QtWidgets, QtGui
import mysql.connector

class MySQLApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý dữ liệu MySQL")
        self.setGeometry(100, 100, 900, 500)
        
        self.initUI()
        self.load_tables()
    
    def initUI(self):
        layout = QtWidgets.QHBoxLayout(self)
        
        # Danh sách bảng
        self.table_list = QtWidgets.QListWidget()
        self.table_list.itemClicked.connect(self.on_table_select)
        layout.addWidget(self.table_list, 1)
        
        # Bảng dữ liệu
        self.table_view = QtWidgets.QTableWidget()
        layout.addWidget(self.table_view, 3)
        
        # Nút thao tác
        button_layout = QtWidgets.QVBoxLayout()
        self.add_button = QtWidgets.QPushButton("Thêm dữ liệu")
        self.edit_button = QtWidgets.QPushButton("Sửa dữ liệu")
        self.delete_button = QtWidgets.QPushButton("Xóa dữ liệu")
        
        self.add_button.clicked.connect(self.add_data)
        self.edit_button.clicked.connect(self.edit_data)
        self.delete_button.clicked.connect(self.delete_data)
        
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        layout.addLayout(button_layout, 1)
    
    def connect_to_mysql(self):
        try:
            return mysql.connector.connect(
                host="localhost", user="root", password="", database="thuchanh8"
            )
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Lỗi MySQL", f"Lỗi kết nối: {err}")
            return None
    
    def load_tables(self):
        conn = self.connect_to_mysql()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            if tables:
                self.table_list.addItems([table[0] for table in tables])
            else:
                QtWidgets.QMessageBox.warning(self, "Cảnh báo", "Không có bảng nào trong CSDL.")
            conn.close()
    
    def on_table_select(self, item):
        self.table_name = item.text()
        conn = self.connect_to_mysql()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute(f"SELECT * FROM {self.table_name}")
                self.columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()

                self.table_view.setColumnCount(len(self.columns))
                self.table_view.setRowCount(len(rows))
                self.table_view.setHorizontalHeaderLabels(self.columns)

                for row_idx, row in enumerate(rows):
                    for col_idx, col_value in enumerate(row):
                        self.table_view.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_value)))
            except mysql.connector.Error as err:
                QtWidgets.QMessageBox.critical(self, "Lỗi", f"Lỗi khi tải dữ liệu:\n{err}")
            finally:
                conn.close()
    
    def add_data(self):
        if not hasattr(self, "table_name"):
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một bảng!")
            return

        conn = self.connect_to_mysql()
        if not conn:
            return

        cursor = conn.cursor()
        cursor.execute(f"DESCRIBE {self.table_name}")
        columns = [col[0] for col in cursor.fetchall()]
        cursor.close()

        input_dialog = QtWidgets.QDialog(self)
        input_dialog.setWindowTitle("Thêm dữ liệu")
        layout = QtWidgets.QFormLayout(input_dialog)

        input_fields = {}
        for col in columns:
            field = QtWidgets.QLineEdit()
            layout.addRow(f"{col}:", field)
            input_fields[col] = field

        btn_submit = QtWidgets.QPushButton("Thêm")
        btn_cancel = QtWidgets.QPushButton("Hủy")

        def submit_data():
            values = [field.text() for field in input_fields.values()]
            if any(v == "" for v in values):
                QtWidgets.QMessageBox.warning(input_dialog, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
                return
            
            placeholders = ", ".join(["%s"] * len(values))
            insert_query = f"INSERT INTO {self.table_name} ({', '.join(columns)}) VALUES ({placeholders})"
            
            try:
                conn = self.connect_to_mysql()
                cursor = conn.cursor()
                cursor.execute(insert_query, values)
                conn.commit()
                self.on_table_select(self.table_list.currentItem())
                input_dialog.accept()
            except mysql.connector.Error as err:
                QtWidgets.QMessageBox.critical(self, "Lỗi", f"Lỗi khi thêm dữ liệu: {err}")
            finally:
                cursor.close()
                conn.close()

        btn_submit.clicked.connect(submit_data)
        btn_cancel.clicked.connect(input_dialog.reject)
        
        layout.addRow(btn_submit, btn_cancel)
        input_dialog.exec()
    
    def edit_data(self):
        selected_row = self.table_view.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một dòng để sửa!")
            return

        selected_data = [self.table_view.item(selected_row, i).text() for i in range(self.table_view.columnCount())]
        primary_key = self.columns[0]
        primary_value = selected_data[0]

        input_dialog = QtWidgets.QDialog(self)
        input_dialog.setWindowTitle("Sửa dữ liệu")
        layout = QtWidgets.QFormLayout(input_dialog)

        input_fields = {}
        for i, col in enumerate(self.columns):
            field = QtWidgets.QLineEdit(selected_data[i])
            layout.addRow(f"{col}:", field)
            input_fields[col] = field

        btn_submit = QtWidgets.QPushButton("Lưu")
        btn_cancel = QtWidgets.QPushButton("Hủy")

        def update_data():
            values = [field.text() for field in input_fields.values()]
            update_query = f"UPDATE {self.table_name} SET " + ", ".join([f"{col}=%s" for col in self.columns]) + f" WHERE {primary_key}=%s"
            
            try:
                conn = self.connect_to_mysql()
                cursor = conn.cursor()
                cursor.execute(update_query, values + [primary_value])
                conn.commit()
                self.on_table_select(self.table_list.currentItem())
                input_dialog.accept()
            except mysql.connector.Error as err:
                QtWidgets.QMessageBox.critical(self, "Lỗi", f"Lỗi khi sửa dữ liệu: {err}")
            finally:
                cursor.close()
                conn.close()

        btn_submit.clicked.connect(update_data)
        btn_cancel.clicked.connect(input_dialog.reject)
        
        layout.addRow(btn_submit, btn_cancel)
        input_dialog.exec()
    
    def delete_data(self):
        selected_row = self.table_view.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một dòng để xóa!")
            return

        primary_key = self.columns[0]  
        primary_value = self.table_view.item(selected_row, 0).text()  

        confirm = QtWidgets.QMessageBox.question(
            self, "Xác nhận xóa", f"Bạn có chắc muốn xóa dữ liệu có {primary_key} = {primary_value}?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )

        if confirm == QtWidgets.QMessageBox.StandardButton.Yes:
            try:
                conn = self.connect_to_mysql()
                cursor = conn.cursor()
                cursor.execute(f"DELETE FROM {self.table_name} WHERE {primary_key} = %s", (primary_value,))
                conn.commit()

                self.on_table_select(self.table_list.currentItem())  
                QtWidgets.QMessageBox.information(self, "Xóa thành công", "Dữ liệu đã bị xóa!")
            except mysql.connector.Error as err:
                QtWidgets.QMessageBox.critical(self, "Lỗi", f"Lỗi khi xóa dữ liệu: {err}")
            finally:
                cursor.close()
                conn.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MySQLApp()
    window.show()
    app.exec()







# -- Tạo cơ sở dữ liệu student_db
# CREATE DATABASE IF NOT EXISTS student_db;

# -- Sử dụng cơ sở dữ liệu vừa tạo
# USE student_db;


# -- Tạo cơ sở dữ liệu student_db
# CREATE DATABASE IF NOT EXISTS student_db;

# -- Sử dụng cơ sở dữ liệu vừa tạo
# USE student_db;

# -- Tạo bảng students
# CREATE TABLE IF NOT EXISTS students (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     age INT CHECK (age > 0),
#     gender ENUM('Nam', 'Nữ') NOT NULL,
#     grade FLOAT CHECK (grade >= 0 AND grade <= 10)
# );

# -- Chèn dữ liệu vào bảng
# INSERT INTO students (name, age, gender, grade) VALUES
# ('Nguyễn Văn A', 20, 'Nam', 8.5),
# ('Trần Thị B', 22, 'Nữ', 9.2),
# ('Lê Văn C', 21, 'Nam', 7.8),
# ('Phạm Thị D', 19, 'Nữ', 6.4),
# ('Đặng Văn E', 23, 'Nam', 5.9),
# ('Hoàng Minh F', 20, 'Nam', 9.0),
# ('Vũ Thị G', 21, 'Nữ', 7.0),
# ('Lê Thị H', 22, 'Nữ', 8.8),
# ('Ngô Văn I', 20, 'Nam', 4.5),
# ('Bùi Văn J', 24, 'Nam', 6.2);

# -- 1. Hiển thị tất cả dữ liệu trong bảng students
# SELECT * FROM students;

# -- 2. Lọc sinh viên có điểm trung bình lớn hơn 8.0
# SELECT * FROM students WHERE grade > 8.0;

# -- 3. Đếm số lượng sinh viên theo giới tính
# SELECT gender, COUNT(*) AS total FROM students GROUP BY gender;

# -- 4. Sắp xếp danh sách sinh viên theo điểm số giảm dần
# SELECT * FROM students ORDER BY grade DESC;

# -- 5. Cập nhật điểm của sinh viên có ID = 1
# UPDATE students SET grade = 9.0 WHERE id = 1;

# -- 6. Xóa sinh viên có điểm dưới 5.0
# DELETE FROM students WHERE grade < 5.0;

# -- 7. Tìm sinh viên có tên chứa 'Nguyễn'
# SELECT * FROM students WHERE name LIKE '%Nguyễn%';

# -- 8. Tính điểm trung bình của tất cả sinh viên
# SELECT AVG(grade) AS avg_grade FROM students;

# -- 9. Lấy 3 sinh viên có điểm cao nhất
# SELECT * FROM students ORDER BY grade DESC LIMIT 3;

# -- 10. Kiểm tra số lượng sinh viên theo độ tuổi
# SELECT age, COUNT(*) AS total FROM students GROUP BY age;

# -- 11. Lấy danh sách sinh viên có độ tuổi từ 20 đến 25
# SELECT * FROM students WHERE age BETWEEN 20 AND 25;

# -- 12. Lấy danh sách sinh viên theo giới tính và sắp xếp theo tên
# SELECT * FROM students WHERE gender = 'Nữ' ORDER BY name;

# -- 13. Lấy danh sách sinh viên có điểm cao nhất theo giới tính
# SELECT * FROM students WHERE grade = (SELECT MAX(grade) FROM students);

# -- 14. Hiển thị số lượng sinh viên có điểm trên mức trung bình
# SELECT COUNT(*) FROM students WHERE grade > (SELECT AVG(grade) FROM students);

# -- 15. Hiển thị danh sách tất cả các bảng trong cơ sở dữ liệu student_db
# SHOW TABLES;

