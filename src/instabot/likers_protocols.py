#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time
import json
from instabot.instabot import InstaBot


def get_user_id_post_page(bot: InstaBot, code):
    if bot.login_status:
        log_string = 'Get user id on post page'
        bot.write_log(log_string)
        url = 'https://www.instagram.com/p/%s/?__a=1' % (code)
        try:
            r = bot.s.get(url)
            all_data = json.loads(r.text)

            bot.user_list = list(all_data['media']['likes']['nodes'])
            log_string = "User likes this post = %i" % (
                all_data['media']['likes']['count'])
            bot.write_log(log_string)
        except:
            bot.media_on_feed = []
            bot.write_log("Except on get user list!!!!")
            time.sleep(10)
            return 0
    else:
        return 0


# from instabot.instabot import InstaBot
def caption_format(caption: str):
    max = 24
    if len(caption) > max:
        caption = caption[:max - 4]
        caption += ' ...'
    caption.replace("\n", ' ')
    return caption


def media_like(bot: InstaBot, media_list: list):
    '''
            Likes media in   media_list and pops it.
        '''
    if len(media_list) == 0:
        return False
    media = media_list.pop()

    if 10 <= media["likes"]["count"] < 100:
        get_user_id_post_page(
            bot, media["code"])
    # username_checker(self)
    bot.like(bot, media)


def recent_feed_like(bot: InstaBot):
    """
    Automatically fetches ank like recent_feed_likes
    :param bot:
    :return:
    """
    # first check if self.media_on feed has length zero.
    if len(bot.media_to_like) is 0:
        print("Refreshing New Media")
        if bot.startup:
            first_init(bot)
            # bot.get_medias_from_recent_feed()
            # bot.fetch_recent_media_recursive(50)
        elif not bot.get_medias_from_recent_feed():
            return "Error : getting recent media"
        else:
            # shorthand to get all the media that was not liked.
            for x in bot.media_on_feed:
                if 'viewer_has_liked' in x['node']:
                    if not x['node']['viewer_has_liked']:
                        bot.media_to_like.append(x)
    # no media to like? it is awesome
    if len(bot.media_to_like) is 0:
        return "Wow! ", " no media remain to like  on recent feed"

    # get a media to like
    media = bot.media_to_like.pop()
    while media['node']['id'] in bot.liked_medias:
        if len(bot.media_to_like) is 0:
            return "Wow! ", " no media remain to like  on recent feed"
        media = bot.media_to_like.pop()

    try:
        caption = media['node']['edge_media_to_caption']['edges'][0]['node']['text']
    except Exception:
        caption = ''
    success = bot.like(media['node']['id'])
    if success:
        bot.liked_medias.add(media['node']['id'])
        return "Liked a post", "User : " + media['node']['owner']['full_name'], \
               "Caption : " + caption_format(caption)


def recent_feed_comment(bot: InstaBot, comment_list: list):
    """
    Automatically fetches new media  and comments on them.
    :param bot:
    :return:
    """
    # first check if self.media_on feed has length zero.
    if len(bot.media_to_comment) is 0:
        if bot.startup:
            first_init(bot)
        elif not bot.get_medias_from_recent_feed():
            return "Error : getting recent media"
        else:
            bot.media_to_comment = []
            for y in bot.media_on_feed:
                # have somebody commented on the post?
                if 'edge_media_preview_comment' in y['node']:
                    # loop through all the comments to see, if the commentor is the user him/herself.
                    already_commented = False
                    for x in y['node']['edge_media_preview_comment']['edges']:
                        if x['node']['owner']['id'] == bot.user_id:
                            already_commented = True

                    if not already_commented:
                        bot.media_to_comment.append(y)

    if len(bot.media_to_comment) is 0:
        return "Wow! ", " no media remain to comment  on recent feed"

    if len(bot.media_on_feed) is 0:
        if not bot.get_medias_from_recent_feed():
            return False
    if len(bot.media_on_feed) is 0:
        return False
    media = bot.media_on_feed.pop()
    # find the caption of the media
    try:
        caption = media['node']['edge_media_to_caption']['edges'][0]['node']['text']
    except Exception:
        caption = ''

    # if length of comment_list is 0, set comment to '.'
    if len(comment_list) is 0:
        comment = '.'
    else:
        comment = random.choice(comment_list)

    success = bot.comment(media['node']['id'], comment)
    print("coment :", comment)

    if success:
        return "Commented on a post", \
               "Comment : " + caption_format(comment), \
               "User : " + media['node']['owner']['full_name'], \
               "Caption : " + caption_format(caption)
    else:
        return "Commented on a post", \
               "Failed! ", \
               "User : " + media['node']['owner']['full_name'], \
               "Caption : " + caption_format(caption)


def user_follow(bot: InstaBot, tag_list: list):
    """
    Automatically fetches ank like recent_feed_likes
    :param bot:
    :return:
    """
    if len(tag_list) > 0:
        tag = random.choice(tag_list)
    else:
        return "Error!", "List of tags is empty"
    if len(bot.media_by_tag) is 0:
        bot.media_by_tag = bot.get_media_id_by_tag(tag)
    if len(bot.media_by_tag) is 0:
        return "Error", "no media on recent feed"
    media = bot.media_by_tag.pop()
    try:
        uid = media['owner']['id']
    except Exception:
        return "Error !", "No owner info"

    success = bot.follow(uid)
    if success:
        return "Foollowed a user", "ID : " + uid


def first_init(bot: InstaBot):
    bot.startup = False
    # this means the application has just started up.
    print("Fetching most recent 50 medias")
    bot.get_medias_from_recent_feed()
    # bot.fetch_recent_media_recursive(50)

    bot.media_to_comment = []
    for y in bot.media_on_feed:
        # have somebody commented on the post?
        if 'edge_media_to_comment' in y['node']:
            # loop through all the comments to see, if the commentor is the user him/herself.
            already_commented = False
            for x in y['node']['edge_media_to_comment']['edges']:
                if x['node']['owner']['id'] == bot.user_id:
                    already_commented = True

            if not already_commented:
                bot.media_to_comment.append(y)
    bot.media_to_like = []
    for x in bot.media_on_feed:
        if 'viewer_has_liked' in x['node']:
            if not x['node']['viewer_has_liked']:
                bot.media_to_like.append(x)
