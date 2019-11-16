from instabot import InstaBot
import pickle
import re
import time
import random
import os


def login_with_session(bot: InstaBot):
    if bot.session_file and os.path.isfile(bot.session_file):
        bot.logger.info(f"Found session file {bot.session_file}")
        with open(bot.session_file, "rb") as i:
            cookies = pickle.load(i)
            bot.s.cookies.update(cookies)
            bot.user_login = cookies.__user_name
            return __verifyLogin(bot)
    return False


def __verifyLogin(bot: InstaBot):
    r = bot.s.get("https://www.instagram.com/")
    bot.csrftoken = re.search('(?<="csrf_token":")\w+', r.text).group(0)
    bot.s.cookies["csrftoken"] = bot.csrftoken
    bot.s.headers.update({"X-CSRFToken": bot.csrftoken})
    finder = r.text.find(bot.user_login)
    if finder != -1:
        bot.user_id = bot.get_user_id_by_username(bot.user_login)
        bot.login_status = True
        bot.logger.info(f"{bot.user_login} login success!\n")
        if bot.session_file is not None:
            bot.logger.info(
                f"Saving cookies to session file {bot.session_file}"
            )
            with open(bot.session_file, "wb") as output:
                bot.s.cookies.__user_name = bot.user_login
                pickle.dump(bot.s.cookies, output, pickle.HIGHEST_PROTOCOL)
        return True
    else:
        bot.login_status = False
        bot.logger.error("Login error! Check your login data!")
        if bot.session_file and os.path.isfile(bot.session_file):
            try:
                os.remove(bot.session_file)
            except:
                bot.logger.info(
                    "Could not delete session file. Please delete manually"
                )

        bot.prog_run = False
        return False


def login_with_password(bot: InstaBot, username=None, password=None):
    bot.user_login = username
    successfulLogin = False
    bot.logger.info("Trying to login as {}...".format(username))
    bot.login_post = {
        "username": username,
        "password": password,
    }
    r = bot.s.get(bot.url)
    csrf_token = re.search('(?<="csrf_token":")\w+', r.text).group(0)
    bot.s.headers.update({"X-CSRFToken": csrf_token})
    time.sleep(5 * random.random())
    login = bot.s.post(
        bot.url_login, data=bot.login_post, allow_redirects=True
    )
    if login.status_code not in (200, 400):
        # Handling Other Status Codes and making debug easier!!
        bot.logger.debug("Login Request didn't return 200 as status code!")
        bot.logger.debug(
            "Here is more info for debugging or creating an issue"
            "==============="
            "Response Status:{login.status_code}"
            "==============="
            "Response Content:{login.text}"
            "==============="
            "Response Header:{login.headers}"
            "==============="
        )
        return False
    else:
        bot.logger.debug("Login request succeeded ")

    loginResponse = login.json()
    try:
        bot.csrftoken = login.cookies["csrftoken"]
        bot.s.headers.update({"X-CSRFToken": bot.csrftoken})
    except Exception as exc:
        bot.logger.warning("Something wrong with login")
        bot.logger.debug(login.text)
        bot.logger.exception(exc)
        return False
    if loginResponse.get("errors"):
        bot.logger.error(
            "Something is wrong with Instagram! Please try again later..."
        )
        bot.logger.error(loginResponse["errors"]["error"])
        return False
    elif loginResponse.get("message") == "checkpoint_required":
        try:
            if "instagram.com" in loginResponse["checkpoint_url"]:
                challenge_url = loginResponse["checkpoint_url"]
            else:
                challenge_url = f"https://instagram.com{loginResponse['checkpoint_url']}"
            bot.logger.info(f"Challenge required at {challenge_url}")
            with bot.s as clg:
                clg.headers.update(
                    {
                        "Accept": "*/*",
                        "Accept-Language": bot.config.get("accept_language"),
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Host": "www.instagram.com",
                        "Origin": "https://www.instagram.com",
                        "User-Agent": bot.user_agent,
                        "X-Instagram-AJAX": "1",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "x-requested-with": "XMLHttpRequest",
                    }
                )
                # Get challenge page
                challenge_request_explore = clg.get(challenge_url)

                # Get CSRF Token from challenge page
                challenge_csrf_token = re.search(
                    '(?<="csrf_token":")\w+', challenge_request_explore.text
                ).group(0)
                # Get Rollout Hash from challenge page
                rollout_hash = re.search(
                    '(?<="rollout_hash":")\w+', challenge_request_explore.text
                ).group(0)

                # Ask for option 1 from challenge, which is usually Email or Phone
                challenge_post = {"choice": 1}

                # Update headers for challenge submit page
                clg.headers.update({"X-CSRFToken": challenge_csrf_token})
                clg.headers.update({"Referer": challenge_url})

                # Request instagram to send a code
                challenge_request_code = clg.post(
                    challenge_url, data=challenge_post, allow_redirects=True
                )

                # User should receive a code soon, ask for it
                challenge_userinput_code = input(
                    "Challenge Required.\n\nEnter the code sent to your mail/phone: "
                )
                challenge_security_post = {
                    "security_code": int(challenge_userinput_code)
                }

                complete_challenge = clg.post(
                    challenge_url,
                    data=challenge_security_post,
                    allow_redirects=True,
                )
                if complete_challenge.status_code != 200:
                    bot.logger.info("Entered code is wrong, Try again later!")
                    return
                bot.csrftoken = complete_challenge.cookies["csrftoken"]
                bot.s.headers.update(
                    {"X-CSRFToken": bot.csrftoken, "X-Instagram-AJAX": "1"}
                )
                successfulLogin = complete_challenge.status_code == 200

        except Exception as err:
            bot.logger.debug(f"Login failed, response: \n\n{login.text} {err}")
            return False
    elif loginResponse.get("authenticated") is False:
        bot.logger.error("Login error! Check your login data!")
        return False
    else:
        rollout_hash = re.search('(?<="rollout_hash":")\w+', r.text).group(0)
        bot.s.headers.update({"X-Instagram-AJAX": rollout_hash})
        bot.login_status = True
    bot.s.cookies["csrftoken"] = bot.csrftoken
    bot.s.cookies["ig_vw"] = "1536"
    bot.s.cookies["ig_pr"] = "1.25"
    bot.s.cookies["ig_vh"] = "772"
    bot.s.cookies["ig_or"] = "landscape-primary"
    return __verifyLogin(bot)
