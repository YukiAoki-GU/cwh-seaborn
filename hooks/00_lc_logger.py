
import os, uuid, pickle

from pathlib import Path

from datetime import datetime, timezone, timedelta
JST = timezone(timedelta(hours=9), 'JST')

SERVER_SIGNATURE = str(uuid.uuid1())

def _log_cell(result):

    try:

        ip = get_ipython()

        code = getattr(result.info, "raw_cell", "")

        status = "ok" if result.success else "error"

        cwd = Path.cwd()

        logdir = cwd / ".log" / datetime.now(JST).strftime("%Y%m%d")

        logdir.mkdir(parents=True, exist_ok=True)

        now = datetime.now(JST)

        base = now.strftime("%Y%m%d-%H%M%S-") + f"{now.microsecond//1000:04d}"

        logfile = logdir / f"{base}.log"

        pklfile = logdir / f"{base}-0.pkl"

        err = result.error_in_exec or result.error_before_exec

        with open(logfile, "w", encoding="utf-8") as f:

            f.write(code.rstrip() + "\n")

            f.write("----\n")

            f.write(f"path: {logfile}\n")

            f.write(f"notebook_path: unknown\n")

            f.write(f"server_signature: {SERVER_SIGNATURE}\n")

            f.write(f"uid: {os.getuid()}\n")

            f.write(f"gid: {os.getgid()}\n")

            f.write(f"start time: {now.strftime('%Y-%m-%d %H:%M:%S')}(JST)\n")

            f.write("----\n\n")

            f.write("----\n")

            f.write(f"end time: {datetime.now(JST).strftime('%Y-%m-%d %H:%M:%S')}(JST)\n")

            f.write("0 chunks with matched keywords or errors\n")

            f.write("----\n")

            f.write(f"result: {pklfile}\n")

            f.write(f"execute_reply_status: {status}\n")

            if err:

                f.write(f"error: {repr(err)}\n")

        with open(pklfile, "wb") as f:

            pickle.dump({"code": code, "status": status, "error": repr(err) if err else None}, f)

    except Exception:

        pass

ip = get_ipython()

if ip is not None:

    ip.events.register("post_run_cell", _log_cell)

