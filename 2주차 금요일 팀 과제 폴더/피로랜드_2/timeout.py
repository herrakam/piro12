import signal


class TimeoutError(Exception):
    pass


def timeout(seconds=10):
    def decorator(func):
        # 시그널 발생하면 timeoutError() 발생시키도록 처리
        def timeout_handler(signum, frame):
            raise TimeoutError()

        def wrapper(*args, **kwargs):
            # 시그널을 받았을 때 실행될 사용자가 만든 핸들러를 지정
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                # 계획된 모든 알람을 취소
                signal.alarm(0)
            return result
        return wrapper
    return decorator
