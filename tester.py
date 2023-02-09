from subprocess import PIPE, Popen, run
from threading import Thread
from time import sleep

try:
    from queue import Queue, Empty
except ImportError:
    from Queue import Queue, Empty  # python 2.x

COLORIZE = True
PYTHON = "python"

SAMPLES = [
    {
        "name": "Black queen vs white king",
        "input": [
            "w",
            "     k  ",
            " p      ",
            "       p",
            "        ",
            "   b   P",
            "P  P  p ",
            " q    P ",
            "K       ",
        ],
        "output": "mate",
    },
    {
        "name": "Rooks throw bricks for black king!",
        "input": [
            "b",
            "k       ",
            "      p ",
            "        ",
            "    p   ",
            "    P   ",
            " R    P ",
            "R       ",
            "    K   ",
        ],
        "output": "mate",
    },
    {
        "name": "Starting position",
        "input": [
            "b",
            "rnbqkbnr",
            "pppppppp",
            "        ",
            "        ",
            "        ",
            "        ",
            "PPPPPPPP",
            "RNBQKBNR",
        ],
        "output": "not mate",
    },
    {
        "name": "Just a game",
        "input": [
            "w",
            "r   k  r",
            "ppp  pbp",
            "  qp  p ",
            "n   pbB ",
            "  PPP n ",
            "     N P",
            "PP   PP ",
            "RN QKB R",
        ],
        "output": "not mate",
    },
    {
        "name": "Scholar's Mate",
        "input": [
            "b",
            "r bqkbnr",
            "pppp Q p",
            "  n   p ",
            "    p   ",
            "  B P   ",
            "        ",
            "PPPP PPP",
            "RNB K NR",
        ],
        "output": "mate",
    },
    {
        "name": "Italian Game Smothered Mate",
        "input": [
            "w",
            "r b kbnr",
            "pppp Npp",
            "        ",
            "        ",
            "    q   ",
            "     n  ",
            "PPPPBP P",
            "RNBQKR  ",
        ],
        "output": "mate",
    },
    {
        "name": "Modern defense",
        "input": [
            "b",
            "rnbqkbnr",
            "ppp  ppp",
            "        ",
            "   p    ",
            "    Pp  ",
            "     N  ",
            "PPPP  PP",
            "RNBQKB R",
        ],
        "output": "not mate",
    },
    {
        "name": "Five to one",
        "input": [
            "w",
            "   k    ",
            "  q b   ",
            "      b ",
            "       r",
            "   K    ",
            "        ",
            "  n     ",
            "        ",
        ],
        "output": "mate",
    },
    {
        "name": "special - 1",
        "input": [
            "w",
            "        ",
            "        ",
            "    k   ",
            "        ",
            "    K   ",
            "r       ",
            "    n   ",
            "        ",
        ],
        "output": "not mate",
    },
    {
        "name": "special - 2",
        "input": [
            "w",
            "        ",
            "        ",
            "    k   ",
            "   p    ",
            "    K   ",
            "r       ",
            "    n   ",
            "        ",
        ],
        "output": "mate",
    },
    {
        "name": "special - 3",
        "input": [
            "b",
            "        ",
            "        ",
            "    K   ",
            "   P    ",
            "    k   ",
            "R       ",
            "    N   ",
            "        ",
        ],
        "output": "not mate",
    },
    {
        "name": "special - 4",
        "input": [
            "b",
            "        ",
            "        ",
            "  B K   ",
            "        ",
            "    k   ",
            "R       ",
            "    N   ",
            "        ",
        ],
        "output": "mate",
    },
    {
        "name": "special - 5",
        "input": [
            "w",
            " q  k   ",
            "b       ",
            "b    n  ",
            "       r",
            "    K   ",
            "        ",
            "   n    ",
            "        ",
        ],
        "output": "mate",
    },
    {
        "name": "special - 6",
        "input": [
            "w",
            " Q  k   ",
            "B       ",
            "B    N  ",
            "       R",
            "    K   ",
            "        ",
            "   N    ",
            "        ",
        ],
        "output": "not mate",
    },
    {
        "name": "special - 7",
        "input": [
            "b",
            " Q  k   ",
            "B       ",
            "B    N  ",
            "       R",
            "    K   ",
            "        ",
            "   N    ",
            "        ",
        ],
        "output": "not mate",
    },
]

py_ver_proc = run([PYTHON, "--version"], stdout=PIPE)
py_ver = py_ver_proc.stdout.decode("utf-8").strip()
if not py_ver.startswith("Python 3"):
    try:
        py_ver_proc = run(["python3", "--version"], stdout=PIPE)
        py_ver = py_ver_proc.stdout.decode("utf-8").strip()
        if py_ver.startswith("Python 3"):
            PYTHON = "python3"
    except:  # noqa
        pass

print("Using python version:", py_ver)

stdout_q = Queue()
proc: Popen = None


def enqueue_output(out):
    for line in iter(out.readline, ""):
        stdout_q.put_nowait(line)
    out.close()


def err_printer(err):
    for line in iter(err.readline, ""):
        if COLORIZE:
            print("\033[33m" + line + "\033[39m", end="")
        else:
            print(line, end="")
    err.close()


stdout_reader: Thread = None
err_reader: Thread = None


def exec_solution():
    global proc, err_reader, stdout_reader
    proc = Popen(
        [PYTHON, "solution.py"], stdout=PIPE, stderr=PIPE, stdin=PIPE, encoding="utf-8"
    )
    sleep(0.2)
    if proc.poll() is not None:
        if proc.returncode == 2:
            print("Can not find your file, please rename it to 'solution.py'")
        else:
            print("unknown error while running your file")
        exit()
    stdout_reader = Thread(target=enqueue_output, args=(proc.stdout,), daemon=True)
    err_reader = Thread(target=err_printer, args=(proc.stderr,), daemon=True)
    stdout_reader.start()
    err_reader.start()


def kill_solution():
    if proc.poll() is None:
        proc.kill()


def readline(timeout=30) -> str | None:
    try:
        line = stdout_q.get(True, timeout)
    except Empty:
        if proc.poll() is not None:
            print("child process closed unexpected")
            exit()
        else:
            return None
    return line.strip()


def write(*lines: str, end="\n", sep=" "):
    if proc.poll() is not None:
        print("child process closed unexpected")
        exit()
    line = sep.join(lines) + end
    proc.stdin.write(line)
    proc.stdin.flush()


print("\n")

for testcase, sample in enumerate(SAMPLES, 1):
    if COLORIZE:
        print(
            "\033[47m" + "\033[30m" + " Testcase",
            testcase,
            "->",
            sample["name"] + " \033[39m" + "\033[49m",
        )
    else:
        print("Testcase", testcase, "->", sample["name"])
    exec_solution()
    for inp in sample["input"]:
        write(inp)
    output = readline()
    print("  → Output:", output)

    kill_solution()
    err_reader.join()
    stdout_reader.join()
    if output != sample["output"]:
        if COLORIZE:
            print(
                f'  \033[31mX\033[39m Failed: expected "{sample["output"]}" but got "{str(output)}"'
            )
        else:
            print(f'  X Failed: expected "{sample["output"]}" but got "{str(output)}"')
        break
    else:
        if COLORIZE:
            print("  \033[32m✔\033[39m Passed")
        else:
            print("  ✔ Passed")

    # clear output buffer
    while not stdout_q.empty():
        stdout_q.get_nowait()

print("\n\n---Test finished---")
