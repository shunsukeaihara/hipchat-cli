# -*- coding: utf-8 -*-
import sys
import gdbm
import datetime


def dt_from_str(st):
    return datetime.datetime.strptime(st, '%Y-%m-%d %H:%M:%S.%f')


def check(title):
    now = datetime.datetime.now()
    db = gdbm.open("sent.db", 'cs')
    if title not in db:
        db[title] = str(now)  # 送信時刻更新
        return 1
    else:
        try:
            dt = dt_from_str(db[title])
            if (now - dt) < datetime.timedelta(minutes=10):
                # 前回送信より10分以内
                return 0  # 送信しない
            else:
                db[title] = str(now)  # 送信時刻を更新
                return 1
        except:
            db[title] = str(now)
            return 1


if __name__ == "__main__":
    """
    タイトルを入れて、同一タイトルのメッセージが10分以内に送信されていなければ1をプリント
    そうでなければ0をプリントして送らない
    """
    title = sys.argv[1]
    print check(title),
