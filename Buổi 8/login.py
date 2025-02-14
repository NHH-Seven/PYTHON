from PyQt6 import QtWidgets, QtGui, QtCore
import mysql.connector
import hashlib


# Form đăng nhập
class LoginForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng nhập")
        self.setGeometry(400, 200, 400, 500)
        self.setStyleSheet("background-color: #f5f5f5;")

        layout = QtWidgets.QVBoxLayout()

        title_label = QtWidgets.QLabel("Đăng nhập", self)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setPlaceholderText("Tên đăng nhập")
        self.username_input.setStyleSheet(self.input_style())
        layout.addWidget(self.username_input)

        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setPlaceholderText("Mật khẩu")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(self.input_style())
        layout.addWidget(self.password_input)

        self.login_button = QtWidgets.QPushButton("Đăng nhập")
        self.login_button.setStyleSheet(self.button_style("#3498db"))
        self.login_button.clicked.connect(self.check_login)
        layout.addWidget(self.login_button)

        self.register_button = QtWidgets.QPushButton("Đăng ký tài khoản")
        self.register_button.setStyleSheet(self.button_style("#2ecc71"))
        self.register_button.clicked.connect(self.show_register_form)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def input_style(self):
        return """
            background-color: white;
            border: 2px solid #bdc3c7;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        """

    def button_style(self, color):
        return f"""
            background-color: {color};
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            border: none;
        """

    def connect_to_mysql(self):
        try:
            return mysql.connector.connect(
                host="localhost", user="root", password="", database="thuchanh8"
            )
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Lỗi MySQL", f"Lỗi kết nối: {err}")
            return None

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if not username or not password:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        conn = self.connect_to_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
                user = cursor.fetchone()

                if user:
                    QtWidgets.QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")
                    self.open_main_app()
                else:
                    QtWidgets.QMessageBox.critical(self, "Thất bại", "Sai tên đăng nhập hoặc mật khẩu!")
            finally:
                conn.close()

    def open_main_app(self):
        self.hide()
        from MySQLApp import MySQLApp
        self.main_app = MySQLApp()
        self.main_app.setGeometry(400, 200, 400, 300)
        self.main_app.show()

    def show_register_form(self):
        self.hide()
        self.register_form = RegisterForm()
        self.register_form.show()


# Form đăng ký
class RegisterForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng ký")
        self.setGeometry(400, 200, 400, 500)
        self.setStyleSheet("background-color: #ecf0f1;")

        layout = QtWidgets.QVBoxLayout()

        title_label = QtWidgets.QLabel("Đăng ký tài khoản", self)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setPlaceholderText("Tên đăng nhập")
        self.username_input.setStyleSheet(self.input_style())
        layout.addWidget(self.username_input)

        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setPlaceholderText("Mật khẩu")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(self.input_style())
        layout.addWidget(self.password_input)

        self.confirm_password_input = QtWidgets.QLineEdit()
        self.confirm_password_input.setPlaceholderText("Xác nhận mật khẩu")
        self.confirm_password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confirm_password_input.setStyleSheet(self.input_style())
        layout.addWidget(self.confirm_password_input)

        self.register_button = QtWidgets.QPushButton("Đăng ký")
        self.register_button.setStyleSheet(self.button_style("#2ecc71"))
        self.register_button.clicked.connect(self.register_user)
        layout.addWidget(self.register_button)

        self.back_button = QtWidgets.QPushButton("Quay lại")
        self.back_button.setStyleSheet(self.button_style("#e74c3c"))
        self.back_button.clicked.connect(self.show_login_form)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def input_style(self):
        return """
            background-color: white;
            border: 2px solid #bdc3c7;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        """

    def button_style(self, color):
        return f"""
            background-color: {color};
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            border: none;
        """

    def connect_to_mysql(self):
        try:
            return mysql.connector.connect(
                host="localhost", user="root", password="", database="thuchanh8"
            )
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Lỗi MySQL", f"Lỗi kết nối: {err}")
            return None

    def register_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if not username or not password or not confirm_password:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return
        
        if password != confirm_password:
            QtWidgets.QMessageBox.critical(self, "Lỗi", "Mật khẩu không khớp!")
            return

        conn = self.connect_to_mysql()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
                if cursor.fetchone():
                    QtWidgets.QMessageBox.critical(self, "Lỗi", "Tên đăng nhập đã tồn tại!")
                else:
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
                    conn.commit()
                    QtWidgets.QMessageBox.information(self, "Thành công", "Đăng ký thành công!")
                    self.show_login_form()
            finally:
                conn.close()

    def show_login_form(self):
        self.hide()
        self.login_form = LoginForm()
        self.login_form.show()
    def show_dangky_form(self):
        self.hide()
        self.login_form = RegisterForm()
        self.login_form.show()


    if __name__ == "__main__":
       app = QtWidgets.QApplication([])
       window = LoginForm()
       window.show()
       app.exec()
