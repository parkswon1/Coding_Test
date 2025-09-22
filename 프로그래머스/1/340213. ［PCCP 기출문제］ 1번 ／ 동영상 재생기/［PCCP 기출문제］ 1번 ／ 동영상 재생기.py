def solution(videoLen, pos, opStart, opEnd, commands):
    def toSec(t):
        m = int(t[0:2])
        s = int(t[3:5])
        return m * 60 + s

    def toMmss(sec):
        m = sec // 60
        s = sec % 60
        return f"{m:02d}:{s:02d}"

    videoSec = toSec(videoLen)
    posSec = toSec(pos)
    opStartSec = toSec(opStart)
    opEndSec = toSec(opEnd)

    # 시작 위치가 오프닝이면 건너뛰기
    if opStartSec <= posSec < opEndSec:
        posSec = opEndSec

    for cmd in commands:
        # 명령 처리 전/후로 오프닝이면 건너뛰기
        if opStartSec <= posSec < opEndSec:
            posSec = opEndSec

        if cmd == "prev":
            posSec = max(0, posSec - 10)
        else:  # "next"
            posSec = min(videoSec, posSec + 10)

        if opStartSec <= posSec < opEndSec:
            posSec = opEndSec

    return toMmss(posSec)
