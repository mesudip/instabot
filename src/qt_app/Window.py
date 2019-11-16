from PyQt5.QtWidgets import QPushButton, QLineEdit, QCheckBox, QMainWindow, QFrame, QWidget, QStackedWidget, \
    QTextBrowser, QPlainTextEdit
from datetime import datetime
from qt_ui.loginform import Ui_Form as LoginForm
from qt_ui.mainwindow import Ui_MainWindow as MainWindowForm
from qt_ui.comment import Ui_Form as CommentForm
from qt_ui.filters import Ui_Form as FilterForm
from qt_ui.follow_unfollow import Ui_Form as FollowUnfollowForm
from qt_ui.like import Ui_Form as LikeForm
from qt_ui.status import Ui_Form as StatusForm
from qt_ui import ui_data
from threaded_instabot.async_bot import AsyncBot

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from . import db_connect


class Window(QMainWindow):
    login_request_signal = pyqtSignal([str, str])
    like_activate_signal = pyqtSignal(float)
    comment_activate_signal = pyqtSignal(list, float)
    follow_activate_signal = pyqtSignal(list, float)
    unfollow_activate_signal = pyqtSignal(list, float)

    like_stop_signal = pyqtSignal()
    comment_stop_signal = pyqtSignal()
    follow_stop_signal = pyqtSignal()
    unfollow_stop_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = MainWindowForm()

        # setup main Window's UI
        self.ui.setupUi(self)

        # setup Ui for login form.
        loginform = LoginForm()
        loginform.setupUi(self.ui.loginArea)

        # set window's title
        self.setWindowTitle("Instagram Bot")

        # create 5 widgets.to initialize the Ui. the loginUi is created by default already
        self.forms = {
            'status': StatusForm(),
            'like': LikeForm(),
            'follow': FollowUnfollowForm(),
            'comment': CommentForm(),
            'filter': FilterForm(),
            'login': LoginForm(),
            'dblogin': LoginForm()
        }
        self.widgets = {
            'status': QWidget(),
            'like': QWidget(),
            'follow': QWidget(),
            'comment': QWidget(),
            'filter': QWidget(),
            'login': QWidget(),
            'dblogin': QWidget()
        }

        self.button_action_map = {
            self.ui.status: self.widgets['status'],
            self.ui.like: self.widgets['like'],
            self.ui.follow: self.widgets['follow'],
            self.ui.comment: self.widgets['comment'],
            self.ui.filter: self.widgets['filter'],
        }
        self.colors = {
            'blue': '#0099cc',
            'red': '#F65F5F',
            'green': '#28B270'
        }

        # add all the widgets to display pane.
        for page in self.forms:
            self.forms[page].setupUi(self.widgets[page])
            self.ui.display.addWidget(self.widgets[page])

        self.ui.display.setCurrentWidget(self.widgets['login'])
        self.forms['login'].start_button.setText("Login to Instagram")

        # initialize bot and only the login connection with it.
        self.bot = AsyncBot()
        self.setup_bot_connections()
        self.forms['dblogin'].start_button.clicked.connect(self.handleFormButtonClick)
        self.forms['login'].start_button.clicked.connect(self.handleFormButtonClick)
        self.bot.moveToThread(self.bot)
        self.bot.start()

        self.show()

    def setup_bot_connections(self):
        self.login_request_signal.connect(self.bot.login)
        self.bot.login_response_signal.connect(self.handleLoginResponse)
        self.like_activate_signal.connect(self.bot.like)
        self.like_stop_signal.connect(self.bot.stop_like)

        self.comment_activate_signal.connect(self.bot.comment)
        self.comment_stop_signal.connect(self.bot.comment_stop)

        self.bot.log_generated.connect(self.log)
        self.follow_activate_signal.connect(self.bot.follow)
        self.follow_stop_signal.connect(self.bot.follow_stop)

    def setup_connections(self):
        self.ui.log.clicked.connect(self.ui.display.hide)
        # connections for handling navigation clicks
        self.ui.like.clicked.connect(self.handleNavigationClicks)
        self.ui.comment.clicked.connect(self.handleNavigationClicks)
        self.ui.follow.clicked.connect(self.handleNavigationClicks)
        self.ui.status.clicked.connect(self.handleNavigationClicks)
        self.ui.filter.clicked.connect(self.handleNavigationClicks)

        button = self.forms['like'].start_button
        button.running = False
        button.active_text = 'Currently liking periodically'
        button.unactive_text = 'Service Stopped'
        button.setText(self.forms['like'].start_button.unactive_text)
        button.setStyleSheet('background-color:#ff0000')
        button.associated_button = self.ui.like
        button.clicked.connect(self.handleFormButtonClick)

        button = self.forms['follow'].start_button
        button.running = False
        button.active_text_follow = 'Currently Following periodically'
        button.active_text_unfollow = 'Currently Unfollowing periodcally'
        button.unactive_text = 'Service Stopped'
        button.setText(self.forms['follow'].start_button.unactive_text)
        button.associated_button = self.ui.follow
        button.clicked.connect(self.handleFormButtonClick)

        button = self.forms['comment'].start_button
        button.running = False
        button.active_text = 'Currently Commenting periodically'
        button.unactive_text = 'Service Stopped'
        button.setText(self.forms['comment'].start_button.unactive_text)
        button.associated_button = self.ui.comment
        button.clicked.connect(self.handleFormButtonClick)

    def handleNavigationClicks(self, *args):
        self.ui.display.setHidden(False)
        self.ui.display.setCurrentWidget(self.button_action_map[self.sender()])

    def handleToggleActive(self, button):

        if button.running:
            button.setStyleSheet('background-color:' + self.colors['red'])
            button.associated_button.setStyleSheet("background-color:" + self.colors['red'] + ";border:none")
            print(button.unactive_text)
            button.setText(button.unactive_text)
            button.running = False

        else:
            button.setStyleSheet("background-color:" + self.colors['green'])
            button.associated_button.setStyleSheet("background-color:" + self.colors['green'] + ";border:none")
            # the active text is different only for the follow/unfollow section
            if hasattr(button, 'active_text'):
                button.setText(button.active_text)
            else:
                data = ui_data.follow_unfollow_data(self.forms['follow'])
                if data['action'] == 'follow':
                    button.setText(button.active_text_follow)
                else:
                    button.setText(button.active_text_unfollow)

            button.running = True

    def handleFormButtonClick(self, status):
        # when user clicks login button
        if self.sender() is self.forms['login'].start_button:
            self.ui.statusbar.showMessage("Trying to login in to instagram")
            data = ui_data.login_data(self.forms['login'])
            self.login_request_signal.emit(
                data['user_name'],
                data['password']
            )
        elif self.sender() is self.forms['dblogin'].start_button:
            self.ui.statusbar.showMessage("Trying to Authenticate with the system")
            data = ui_data.login_data(self.forms['dblogin'])
            verified = db_connect.verify(
                data['user_name'],
                data['password']
            )
            if verified:
                self.selfLog("Authenticated to the system")
                self.ui.statusbar.showMessage("Authenticated to the system")
                self.ui.display.setCurrentWidget(self.widgets['login'])
            else:
                print("Error Authenticating")
                self.selfLog(str(db_connect.lasterror))

        elif self.sender() is self.forms['like'].start_button:
            if self.sender().running:
                self.selfLog("Stopping Auto Like task")
                self.like_stop_signal.emit()
            else:
                rate = ui_data.like_data(self.forms['like'])['rate']
                self.like_activate_signal.emit(rate)

            self.handleToggleActive(self.sender())

        elif self.sender() is self.forms['comment'].start_button:

            if self.sender().running:
                self.selfLog("Stopping Auto Comment Task")
                self.comment_stop_signal.emit()
            else:
                result = ui_data.comment_data(self.forms['comment'])
                if 'format' in result['error']:
                    self.selfLog("Error! ", "Invalid comment format")
                    return
                self.comment_activate_signal.emit(result['format'], result['rate'])
            self.handleToggleActive(self.sender())

        elif self.sender() is self.forms['follow'].start_button:
            if self.sender().running:
                self.selfLog("Stopping Auto Follow/Unfollow Task")
                self.follow_stop_signal.emit()
                self.handleToggleActive(self.sender())
                self.sender().running = False
            else:
                result = ui_data.follow_unfollow_data(self.forms['follow'])
                if 'tags' in result['error']:
                    self.selfLog("Error! ", "No tags to start follow")
                    return
                if result['action'] == 'follow':
                    self.follow_activate_signal.emit(result['tags'], result['rate'])
                    self.handleToggleActive(self.sender())
                    self.sender().running = True
                else:
                    self.selfLog("Error! ", "Auto Unfollowing not implemented yet!")

            pass  # TODO : Implement unfollowing mechanism
        else:
            print("Button click ignored")

    @pyqtSlot(str)
    def handleLoginResponse(self, status):
        if status == 'success':
            self.setup_connections()
            self.ui.statusbar.showMessage("Logged in as " + self.bot.bot.user_login)
            self.ui.display.setCurrentWidget(self.widgets['status'])
        else:
            self.ui.statusbar.showMessage("Login in failed with message :" + status)

    @pyqtSlot(str)
    def log(self, logText: str):
        self.ui.logBrowser.setPlainText(self.ui.logBrowser.toPlainText() + '\n' + logText)
        self.ui.logBrowser.verticalScrollBar().setSliderPosition(
            self.ui.logBrowser.verticalScrollBar().maximum()
        )

    def selfLog(self, *args) -> None:
        '''
         For logging window's activities,
         Good programming would be : the async_bot being responsible to genere all the necessary log.
         But that's not happening, so window is logging some of the activities.
        :param args:
        :return:
        '''
        args = list(args)
        log = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for logUnit in args:
            log += ' > ' + logUnit
        self.log(log)
