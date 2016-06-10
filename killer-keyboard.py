import signal

import kk.events.caps as caps
import kk.events.alphanum as alphanum
import kk.ckb as ckb

def main():
    global ckbObj

    ckbObj = ckb.CKB("ffffff")
    capsObj = caps.Caps(ckbObj)
    keyObj = alphanum.AlphaNum(ckbObj)

    for line in ckbObj.notifier:
        if line.strip("\n") in " ".join(keyObj.events):
            keyObj.action(line)
        elif line.strip("\n") in " ".join(capsObj.events):
            capsObj.action(line)

def cleanup(signum, frame):
    ckbObj.reset()

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, cleanup)
    signal.signal(signal.SIGINT, cleanup)

    main()
