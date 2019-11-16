from qt_ui.loginform import Ui_Form as LoginForm
from qt_ui.mainwindow import Ui_MainWindow as MainWindowForm
from qt_ui.comment import Ui_Form as CommentForm
from qt_ui.filters import Ui_Form as FilterForm
from qt_ui.follow_unfollow import Ui_Form as FollowUnfollowForm
from qt_ui.like import Ui_Form as LikeForm
from qt_ui.status import Ui_Form as StatusForm


def login_data(ui: LoginForm):
    return {
        'user_name': ui.uname_text.text(),
        'password': ui.password_text.text(),
        'remember': bool(ui.remember_checkbox.checkState())
    }


def comment_data(ui: CommentForm):
    default_format = "Nice,Wow"
    dict = {'error': []}
    try:
        rate = float(ui.rate.text())
    except ValueError as e:
        rate = 0.0
        ui.rate.setText('0')
        dict['error'].append('rate')
    try:
        format = [x.strip() for x in str(ui.format_text.toPlainText()).split(',')]
        if len(format) is 0:
            dict['error'].append('format')
    except Exception as e:
        format = default_format
        dict['error'].append('format')
    dict['format'] = format
    dict['rate'] = rate
    return dict


def filter_data(ui: FilterForm):
    return {
        'black_list': ui.black_list_text.toPlainText(),
        'tags': ui.tag_text.toPlainText(),
        'tag_action': 'allow' if ui.allow_radio.isChecked() else 'deny'
    }


def follow_unfollow_data(ui: FollowUnfollowForm):
    dict = {}
    dict['error'] = []
    try:
        rate = float(ui.rate_text.text())
    except ValueError as e:
        rate = 0.0
        ui.rate_text.setText('0')
        dict['error'].append('rate')

    tags = [y.replace('#', '') for y in [x.strip() for x in str(ui.tag_text.toPlainText()).split(',')]]

    if len(tags) is 0:
        dict['error'].append('tags')

    dict.update({
        'rate': rate,
        'action': 'follow' if ui.follow_radio.isChecked() else 'unfollow',
        'tags': tags
    })
    return dict


def like_data(ui: LikeForm):
    try:
        rate = float(ui.rate_text.text())
    except ValueError as e:
        rate = 0.0
        ui.rate_text.setText('0')
    return {
        'rate': rate
    }


def status_data(ui: StatusForm):
    return {
        'current': {
            'likes': ui.cur_like,
            'follows': ui.cur_follow,
            'unfollows': ui.cur_unfollow,
            'comments': ui.cur_comment

        },
        'lifetime': {
            'likes': ui.life_like,
            'follows': ui.life_follow,
            'unfollows': ui.life_unfollow,
            'comments': ui.life_comment
        }
    }


from PyQt5.QtWidgets import QLineEdit


def status_write(ui: StatusForm, data: dict):
    current = data['current']
    ui.cur_like.setText(current['likes'])
    ui.cur_follow.setText(current['follows'])
    ui.cur_unfollow.setText(current['unfollows'])
    ui.cur_comment.setText(current['comments'])

    current = data['lifetime']
    ui.life_like.setText(current['likes'])
    ui.life_follow.setText(current['follows'])
    ui.life_unfollow.setText(current['unfollows'])
    ui.life_comment.setText(current['comments'])
