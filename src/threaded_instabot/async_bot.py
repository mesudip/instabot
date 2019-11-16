from datetime import datetime
from instabot import InstaBot
import sys
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal
from instabot import likers_protocols as likers_protocol
from PyQt5.QtCore import QTimer
import instabot.commands.login as login


class AsyncBot(QThread):
    """
        Async Bot
    """
    login_response_signal = pyqtSignal(str)
    log_generated = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # setup like timer
        timer = QTimer(self)
        timer.timeout.connect(self.like_task)
        self.like_timer = timer
        self.stop_like = timer.stop

        # setup comment timier
        timer = QTimer(self)
        timer.timeout.connect(self.comment_task)
        self.comment_timer = timer
        self.comment_stop = timer.stop

        # setup follow timer
        timer = QTimer(self)
        timer.timeout.connect(self.follow_task)
        self.follow_timer = timer
        self.follow_stop = timer.stop

        # setup unfollow timer
        timer = QTimer(self)
        timer.timeout.connect(self.unfollow_task)
        self.unfollow_timer = timer
        self.unfollow_stop = timer.stop

        self.bot = InstaBot(
            login="",
            password="",
            like_per_day=1000)
        self.started.connect(self.initialize_task)

    def detach(self):
        self.moveToThread(self)

    @pyqtSlot(str, str)
    def login(self, username, password):
        self.log("Trying to log in as " + username)
        if login.login_with_password(self.bot, username, password):
            self.bot.populate_user_blacklist()
            self.login_response_signal.emit("success")
            self.log("Logged in successfully !")
        else:
            self.login_response_signal.emit("Error!  Login failed")
            self.log("Error !", "Login Failed")

    @pyqtSlot(float)
    def like(self, rate_per_hour):
        if rate_per_hour < 0.005:
            like_sleep_time = 999999999
        else:
            rate = rate_per_hour / 60 / 60
            like_sleep_time = int(1 / rate) * 1000

        self.like_timer.start(like_sleep_time)
        self.log("Like Task Scheduled", "1 Like every " + "%.2f" % (like_sleep_time / 1000) + " seconds")

    @pyqtSlot()
    def like_task(self):
        # simply like the media
        self.log(*likers_protocol.recent_feed_like(self.bot))

    @pyqtSlot(list, float)
    def comment(self, comment_list: list, rate_per_hour):
        if rate_per_hour < 0.005:
            comment_sleep_time = 99999999
        else:
            rate = rate_per_hour / 60 / 60
            comment_sleep_time = int(1 / rate) * 1000
        self.comment_timer.start(comment_sleep_time)
        self.log("Comment Task Scheduled", "1 Comment every " + "%.2f" % (comment_sleep_time / 1000) + " seconds")
        self.comment_list = comment_list

    @pyqtSlot()
    def comment_task(self):
        self.log(*likers_protocol.recent_feed_comment(self.bot, self.comment_list))

        pass

    @pyqtSlot(list, float)
    def follow(self, follow_tag_list: list, rate_per_hour):
        if rate_per_hour < 0.005:
            follow_sleep_time = 99999999
        else:
            rate = rate_per_hour / 60 / 60
            follow_sleep_time = int(1 / rate) * 1000
        self.follow_timer.start(follow_sleep_time)
        self.log("Follow Task Scheduled", "1 follow every " + "%.2f" % (follow_sleep_time / 1000) + " seconds")
        self.follow_tag_list = follow_tag_list

    @pyqtSlot()
    def follow_task(self):
        self.log(*likers_protocol.user_follow(self.bot, self.follow_tag_list))
        pass

    @pyqtSlot(float)
    def unfollow(self, rate):
        pass

    @pyqtSlot()
    def unfollow_task(self):
        pass

    @pyqtSlot()
    def initialize_task(self):
        if login.login_with_session(self.bot):
            self.login_response_signal.emit("success")
        else:
            self.log_generated.emit("Previous session not found")

    def log(self, *args):
        args = list(args)
        log = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for logUnit in args:
            log += ' > ' + logUnit
        self.log_generated.emit(log)
