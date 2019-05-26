from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import mysql.connector
import sys

from PyQt5.uic import loadUiType

ui,_ = loadUiType('library.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_ui_changes()
        self.handle_buttons()
        self.show_category()
        self.show_author()
        self.show_publisher()
        self.show_in_combobox_category()
        self.show_in_publisher_combobox()
        self.show_in_author_combobox()
        #self.add_new_book()
        #self.edit_book()

    def handle_buttons(self):
        self.pushButton_5.clicked.connect(self.show_themes)
        self.pushButton_22.clicked.connect(self.hide_themes)
        self.pushButton.clicked.connect(self.open_daytoday_tab)
        self.pushButton_2.clicked.connect(self.open_books_tab)
        self.pushButton_3.clicked.connect(self.open_users_tab)
        self.pushButton_4.clicked.connect(self.open_settings_tab)
        self.pushButton_7.clicked.connect(self.add_new_book)
        self.pushButton_16.clicked.connect(self.add_category)
        self.pushButton_17.clicked.connect(self.add_author)
        self.pushButton_15.clicked.connect(self.add_publisher)
        self.commandLinkButton.clicked.connect(self.search_books)
        self.pushButton_8.clicked.connect(self.edit_book)
        self.pushButton_11.clicked.connect(self.delete_books)

    def handle_ui_changes(self):
        self.hide_themes()
        self.tabWidget.tabBar().setVisible(False)

    def show_themes(self):
        self.groupBox_3.show()

    def hide_themes(self):
        self.groupBox_3.hide()
##################tab operations################
    def open_daytoday_tab(self):
        self.tabWidget.setCurrentIndex(0)

    def open_books_tab(self):
        self.tabWidget.setCurrentIndex(1)

    def open_users_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def open_settings_tab(self):
        self.tabWidget.setCurrentIndex(3)

########################books###################

    def add_new_book(self):
        self.db = mysql.connector.connect(host ='localhost' ,user ='root',password ='' ,db = 'library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()
        book_description = self.textEdit.toPlainText()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_3.currentIndex()
        book_author = self.comboBox_4.currentIndex()
        book_publisher = self.comboBox_5.currentIndex()
        book_price = self.lineEdit_4.text()

        self.cur.execute('''
            INSERT INTO books(book_title,book_description,book_code,book_category,book_author,book_publisher,book_price)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        ''',(book_title,book_description,book_code,book_category,book_author,book_publisher,book_price))


        self.db.commit()
        self.statusBar().showMessage('Book added successfully')
        self.lineEdit_2.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_3.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_4.setText('')




    def search_books(self):

        self.db = mysql.connector.connect(host ='localhost' ,user ='root',password ='' ,db = 'library')
        self.cur = self.db.cursor()
        book_title = self.lineEdit_9.text()

        sql = ''' SELECT * from books WHERE book_title = %s '''
        self.cur.execute(sql,[(book_title)])

        data = self.cur.fetchone()
        self.lineEdit_10.setText(data[1])
        self.textEdit_2.setPlainText(data[2])
        self.lineEdit_7.setText(data[3])
        self.comboBox_6.setCurrentIndex(data[4])
        self.comboBox_7.setCurrentIndex(data[5])
        self.comboBox_8.setCurrentIndex(data[6])
        self.lineEdit_6.setText(str(data[7]))

    def edit_book(self):
        self.db = mysql.connector.connect(host ='localhost' ,user ='root',password ='' ,db = 'library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_10.text()
        book_description = self.textEdit_2.toPlainText()
        book_code = self.lineEdit_7.text()
        book_category = self.comboBox_6.currentIndex()
        book_author = self.comboBox_7.currentIndex()
        book_publisher = self.comboBox_8.currentIndex()
        book_price = self.lineEdit_6.text()

        search_book_title = self.lineEdit_9.text()

        self.cur.execute('''
            UPDATE books SET book_title =%s,book_description=%s,book_code =%s,book_category =%s,book_author=%s,book_publisher=%s,book_price=%s WHERE book_title =%s
        ''',(book_title,book_description,book_code,book_category,book_author,book_publisher,book_price,search_book_title))

        self.db.commit()
        self.statusBar().showMessage('Book edited successfully')
        self.lineEdit_10.setText('')
        self.textEdit_2.setPlainText('')
        self.lineEdit_7.setText('')
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_8.setCurrentIndex(0)
        self.lineEdit_6.setText('')
    def delete_books(self):
        self.db = mysql.connector.connect(host ='localhost' ,user ='root',password ='' ,db = 'library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_9.text()
        warning = QMessageBox.warning(self, 'Delete Book', "are you sure you want top delete the book!!!", QMessageBox.Yes|QMessageBox.No)
        if warning == QMessageBox.Yes:
            self.cur.execute(''' DELETE FROM books WHERE book_title=%s''',[(book_title)])
            self.db.commit()
        self.statusBar().showMessage('Book edited successfully')
        self.lineEdit_10.setText('')
        self.textEdit_2.setPlainText('')
        self.lineEdit_7.setText('')
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_8.setCurrentIndex(0)
        self.lineEdit_6.setText('')
        self.statusBar().showMessage('Book deleted')




########################books###################

    def add_new_user(self):
        pass

    def login(self):
        pass

    def edit_user(self):
        pass
########################settings###################

    def add_category(self):
        self.db = mysql.connector.connect(host ='localhost' ,user ='root',password ='' ,db = 'library')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_30.text()

        self.cur.execute('''
            INSERT INTO category(category_name) VALUES (%s)
        ''',(category_name,))

        self.db.commit()
        self.statusBar().showMessage('New Category Added')
        self.lineEdit_30.setText('')
        self.show_category()
        self.show_in_combobox_category()

    def show_category(self):
        self.db = mysql.connector.connect(host ='localhost' ,user ='root',password ='' ,db = 'library')
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT category_name FROM category
        ''')
        data = self.cur.fetchall()
        #print(data)
        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row,column,QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)


    def add_author(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = '',db = 'library')
        self.cur = self.db.cursor()

        author_name = self.lineEdit_31.text()

        self.cur.execute('''
            INSERT INTO authors(author_name) VALUES (%s)

        ''',(author_name,))

        self.db.commit()
        self.statusBar().showMessage('author added successfully')
        self.lineEdit_31.setText('')
        self.show_author()
        self.show_in_author_combobox()


    def show_author(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT author_name FROM authors
        ''')

        data1 = self.cur.fetchall()
        if data1:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row,form in enumerate(data1):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column,QTableWidgetItem(str(item)))
                    column+=1

                row_position1 = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position1)


    def add_publisher(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = '',db = 'library')
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_29.text()

        self.cur.execute('''
            INSERT INTO publisher(publisher_name) VALUES (%s)

        ''',(publisher_name,))
        self.db.commit()
        self.statusBar().showMessage('publisher added successfully')
        self.lineEdit_29.setText('')
        self.show_publisher()
        self.show_in_publisher_combobox()


    def show_publisher(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT publisher_name FROM publisher
        ''')

        data2 = self.cur.fetchall()
        if data2:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row,form in enumerate(data2):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column,QTableWidgetItem(str(item)))
                    column+=1

                row_position2 = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position2)

########################display settings data###################
    def show_in_combobox_category(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category ''')
        data = self.cur.fetchall()
        #print(data)
        self.comboBox_3.clear()
        for category in data:
            #print(category[0])
            self.comboBox_3.addItem(category[0])
            self.comboBox_6.addItem(category[0])

    def show_in_author_combobox(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM authors ''')
        data = self.cur.fetchall()
        #print(data)
        self.comboBox_4.clear()
        for author in data:
            #print(category[0])
            self.comboBox_4.addItem(author[0])
            self.comboBox_7.addItem(author[0])


    def show_in_publisher_combobox(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', db = 'library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        data = self.cur.fetchall()
        #print(data)
        self.comboBox_5.clear()
        for publisher in data:
            #print(category[0])
            self.comboBox_5.addItem(publisher[0])
            self.comboBox_8.addItem(publisher[0])



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
