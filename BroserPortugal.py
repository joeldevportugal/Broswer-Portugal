from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QMenuBar, QMenu, QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def go_home(self):
        self.browser.setUrl(QUrl('https://www.ciccopn.pt/'))

    def go_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())

    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.microsoft.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Barra de navegação
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Botão voltar
        voltar_btn = QAction('<<=', self)
        voltar_btn.triggered.connect(self.browser.back)
        navbar.addAction(voltar_btn)

        # Botão atualizar
        atualizar_btn = QAction('atualizar', self)
        atualizar_btn.triggered.connect(self.browser.reload)
        navbar.addAction(atualizar_btn)

        # Botão Home
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.go_home)
        navbar.addAction(home_btn)

        # Botão avançar
        avancar_btn = QAction('=>>', self)
        avancar_btn.triggered.connect(self.browser.forward)
        navbar.addAction(avancar_btn)

        # Barra de endereço
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.go_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

        # Menus
        menu_bar = self.menuBar()

        # Menu Arquivo
        file_menu = menu_bar.addMenu('Arquivo')

        # Ação Sair
        sair_action = QAction('Sair', self)
        sair_action.triggered.connect(self.close)
        file_menu.addAction(sair_action)

        # Menu Ajuda
        ajuda_menu = menu_bar.addMenu('Ajuda')

        # Ação Sobre
        sobre_action = QAction('Sobre', self)
        sobre_action.triggered.connect(self.show_about_dialog)
        ajuda_menu.addAction(sobre_action)

    def show_about_dialog(self):
        about_text = 'Este é um navegador básico desenvolvido com PyQt5.\n Autores: Joel e Julio\n: paises : Portugal e Brasil'
        QMessageBox.about(self, 'Sobre', about_text)


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon(r'C:\Users\HP\Desktop\Broser\icon\icon1.ico'))  # Altere para o caminho correto do ícone
    QApplication.setApplicationName('Browser Portugal')
    window = MainWindow()
    app.exec_()
