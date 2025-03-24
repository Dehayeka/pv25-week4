import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QTextEdit

class POSApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("POS Application")
        self.setGeometry(100, 100, 400, 300)

        # Widgets
        self.title_label = QLabel("Adhyatmika Eka Saputra\nF1D022105")
        
        self.product_label = QLabel("Product")
        self.product_combo = QComboBox()
        self.products = {
            "Bimoli (Rp. 20,000)": 20000,
            "Beras 5 Kg (Rp. 75,000)": 75000,
            "Kecap ABC (Rp. 7,000)": 7000,
            "Saos Saset (Rp. 2,500)": 2500
        }
        self.product_combo.addItems(self.products.keys())

        self.quantity_label = QLabel("Quantity")
        self.quantity_input = QLineEdit()

        self.discount_label = QLabel("Discount")
        self.discount_combo = QComboBox()
        self.discount_combo.addItems(["0%", "5%", "10%", "15%"])

        self.add_button = QPushButton("Add to Cart")
        self.clear_button = QPushButton("Clear")
        
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        
        self.total_label = QLabel("Total: Rp. 0")
        
        self.error_label = QLabel("")

        # Layout
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.title_label)
        
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.product_label)
        hbox1.addWidget(self.product_combo)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.quantity_label)
        hbox2.addWidget(self.quantity_input)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.discount_label)
        hbox3.addWidget(self.discount_combo)
        
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.add_button)
        hbox4.addWidget(self.clear_button)
        
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addWidget(self.result_area)
        vbox.addWidget(self.total_label)
        vbox.addWidget(self.error_label)
        
        self.setLayout(vbox)
        
        # Connect events
        self.add_button.clicked.connect(self.add_to_cart)
        self.clear_button.clicked.connect(self.clear_fields)
        
        self.total_amount = 0

    def add_to_cart(self):
        product = self.product_combo.currentText()
        price = self.products[product]
        quantity = self.quantity_input.text()
        discount = self.discount_combo.currentText()

        if not quantity.isdigit() or int(quantity) <= 0:
            self.error_label.setText("Invalid input")
            return

        quantity = int(quantity)
        discount_value = int(discount.strip('%')) / 100
        total_price = price * quantity * (1 - discount_value)
        self.total_amount += total_price

        self.error_label.setText("")
        formatted_output = f"{product} - {quantity} x Rp. {price:,.0f} (disc {discount})"
        self.result_area.append(formatted_output)
        self.total_label.setText(f"Total: Rp. {self.total_amount:,.0f}")

    def clear_fields(self):
        self.quantity_input.clear()
        self.result_area.clear()
        self.total_amount = 0
        self.total_label.setText("Total: Rp. 0")
        self.error_label.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = POSApplication()
    window.show()
    sys.exit(app.exec_())